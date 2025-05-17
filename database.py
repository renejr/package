import sqlite3
import os
import uuid
import socket
from datetime import datetime

class Database:
    def __init__(self):
        self.db_path = os.path.join(os.path.dirname(__file__), 'chat_export.db')
        self.machine_id = self._get_or_create_machine_id()
        self.ip = self._get_local_ip()
        self._create_tables()

    def _get_or_create_machine_id(self):
        id_file = os.path.join(os.path.dirname(__file__), '.machine_id')
        if os.path.exists(id_file):
            with open(id_file, 'r') as f:
                return f.read().strip()
        machine_id = str(uuid.uuid4())
        with open(id_file, 'w') as f:
            f.write(machine_id)
        return machine_id

    def _get_local_ip(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return '127.0.0.1'

    def _create_tables(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Tabela channels
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS channels (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    channel_id TEXT,
                    name TEXT,
                    description TEXT
                )
            ''')

            # Tabela messages
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS messages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    channel_id TEXT,
                    author TEXT,
                    timestamp TEXT,
                    content TEXT,
                    machine_id TEXT,
                    ip TEXT
                )
            ''')

            # Tabela attachments
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS attachments (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    message_id INTEGER,
                    url TEXT,
                    FOREIGN KEY (message_id) REFERENCES messages(id)
                )
            ''')

            # Tabela import_log
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS import_log (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    import_time TEXT,
                    machine_id TEXT,
                    ip TEXT,
                    file_path TEXT,
                    export_type TEXT
                )
            ''')
            
            conn.commit()

    def log_export(self, file_path, export_type):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO import_log (import_time, machine_id, ip, file_path, export_type)
                VALUES (?, ?, ?, ?, ?)
            ''', (
                datetime.now().isoformat(),
                self.machine_id,
                self.ip,
                file_path,
                export_type
            ))
            conn.commit()

    def save_messages(self, channel_id, messages):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            for msg in messages:
                cursor.execute('''
                    INSERT INTO messages (channel_id, author, timestamp, content, machine_id, ip)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (
                    channel_id,
                    msg.get('author', 'Desconhecido'),
                    msg.get('timestamp', ''),
                    msg.get('content', ''),
                    self.machine_id,
                    self.ip
                ))
                msg_id = cursor.lastrowid
                
                attachments = msg.get('attachments', [])
                if isinstance(attachments, str):
                    attachments = [attachments]
                
                for att in attachments:
                    if att:
                        cursor.execute('''
                            INSERT INTO attachments (message_id, url)
                            VALUES (?, ?)
                        ''', (msg_id, att))
            
            conn.commit()

    def get_log_entries(self, limit=50):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT import_time, machine_id, ip, file_path, export_type 
                FROM import_log 
                ORDER BY import_time DESC 
                LIMIT ?
            ''', (limit,))
            return cursor.fetchall()