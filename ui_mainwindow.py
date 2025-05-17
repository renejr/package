from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QPushButton, QFileDialog, QListWidget, QTextEdit,
    QTabWidget, QLabel, QLineEdit, QTableWidget, 
    QTableWidgetItem, QHeaderView
)

class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("Conversor de JSON para HTML/MD/PDF")
        MainWindow.resize(800, 600)
        self.central_widget = QWidget()
        MainWindow.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Criar TabWidget
        self.tab_widget = QTabWidget()
        self.layout.addWidget(self.tab_widget)

        # Tab 1 - Conversão
        self.tab_convert = QWidget()
        self.tab_widget.addTab(self.tab_convert, "Conversão")
        self.convert_layout = QVBoxLayout(self.tab_convert)

        self.select_btn = QPushButton("Selecionar Pasta ou Arquivo")
        self.convert_layout.addWidget(self.select_btn)

        self.file_list = QListWidget()
        self.convert_layout.addWidget(self.file_list)

        self.content_view = QTextEdit()
        self.content_view.setReadOnly(True)
        self.convert_layout.addWidget(self.content_view)

        # Botões de conversão
        self.btn_layout = QHBoxLayout()
        self.html_btn = QPushButton("Converter para HTML")
        self.md_btn = QPushButton("Converter para Markdown")
        self.pdf_btn = QPushButton("Converter para PDF")
        self.exit_btn = QPushButton("Sair")
        self.btn_layout.addWidget(self.html_btn)
        self.btn_layout.addWidget(self.md_btn)
        self.btn_layout.addWidget(self.pdf_btn)
        self.btn_layout.addWidget(self.exit_btn)
        self.convert_layout.addLayout(self.btn_layout)

        # Tab 2 - Consulta
        self.tab_query = QWidget()
        self.tab_widget.addTab(self.tab_query, "Consulta")
        self.query_layout = QVBoxLayout(self.tab_query)

        # Área de pesquisa
        self.search_layout = QHBoxLayout()
        self.search_label = QLabel("Pesquisar:")
        self.search_input = QLineEdit()
        self.search_btn = QPushButton("Buscar")
        self.search_layout.addWidget(self.search_label)
        self.search_layout.addWidget(self.search_input)
        self.search_layout.addWidget(self.search_btn)
        self.query_layout.addLayout(self.search_layout)

        # Tabela de resultados
        self.result_table = QTableWidget()
        self.result_table.setColumnCount(5)
        self.result_table.setHorizontalHeaderLabels([
            "Data/Hora", "Autor", "Conteúdo", "Canal", "IP"
        ])
        header = self.result_table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.query_layout.addWidget(self.result_table)

        # Log de exportação
        self.log_label = QLabel("Log de Exportação:")
        self.query_layout.addWidget(self.log_label)
        self.log_table = QTableWidget()
        self.log_table.setColumnCount(5)
        self.log_table.setHorizontalHeaderLabels([
            "Data/Hora", "ID Máquina", "IP", "Arquivo", "Tipo"
        ])
        header = self.log_table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.query_layout.addWidget(self.log_table)