import os
from PyQt5.QtGui import QIcon

def get_element_color(category):
    """ Retorna a cor correspondente à categoria do elemento químico """
    colors = {
        "Metal alcalino": "#FFEB3B",
        "Metal alcalino-terroso": "#FFC107",
        "Gás nobre": "#64B5F6",
        "Metaloide": "#A5D6A7",
        "Halogênio": "#FF7043",
        "Não-metal": "#7CA67E",
        "Metal de transição": "#90A4AE",
        "Metal": "#A7C9F9",
        "Lantanídeos": "#9F0081",
        "Actinídios": "#FE60C4"
    }
    return colors.get(category, "#FFFFFF")  # Retorna branco se não encontrar a categoria

def set_icon(window, icon_path="assets/favicon.ico"):
    """ Define o ícone da janela """
    if os.path.exists(icon_path):
        window.setWindowIcon(QIcon(icon_path))
