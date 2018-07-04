import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout
from menu_controller import TMainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = TMainWindow()

    sys.exit(app.exec_())
