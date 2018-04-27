import sys
from PyQt5.QtWidgets import QApplication, QWidget

import menu_controller

app = QApplication(sys.argv)

main_window = QWidget()
menu_controller.main_menu_create(main_window)

main_window.setGeometry(300, 300, 300, 200)
main_window.setWindowTitle('Tooltips 2')
main_window.show()


sys.exit(app.exec_())
