from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QScrollArea, QApplication, QPushButton, QMessageBox
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont

import calculates
from calculates import data

class LBRM(QWidget):

    def __init__(self, arguments):
        super().__init__()

        self.arguments = arguments

        self.timer = None
        self.layout = None
        self.buttons_data = {}

        self.old_data = {}

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
        container.setLayout(self.layout)

        self.update_data()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_data)
        self.timer.start(500)

        self.show()

    def update_data(self):
        calculates.calculate(self.arguments)
        if data == self.old_data:
            return
        self.old_data = data.copy()

        while self.layout.count():
            item = self.layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        for category, items in data.items():
            button_title = QPushButton(f"{category}", self)
            button_title.setFont(QFont("Inria Sans", 20))
            button_title.setStyleSheet("""
                font-size: 20px;
                font-family: 'Inria Sans';
                color: #ffffff;
                margin-bottom: 5px;
                text-align: left;
                padding: 5px;
            """)

            self.layout.addWidget(button_title)
            if category not in self.buttons_data:
                self.buttons_data[category] = False
            button_title.clicked.connect(lambda _, cat=category: self.change_button_data(cat))
            if self.buttons_data[category]:
                for item in items:
                    for subcategory, values in item.items():
                        values_cleaned = ", ".join(str(v) for v in values if v is not None)
                        label_item = QLabel(f"{subcategory if subcategory else 'Unnamed'}: {values_cleaned}", self)
                        label_item.setFont(QFont("Inria Sans", 18))
                        label_item.setAlignment(Qt.AlignmentFlag.AlignLeft)
                        label_item.setStyleSheet("""
                                font-size: 18px;
                                font-family: 'Inria Sans';
                                color: #cccccc;
                                padding-left: 20px;
                                margin-bottom: 5px;
                                """)
                        self.layout.addWidget(label_item)
    def change_button_data(self, category):
        if self.buttons_data[category]:
            self.buttons_data[category] = False
        elif not self.buttons_data[category]:
            self.buttons_data[category] = True
        if (len(self.arguments) >= 3 and self.arguments[2] == '1') or (len(self.arguments) >= 1 and self.arguments[1] == '1'): print(f"BUTTONS_DATA :: {category} : {self.buttons_data[category]}")