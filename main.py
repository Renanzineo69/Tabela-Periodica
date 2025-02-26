import sys
from PyQt5.QtWidgets import QApplication
from ui.table import PeriodicTable
from logic.utils import set_icon

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PeriodicTable()
    set_icon(window)
    window.show()
    sys.exit(app.exec_())
