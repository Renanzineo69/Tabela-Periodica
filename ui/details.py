from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QDesktopWidget, QFrame, QTextEdit
from PyQt5.QtCore import Qt
from logic.utils import get_element_color, set_icon  # 🔹 Importando a função set_icon

class ElementDetails(QWidget):
    def __init__(self, element):
        super().__init__()
        self.element = element
        self.initUI()

    def initUI(self):
        self.setWindowTitle(f"{self.element['name']}")
        self.setFixedSize(350, 360)  # 🔹 Mantém um tamanho menor para parecer um card
        self.center_window()  # 🔹 Agora aparece centralizada
        set_icon(self)  # 🔹 Define o ícone correto

        self.setStyleSheet("""
            background-color: #2C2F33; 
            color: white; 
            border-radius: 12px; 
            padding: 10px;
        """)

        layout = QVBoxLayout()
        
        # 🔹 Cabeçalho estilizado
        header_label = QLabel(f"{self.element['name']} ({self.element['symbol']})")
        header_label.setStyleSheet(f"""
            background-color: {get_element_color(self.element['category'])};
            color: black; 
            font-size: 16px; 
            font-weight: bold; 
            padding: 8px;
            border-radius: 8px;
            text-align: center;
        """)
        header_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(header_label)

        # 🔹 Informações do elemento
        details = [
            f"Número Atômico: {self.element['atomic_number']}",
            f"Massa Atômica: {self.element['atomic_mass']}",
            f"Grupo: {self.element['group']}",
            f"Período: {self.element['period']}",
            f"Categoria: {self.element['category']}"
        ]

        for detail in details:
            label = QLabel(detail)
            label.setStyleSheet("""
                padding: 4px; 
                font-size: 12px; 
                background-color: #23272A; 
                border-radius: 5px;
                margin-bottom: 5px;
            """)
            label.setAlignment(Qt.AlignCenter)
            layout.addWidget(label)

        # 🔹 Caixa de texto com barra de rolagem estilizada
        description_text = QTextEdit()
        description_text.setText(f"Descrição:\n{self.element['description']}")
        description_text.setReadOnly(True)
        description_text.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        description_text.setStyleSheet("""
            QTextEdit {
                font-size: 11px; 
                padding: 6px; 
                background-color: #23272A; 
                border-radius: 5px;
                color: white;
                border: none;
                min-height: 60px;
                max-height: 100px;
            }
            QScrollBar:vertical {
                border: none;
                background: #2C2F33;
                width: 8px;
                margin: 3px 0 3px 0;
                border-radius: 4px;
            }
            QScrollBar::handle:vertical {
                background: #7289DA;
                min-height: 20px;
                border-radius: 4px;
            }
            QScrollBar::handle:vertical:hover {
                background: #5865F2;
            }
            QScrollBar::add-line:vertical, 
            QScrollBar::sub-line:vertical {
                background: none;
                height: 0px;
            }
        """)
        layout.addWidget(description_text)

        # 🔹 Linha divisória
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setStyleSheet("background-color: #7289DA; height: 1px;")
        layout.addWidget(line)

        # 🔹 Botão estilizado para fechar
        close_button = QPushButton("Fechar")
        close_button.setStyleSheet("""
            QPushButton {
                background-color: #7289DA; 
                color: white; 
                font-size: 13px; 
                font-weight: bold;
                padding: 6px; 
                border-radius: 6px;
                margin-top: 5px;
            }
            QPushButton:hover {
                background-color: #5b6eae;
            }
        """)
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)

        self.setLayout(layout)

    def center_window(self):
        """ 🔹 Centraliza a janela de detalhes na tela """
        screen_geometry = QDesktopWidget().screenGeometry()
        window_geometry = self.frameGeometry()
        center_point = screen_geometry.center()
        window_geometry.moveCenter(center_point)
        self.move(window_geometry.topLeft())
