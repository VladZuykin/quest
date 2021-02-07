from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from PyQt5 import uic


class QuestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("QuestMainWindow.ui", self)
        self.change_sizes()

    def change_sizes(self):
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QuestWindow()
    window.show()
    sys.exit(app.exec())
