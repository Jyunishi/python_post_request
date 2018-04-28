# import sys
from PyQt5.QtWidgets import QPushButton, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QCoreApplication





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

        # vbox.addLayout(okButton, )


# def main_menu_create(hwnd):
#     """
#
#     :param hwnd:
#     :return:
#     """
#
#     btn = QPushButton('Button', hwnd)
#     btn.clicked.connect(refresh(btn, hwnd))
#     btn.setToolTip('This is a <b>QPushButton</b> widget')
#     # btn.resize(btn.sizeHint())
#     btn.move(50, 50)
#
#
# def refresh(self, hwnd):
#     """
#
#     :return:
#     """
#     # if hwnd is not None:
#     #     btn = QPushButton('Button', hwnd)
#     #     btn.setToolTip('This is a <b>QPushButton</b> widget 2')
#     #     btn.resize(btn.sizeHint())
#     #     btn.move(150, 150)
