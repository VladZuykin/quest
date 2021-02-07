from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.QtWidgets import QTableWidgetItem, QDoubleSpinBox, QAbstractSpinBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
import sys
from PyQt5 import uic


class QuestWindow(QMainWindow):
    STATION_NAMES = ["«Кама-река»", "«Счастье не за горами»", "«Пермяк - солёные уши»",
                     "«Легенда о пермском медведе»",
                     "«Трус, Балбес и Бывалый»", "«Водопроводчик»", "«Эйфелева Башня»"]
    ASSOCIATIONS = ["кам", "счасть", "пермяк", "медвед", "трус", "водопровод", "эйфел"]

    def __init__(self):
        super().__init__()
        uic.loadUi("QuestMainWindow.ui", self)

        self.opened_cells_rows = set()
        self.init_ui()
        self.station = None

    def init_ui(self):
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)

        for i in range(7):
            item = QTableWidgetItem("")
            item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.tableWidget.setItem(i, 1, item)

        self.tableWidget.cellChanged.connect(self.check_and_edit)
        self.goButton.clicked.connect(self.choose_station)

    def check_and_edit(self, row, col):
        if col == 0 and row not in self.opened_cells_rows:
            association = self.ASSOCIATIONS[row]
            cell_text = self.tableWidget.item(row, col).text()
            if association in cell_text.lower():
                item = QTableWidgetItem(self.STATION_NAMES[row])
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                item.setBackground(QColor(10, 255, 10, 50))
                self.opened_cells_rows.add(row)
                self.tableWidget.setItem(row, col, item)

    def choose_station(self):
        row = self.tableWidget.currentRow()
        if self.tableWidget.currentColumn() == 0 and \
                row in self.opened_cells_rows and \
                self.tableWidget.selectedItems() and\
                self.tableWidget.item(row, 1).text() == "":
            if row == 0:
                self.station = FirstStation(self)
                self.station.show()
            elif row == 1:
                self.station = SecondStation(self)
                self.station.show()
            elif row == 2:
                self.station = ThirdStation(self)
                self.station.show()
            elif row == 3:
                self.station = FourthStation(self)
                self.station.show()
            elif row == 4:
                self.station = FifthStation(self)
                self.station.show()
            elif row == 5:
                self.station = SixthStation(self)
                self.station.show()
            elif row == 6:
                self.station = SeventhStation(self)
                self.station.show()


class FirstStation(QMainWindow):
    def __init__(self, parent):
        super().__init__()
        uic.loadUi("FirstTaskWindow.ui", self)
        self.parent = parent
        self.answerButton.clicked.connect(self.check_answer)

    def check_answer(self):
        mark = 0
        if self.firstAnswerSpinBox.value() == 1713:
            mark += 1
        if self.secondAnswerSpinBox.value() == 3:
            mark += 1

        item = QTableWidgetItem(str(mark))
        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        item.setBackground(QColor(10, 255, 10, 50))
        self.parent.tableWidget.setItem(0, 1, item)
        self.close()


class SecondStation(QMainWindow):
    ANSWERS = ("м", "а", "т", "р", "о", "c", "о", "в")

    def __init__(self, parent):
        super().__init__()
        uic.loadUi("SecondTaskWindow.ui", self)
        self.parent = parent
        self.answerButton.clicked.connect(self.check_answer)

    def check_answer(self):
        mark = 0
        for i in range(8):
            if self.tableWidget.item(1, i).text().lower() == self.ANSWERS[i]:
                mark += 1

        item = QTableWidgetItem(str(mark))
        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        item.setBackground(QColor(10, 255, 10, 50))
        self.parent.tableWidget.setItem(1, 1, item)
        self.close()


class ThirdStation(QMainWindow):
    def __init__(self, parent):
        super().__init__()
        uic.loadUi("ThirdTaskWindow.ui", self)
        self.parent = parent
        self.answerButton.clicked.connect(self.check_answer)

    def check_answer(self):
        mark = 0
        if self.spinBox.value() == 60:
            mark = 1

        item = QTableWidgetItem(str(mark))
        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        item.setBackground(QColor(10, 255, 10, 50))
        self.parent.tableWidget.setItem(2, 1, item)
        self.close()


class FourthStation(QMainWindow):
    def __init__(self, parent):
        super().__init__()
        uic.loadUi("FourthTaskWindow.ui", self)
        self.parent = parent
        self.answerButton.clicked.connect(self.check_answer)

    def check_answer(self):
        mark = 0
        if self.doubleSpinBox.value() == 2.5:
            mark = 1

        item = QTableWidgetItem(str(mark))
        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        item.setBackground(QColor(10, 255, 10, 50))
        self.parent.tableWidget.setItem(3, 1, item)
        self.close()


class FifthStation(QMainWindow):
    def __init__(self, parent):
        super().__init__()
        uic.loadUi("FifthTaskWindow.ui", self)
        self.parent = parent
        self.answerButton.clicked.connect(self.check_answer)

    def check_answer(self):
        mark = 0
        if self.spinBox.value() == 35:
            mark += 1
        if self.spinBox_1.value() == 955:
            mark += 1

        item = QTableWidgetItem(str(mark))
        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        item.setBackground(QColor(10, 255, 10, 50))
        self.parent.tableWidget.setItem(4, 1, item)
        self.close()


class SixthStation(QMainWindow):
    def __init__(self, parent):
        super().__init__()
        uic.loadUi("SixthTaskWindow.ui", self)
        self.parent = parent
        self.answerButton.clicked.connect(self.check_answer)

    def check_answer(self):
        mark = 0
        if self.spinBox.value() == 1886:
            mark += 1
        if self.spinBox_1.value() == 1:
            mark += 1
        if self.spinBox_2.value() == 40:
            mark += 1

        item = QTableWidgetItem(str(mark))
        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        item.setBackground(QColor(10, 255, 10, 50))
        self.parent.tableWidget.setItem(5, 1, item)
        self.close()


class SeventhStation(QMainWindow):
    ANSWERS = ((10, 11), (9, 10), (5, 6), (3, 4), (3, 4), (1, 2), (4, 5))

    def __init__(self, parent):
        super().__init__()
        uic.loadUi("SeventhTaskWindow.ui", self)
        self.parent = parent
        self.init_ui()
        self.answerButton.clicked.connect(self.check_answer)

    def check_answer(self):
        mark = 0
        for num, spin_box in enumerate(self.spin_boxes):
            if self.ANSWERS[num][0] <= spin_box.value() <= self.ANSWERS[num][1]:
                mark += 1
        item = QTableWidgetItem(str(mark))
        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        item.setBackground(QColor(10, 255, 10, 50))
        self.parent.tableWidget.setItem(6, 1, item)
        self.close()

    def init_ui(self):
        eifel_pixmap = QPixmap("img/EifelTower.png")
        self.eifel_label = QLabel(self)
        self.eifel_label.setGeometry(100, 200, 400, 500)
        self.eifel_label.setPixmap(eifel_pixmap)

        perm_pixmap = QPixmap("img/PermTower.png")
        self.perm_label = QLabel(self)
        self.perm_label.setGeometry(600, 200, 400, 500)
        self.perm_label.setPixmap(perm_pixmap)

        spin_boxes_coords = ((768, 248), (875, 410), (770, 457), (770, 531), (835, 531),
                             (790, 579), (692, 668))

        self.spin_boxes = []
        for x, y in spin_boxes_coords:
            spin_box = QDoubleSpinBox(self)
            spin_box.setRange(0, 300)
            spin_box.setButtonSymbols(QAbstractSpinBox.NoButtons)
            spin_box.setGeometry(x, y, 30, 18)
            spin_box.setFrame(False)
            self.spin_boxes.append(spin_box)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QuestWindow()
    window.show()

    sys.exit(app.exec())
