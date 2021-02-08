from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.QtWidgets import QTableWidgetItem, QDoubleSpinBox, QAbstractSpinBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QColor
import sys
from PyQt5 import uic


def set_item(parent, element, row, col=1):
    item = QTableWidgetItem(str(element))
    item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
    item.setBackground(parent.CELL_COLOR)
    parent.tableWidget.setItem(row, col, item)
    parent.stations_last -= 1
    parent.set_pixmap(row)
    if parent.stations_last > 0:
        parent.statusBar().showMessage(f"Добавлена часть картинки, осталось {parent.stations_last}.", 5000)
    else:
        parent.statusBar().showMessage("Вы собрали все части картинки.", 5000)


class QuestWindow(QMainWindow):
    CELL_COLOR = QColor(10, 255, 10, 50)

    STATION_NAMES = ("«Кама-река»", "«Счастье не за горами»", "«Пермяк - солёные уши»",
                     "«Легенда о пермском медведе»",
                     "«Трус, Балбес и Бывалый»", "«Водопроводчик»", "«Эйфелева Башня»")
    ASSOCIATIONS = (("кам", ), ("счасть",), ("пермяк", "сол"), ("медвед", "мишк"),
                    ("трус", "балбес", "бывалый"), ("водопровод",), ("эйфел",))

    def __init__(self):
        super().__init__()
        uic.loadUi("QuestMainWindow.ui", self)

        self.opened_cells_rows = set()
        self.station = None
        self.stations_last = 7
        self.last_mark = 0

        self.res_pixmap = QPixmap("img/ClockPainting.png")

        self.LABELS = (self.label_1, self.label_2, self.label_3, self.label_4,
                       self.label_5, self.label_6, self.label_7,)
        self.STATIONS = (FirstStation, SecondStation, ThirdStation, FourthStation,
                         FifthStation, SixthStation, SeventhStation)

        title_size = self.res_pixmap.width() // 3, self.res_pixmap.height() // 3
        self.RECTS = ((0, 0, *title_size),
                      (title_size[0], 0, *title_size),
                      (title_size[0] * 2, 0,  *title_size),
                      (0, title_size[1], *title_size),
                      (title_size[0], title_size[1], *title_size),
                      (title_size[0] * 2, title_size[1], *title_size),
                      (0, title_size[1] * 2, title_size[0] * 3, title_size[1]))

        self.init_ui()

    def init_ui(self):
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)

        for i in range(7):
            item = QTableWidgetItem("")
            item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.tableWidget.setItem(i, 1, item)

        for label in self.LABELS:
            label.setScaledContents(True)

        self.answerLabel.hide()
        self.answerLineEdit.hide()
        self.answerButton.hide()
        self.questionTextBrowser.hide()

        self.tableWidget.cellChanged.connect(self.check_and_edit)
        self.goButton.clicked.connect(self.choose_station)
        self.answerButton.clicked.connect(self.last_question_processing)

    def check_and_edit(self, row, col):
        if col == 0 and row not in self.opened_cells_rows:
            association = self.ASSOCIATIONS[row]
            cell_text = self.tableWidget.item(row, col).text()
            if any(map(lambda x: x in cell_text.lower(), association)):
                item = QTableWidgetItem(self.STATION_NAMES[row])
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                item.setBackground(self.CELL_COLOR)
                self.opened_cells_rows.add(row)
                self.tableWidget.setItem(row, col, item)

    def set_pixmap(self, row):
        pixmap = self.res_pixmap.copy(*self.RECTS[row])
        self.LABELS[row].setPixmap(pixmap)
        self.label.setText(f"Соберите всю картинку, проходя станции (осталось {self.stations_last})")
        if not self.stations_last:
            self.goButton.hide()
            self.tabWidget.setTabText(1, "Итоговое задание")
            self.answerLabel.show()
            self.answerLineEdit.show()
            self.answerButton.show()
            self.questionTextBrowser.show()
            self.label.hide()
            self.label_8.hide()

    def choose_station(self):
        row = self.tableWidget.currentRow()
        if self.tableWidget.currentColumn() == 0 and \
                row in self.opened_cells_rows and \
                self.tableWidget.selectedItems() and\
                self.tableWidget.item(row, 1).text() == "":

                self.station = self.STATIONS[row](self)
                self.station.show()

    def last_question_processing(self):
        answer = self.answerLineEdit.text().lower()
        three_hundred_str = {"трехсот", "трёхсот", "300", "тремста",
                             "трёмста"}
        if "часы" in answer and \
                any(map(lambda word: word in answer, three_hundred_str)):
            self.last_mark = 1
            self.answerLineEdit.setText("«Часы обратного отсчета до 300-летия г.Перми»")

        res_table_mark = sum([int(self.tableWidget.item(row, 1).text()) for row in range(7)])
        self.last_window = ResultWindow(self.last_mark + res_table_mark)
        self.last_window.show()
        self.close()


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
        set_item(self.parent, mark, 0)
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
            if self.tableWidget.item(1, i) and\
                    self.tableWidget.item(1, i).text().lower() == self.ANSWERS[i]:
                mark += 1
        set_item(self.parent, mark, 1)
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

        set_item(self.parent, mark, 2)
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

        set_item(self.parent, mark, 3)
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

        set_item(self.parent, mark, 4)
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
        if self.spinBox_1.value() == 1 and self.spinBox_2.value() == 40:
            mark += 1

        set_item(self.parent, mark, 5)
        self.close()


class SeventhStation(QMainWindow):
    ANSWERS = ((10, 11), (9, 10), (5, 6), (3, 4), (3, 4), (1, 2), (4, 5))

    def __init__(self, parent):
        super().__init__()
        uic.loadUi("SeventhTaskWindow.ui", self)
        self.parent = parent
        self.init_ui()
        self.answerButton.clicked.connect(self.check_answer)

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

    def check_answer(self):
        mark = 0
        for num, spin_box in enumerate(self.spin_boxes):
            if self.ANSWERS[num][0] <= spin_box.value() <= self.ANSWERS[num][1]:
                mark += 1
        set_item(self.parent, mark, 6)
        self.close()


class ResultWindow(QMainWindow):
    def __init__(self, result):
        super().__init__()
        uic.loadUi("LastWindow.ui", self)
        self.result = result
        self.init_ui()

    def init_ui(self):
        pixmap = QPixmap("img/ClockImage.png")
        self.imageLabel.setPixmap(pixmap)

        self.resultLabel.setText(f"Поздравляем! Ваш итоговый балл равен {self.result}!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QuestWindow()
    window.show()

    sys.exit(app.exec())
