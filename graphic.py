from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QScrollArea
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont

import calculates
from calculates import data

class LBRM(QWidget):

    def __init__(self):
        super().__init__()
        self.timer = None
        self.layout = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("LBRM.py")
        self.setFixedSize(800, 800)
        self.setStyleSheet("background-color: #000000; color: #ffffff;")

        container = QWidget(self)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        scroll_area.setWidget(container)

        main_layout = QVBoxLayout()
        main_layout.addWidget(scroll_area)

        self.setLayout(main_layout)

        self.layout = QVBoxLayout()

        self.update_data()

        container.setLayout(self.layout)

        self.show()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_data)
        self.timer.start(500)

    def update_data(self):
        for i in reversed(range(self.layout.count())):
            widget = self.layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        calculates.calculate()

        y = 0

        for n in data:
            label_title = QLabel(f"{n}", self)
            label_title.setFont(QFont("Inria Sans", 20))
            label_title.setAlignment(Qt.AlignmentFlag.AlignLeft)
            self.layout.addWidget(label_title)

            for l in data[n]:
                label_item = QLabel(f"{l}", self)
                label_item.setFont(QFont("Inria Sans", 20))
                label_item.setAlignment(Qt.AlignmentFlag.AlignLeft)
                label_item.setStyleSheet("padding-left: 20px; padding-top: 5px; margin: 5px;")
                self.layout.addWidget(label_item)

        self.update()

