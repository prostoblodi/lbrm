import sys
from PyQt6.QtWidgets import QApplication
from graphic import LBRM

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LBRM()
    window.show()
    sys.exit(app.exec())