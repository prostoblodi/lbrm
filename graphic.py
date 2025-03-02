from PyQt6.QtWidgets import QWidget, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

import calculates
from calculates import data

class LBRM(QWidget):

    def __init__(self):
        super().__init__()
        self.y = 0
        self.label_titles = []
        self.label_title = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("LBRM.py")
        self.setFixedSize(800, 500)
        self.setStyleSheet("background-color: #000000; color: #ffffff;")

        calculates.calculate()

        for n in data:
            self.label_title = QLabel(f"{n}", self)
            self.label_title.setFont(QFont("Inria Sans", 20))
            self.label_title.setAlignment(Qt.AlignmentFlag.AlignLeft)
            self.label_title.setGeometry(0, self.y, 800, 40)
            self.y += 40
            self.label_titles.append(self.label_title)


        self.show()