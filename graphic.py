from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QFrame
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from calculates import labels, criticals, highs, names, currents

class LBRM(QWidget):
    def __init__(self):
        super().__init__()
        self.label_title = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("LBRM.py")
        self.setFixedSize(800, 500)
        self.setStyleSheet("background-color: #ffffff; color: #000000;")

        self.label_title = QLabel("Hello, world!", self)
        self.label_title.setFont(QFont("Inria Sans", 20))
        self.label_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_title.setGeometry(200, 40, 400, 40)

        self.show()