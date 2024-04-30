import sys
from PyQt6.QtWidgets import *


class Form(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

    def get_directory(self):  # <-----
        return QFileDialog.getExistingDirectory(self, "Выбрать папку", ".")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Form()

    print(ex.get_directory())