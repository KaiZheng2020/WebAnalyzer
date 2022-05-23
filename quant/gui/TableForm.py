from PyQt5.QtCore import QDate, QObject, QSize, Signal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QFileDialog, QHeaderView, QWidget

from .resources import resources
from .widgets.TableForm import Ui_TableForm


class TableForm(QWidget, Ui_TableForm):
    def __init__(self):
        super().__init__()

        self.gui = Ui_TableForm()
        self.gui.setupUi(self)

        icon = QIcon()
        icon.addFile(u":/logo/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

        self.gui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
