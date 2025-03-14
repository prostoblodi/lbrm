import sys
from PyQt6.QtWidgets import QApplication
from graphic import LBRM

if __name__ == "__main__":
    app = QApplication(sys.argv)
    arguments = sys.argv
    print(f"Г Started with argumnets: {arguments}\n"
          f"| All debug mode: {True if len(arguments) >= 2 and arguments[1] == '1' else False};\n"
          f"| Graphics debug mode: {True if len(arguments) >= 3 and arguments[2] == '1' else False};\n"
          f"L Calculates debug mode: {True if len(arguments) >= 4 and arguments[3] == '1' else False}.")
    window = LBRM(arguments)
    window.show()
    sys.exit(app.exec())