import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
import menu_controller


class TMainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        """

        :return:
        """
        ok_button = QPushButton("OK")
        cancel_button = QPushButton("Cancel")
        v_box = QHBoxLayout()
        v_box.addStretch()
        v_box.addWidget(ok_button)
        v_box.addWidget(cancel_button)
        self.setGeometry(300, 300, 300, 300)
        self.setLayout(v_box)
        self.show()


app = QApplication(sys.argv)

window = TMainWindow()

sys.exit(app.exec_())
