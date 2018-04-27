# import sys
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QCoreApplication


def main_menu_create(hwnd):
    """

    :param hwnd:
    :return:
    """

    btn = QPushButton('Button', hwnd)
    btn.clicked.connect(refresh)
    btn.setToolTip('This is a <b>QPushButton</b> widget')
    # btn.resize(btn.sizeHint())
    btn.move(50, 50)


def refresh():
    """

    :return:
    """
    # if hwnd is not None:
    #     btn = QPushButton('Button', hwnd)
    #     btn.setToolTip('This is a <b>QPushButton</b> widget 2')
    #     btn.resize(btn.sizeHint())
    #     btn.move(150, 150)
