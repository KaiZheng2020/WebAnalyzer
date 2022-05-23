# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TableForm.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl,
                          Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QGradient, QIcon, QImage,
                         QKeySequence, QLinearGradient, QPainter, QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt5.QtWidgets import (QApplication, QGridLayout, QHeaderView, QSizePolicy, QTableView, QWidget)


class Ui_TableForm(object):
    def setupUi(self, TableForm):
        if not TableForm.objectName():
            TableForm.setObjectName(u"TableForm")
        TableForm.resize(400, 300)
        self.gridLayout = QGridLayout(TableForm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableView = QTableView(TableForm)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setSortingEnabled(True)

        self.gridLayout.addWidget(self.tableView, 0, 0, 1, 1)

        self.retranslateUi(TableForm)

        QMetaObject.connectSlotsByName(TableForm)

    # setupUi

    def retranslateUi(self, TableForm):
        TableForm.setWindowTitle(QCoreApplication.translate("TableForm", u"Form", None))

    # retranslateUi
