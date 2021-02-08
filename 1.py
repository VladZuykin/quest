from main import ResultWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

app = QApplication(sys.argv)
window = ResultWindow(60)
window.show()
sys.exit(app.exec())
