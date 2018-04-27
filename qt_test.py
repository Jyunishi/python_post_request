import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)

window = QWidget()

window.resize(200, 200)
window.move(100, 100)
window.setWindowTitle('Title')
window.show()

sys.exit(app.exec_())


