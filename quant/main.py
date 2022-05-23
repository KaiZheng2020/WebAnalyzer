import sys
from multiprocessing import freeze_support

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

from gui.MainForm import MainForm

if __name__ == '__main__':

    freeze_support()

    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon('./gui/resources/logo/logo.png'))

    main = MainForm()
    main.show()
    sys.exit(app.exec())
