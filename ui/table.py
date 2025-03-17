from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QDesktopWidget
from logic.data_loader import load_data
from logic.utils import get_element_color, get_hover_color
from ui.details import ElementDetails

class PeriodicTable(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Tabela Periódica")
        self.setGeometry(100, 100, 900, 500)
        self.center_window()  # 🔹 Centraliza a janela ao iniciar
        self.setStyleSheet("background-color: #2b2b2b;")
        layout = QGridLayout()

        elements_data = load_data()
        column_position = 4  # Para os Lantanídeos e Actinídeos

        for element_id, element in elements_data.items():
            period = int(element["period"])
            group = int(element["group"])

            # Lantanídeos e Actinídeos
            if 57 <= element["atomic_number"] <= 71:
                row, column = 9, column_position
                column_position += 1
            elif 89 <= element["atomic_number"] <= 103:
                row, column = 10, column_position - 15
                column_position += 1
            else:
                row, column = period, group

            button = QPushButton(element["symbol"])
            button.setStyleSheet(f"""
                QPushButton {{
                    background-color: {get_element_color(element['category'])}; 
                    font-size: 14px; 
                    font-weight: bold;
                    width: 45px; 
                    height: 45px;
                    border-radius: 5px;
                }}
                QPushButton:hover {{
                    background-color: {get_hover_color(get_element_color(element['category']))};  /* Tom mais baixo */
                }}
            """)
        
            button.clicked.connect(lambda _, e=element: self.show_details(e))
            layout.addWidget(button, row, column)

        self.setLayout(layout)

    def show_details(self, element):
        """ Exibe a janela de detalhes ao clicar em um elemento """
        self.details_window = ElementDetails(element)
        self.details_window.show()

    def center_window(self):
        """ 🔹 Centraliza a janela na tela """
        screen_geometry = QDesktopWidget().screenGeometry()
        window_geometry = self.frameGeometry()
        center_point = screen_geometry.center()
        window_geometry.moveCenter(center_point)
        self.move(window_geometry.topLeft())
