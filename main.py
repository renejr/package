import sys
import os
import json
import shutil
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QFileDialog, QMessageBox,
    QTableWidgetItem
)
from ui_mainwindow import Ui_MainWindow
from converter import json_to_html, json_to_md, json_to_pdf
from database import Database

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.current_folder = None
        self.current_file = None
        self.current_json_data = None
        self.db = Database()

        # Conectar eventos
        self.ui.select_btn.clicked.connect(self.select_folder_or_file)
        self.ui.file_list.itemClicked.connect(self.display_file_content)
        self.ui.html_btn.clicked.connect(self.convert_to_html)
        self.ui.md_btn.clicked.connect(self.convert_to_md)
        self.ui.pdf_btn.clicked.connect(self.convert_to_pdf)
        self.ui.exit_btn.clicked.connect(self.close)
        self.ui.search_btn.clicked.connect(self.search_messages)

        # Carregar log inicial
        self.update_log_table()

    def update_log_table(self):
        log_entries = self.db.get_log_entries()
        self.ui.log_table.setRowCount(len(log_entries))
        for i, entry in enumerate(log_entries):
            for j, value in enumerate(entry):
                self.ui.log_table.setItem(i, j, QTableWidgetItem(str(value)))

    def search_messages(self):
        search_text = self.ui.search_input.text()
        # Implementar busca no banco
        # Atualizar result_table com os resultados

    def select_folder_or_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Selecionar arquivo JSON", "", "JSON Files (*.json);;All Files (*)")
        if not path:
            path = QFileDialog.getExistingDirectory(self, "Selecionar pasta")
        if not path:
            return

        self.ui.file_list.clear()
        self.current_folder = None
        self.current_file = None
        self.current_json_data = None
        self.ui.content_view.clear()

        if os.path.isdir(path):
            self.current_folder = path
            files = [f for f in os.listdir(path) if f.lower().endswith('.json')]
            for f in files:
                self.ui.file_list.addItem(f)
        elif os.path.isfile(path) and path.lower().endswith('.json'):
            self.current_folder = os.path.dirname(path)
            # filename = os.path.basename(path)
            # self.ui.file_list.addItem(filename)
            self.ui.file_list.addItem(path)  # Exibe o caminho completo
            # Seleciona e exibe automaticamente o arquivo
            self.ui.file_list.setCurrentRow(0)
            self.display_file_content(self.ui.file_list.item(0))
        else:
            QMessageBox.warning(self, "Aviso", "Selecione um arquivo ou pasta válida.")

    def display_file_content(self, item):
        # filename = item.text()
        # full_path = os.path.join(self.current_folder, filename)
        full_path = item.text()  # Agora o item já contém o caminho completo
        self.current_file = full_path
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                data = f.read()
                self.ui.content_view.setPlainText(data)
                try:
                    self.current_json_data = json.loads(data)
                except Exception:
                    self.current_json_data = data
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao abrir o arquivo:\n{e}")

    def get_suggested_name(self, ext):
        if not self.current_file or not self.current_folder:
            return ""
        folder_name = os.path.basename(self.current_folder.rstrip(os.sep))
        file_name = os.path.splitext(os.path.basename(self.current_file))[0]
        return f"{folder_name}_{file_name}{ext}"

    def save_and_show(self, content, file_filter, ext, suggested_name=""):
        # Seleciona a pasta de destino
        dest_dir = QFileDialog.getExistingDirectory(self, "Selecionar pasta para exportação")
        if not dest_dir:
            return

        # Nome da subpasta = nome da pasta onde está o JSON original
        if not self.current_file or not self.current_folder:
            QMessageBox.warning(self, "Aviso", "Arquivo de origem não definido.")
            return
        subfolder_name = os.path.basename(self.current_folder.rstrip(os.sep))
        export_folder = os.path.join(dest_dir, subfolder_name)
        os.makedirs(export_folder, exist_ok=True)

        # Nome do arquivo exportado
        file_name = os.path.splitext(os.path.basename(self.current_file))[0] + ext
        export_path = os.path.join(export_folder, file_name)

        # Salva o arquivo exportado
        try:
            with open(export_path, 'w', encoding='utf-8') as f:
                f.write(content)
            # Log da exportação
            self.db.log_export(export_path, ext.replace('.', ''))
            self.update_log_table()
            # Salvar mensagens no banco
            if self.current_json_data:
                channel_id = os.path.basename(self.current_folder)
                self.db.save_messages(channel_id, self.current_json_data)
            QMessageBox.information(self, "Sucesso", f"Arquivos salvos em:\n{export_folder}")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao salvar arquivo:\n{e}")

        # Copia o JSON original com sufixo _EXTRAIDO
        try:
            json_copy_name = os.path.splitext(os.path.basename(self.current_file))[0] + "_EXTRAIDO.json"
            json_copy_path = os.path.join(export_folder, json_copy_name)
            shutil.copy2(self.current_file, json_copy_path)
        except Exception as e:
            QMessageBox.warning(self, "Aviso", f"Arquivo exportado salvo, mas não foi possível copiar o JSON original:\n{e}")

    def convert_to_html(self):
        if self.current_json_data is None:
            QMessageBox.warning(self, "Aviso", "Nenhum arquivo carregado.")
            return
        html = json_to_html(self.current_json_data)
        suggested = self.get_suggested_name(".html")
        self.save_and_show(html, "HTML Files (*.html)", ".html", suggested)

    def convert_to_md(self):
        if self.current_json_data is None:
            QMessageBox.warning(self, "Aviso", "Nenhum arquivo carregado.")
            return
        md = json_to_md(self.current_json_data)
        suggested = self.get_suggested_name(".md")
        self.save_and_show(md, "Markdown Files (*.md)", ".md", suggested)

    def convert_to_pdf(self):
        if self.current_json_data is None:
            QMessageBox.warning(self, "Aviso", "Nenhum arquivo carregado.")
            return
        # Seleciona a pasta de destino
        dest_dir = QFileDialog.getExistingDirectory(self, "Selecionar pasta para exportação")
        if not dest_dir:
            return
        subfolder_name = os.path.basename(self.current_folder.rstrip(os.sep))
        export_folder = os.path.join(dest_dir, subfolder_name)
        os.makedirs(export_folder, exist_ok=True)
        file_name = os.path.splitext(os.path.basename(self.current_file))[0] + ".pdf"
        export_path = os.path.join(export_folder, file_name)
        try:
            json_to_pdf(self.current_json_data, export_path)
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao salvar PDF:\n{e}")
            return
        # Copia o JSON original com sufixo _EXTRAIDO
        try:
            json_copy_name = os.path.splitext(os.path.basename(self.current_file))[0] + "_EXTRAIDO.json"
            json_copy_path = os.path.join(export_folder, json_copy_name)
            shutil.copy2(self.current_file, json_copy_path)
        except Exception as e:
            QMessageBox.warning(self, "Aviso", f"PDF salvo, mas não foi possível copiar o JSON original:\n{e}")
        QMessageBox.information(self, "Sucesso", f"Arquivos salvos em:\n{export_folder}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())