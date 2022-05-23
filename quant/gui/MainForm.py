import re
import sys
import threading
from concurrent.futures import thread

from loguru import logger
from PyQt5 import QtGui
from PyQt5.QtCore import QObject, QSize, QTimer, QUrl, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineCore import QWebEngineUrlRequestInterceptor
from PyQt5.QtWebEngineWidgets import (QWebEnginePage, QWebEngineProfile, QWebEngineView)
from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox, QWidget
from requests import head
from sqlalchemy import column

from .resources import resources
from .widgets.MainForm import Ui_MainForm

record_flag = False
filter = ''
lock = threading.Lock()


class RequestInterceptor(QWebEngineUrlRequestInterceptor):
    def interceptRequest(self, info):
        global record_flag, filter, lock
        lock.acquire()
        if record_flag:
            url = info.requestUrl().toString()
            if len(filter) > 0:
                if re.search(filter, url) != None:
                    logger.info(url)
            else:
                logger.info(url)
        lock.release()


class Stream(QObject):
    _log = pyqtSignal(str)

    def write(self, text):
        self._log.emit(str(text))

    def flush(self):
        QApplication.processEvents()


class MainForm(QWidget, Ui_MainForm):
    def __init__(self):
        super().__init__()

        self.gui = Ui_MainForm()
        self.gui.setupUi(self)

        icon = QIcon()
        icon.addFile(u":/logo/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

        self.gui.splitter_h.setStretchFactor(1, 20)
        self.gui.splitter_v.setStretchFactor(1, 20)

        # Log
        self.stream = Stream()
        self.stream._log.connect(self.log)

        sys.stdout = self.stream
        sys.stderr = self.stream

        logger.add(self.stream, format="{time:YYYY-MM-DD HH:mm:ss} {level} - {message}", level="INFO")

        self.gui.textEdit_Log.document().setMaximumBlockCount(4096)

        # Button
        self.gui.pushButton_OpenUrl.clicked.connect(self.open_url)
        self.gui.pushButton_DoAction.clicked.connect(self.do_action)
        self.gui.pushButton_Record_Start.clicked.connect(self.record_start)
        self.gui.pushButton_Record_Stop.clicked.connect(self.record_stop)
        self.gui.pushButton_ActionTimer_Start.clicked.connect(self.timer_start)
        self.gui.pushButton_ActionTimer_Stop.clicked.connect(self.timer_stop)

        QWebEngineProfile.defaultProfile().setRequestInterceptor(RequestInterceptor(self))
        self.gui.lineEdit_Url.setText('http://www.jd.com')

        self.timer = QTimer()
        self.timer.timeout.connect(self.do_action)

        logger.info('Welcome to use Web Analyzer.')

    def log(self, text):
        if '\r' in text:
            text = text.replace('\r', '').rstrip()
            cursor = self.gui.textEdit_Log.textCursor()
            # cursor.movePosition(QtGui.QTextCursor.End)
            cursor.select(QtGui.QTextCursor.BlockUnderCursor)
            cursor.removeSelectedText()
            cursor.insertBlock()
            self.gui.textEdit_Log.setTextCursor(cursor)

        self.gui.textEdit_Log.insertPlainText(text)
        self.gui.textEdit_Log.moveCursor(QtGui.QTextCursor.End)

    # Functions

    def open_url(self):

        try:
            url = QUrl(self.gui.lineEdit_Url.text())
            if url.scheme() == '':
                url.setScheme('http')

            self.gui.webEngineView.load(url)
        except Exception as err:
            logger.error(err)

    def record_start(self):

        try:
            lock.acquire()
            global record_flag, filter
            record_flag = True
            filter = self.gui.lineEdit_Filter.text()
            lock.release()
            logger.info('record start')
        except Exception as err:
            logger.error(err)

    def record_stop(self):

        try:
            lock.acquire()
            global record_flag
            record_flag = False
            lock.release()
            logger.info('record stop')
        except Exception as err:
            logger.error(err)

    def do_action(self):

        try:
            action = self.gui.lineEdit_Action.text()
            self.gui.webEngineView.load(QUrl(action))
            logger.info(f'do action: {action}')
        except Exception as err:
            logger.error(err)

    def timer_start(self):
        try:
            logger.info(f'timer start')
            time = self.gui.spinBox_ActionTime.value()
            self.timer.start(time)
        except Exception as err:
            logger.error(err)

    def timer_stop(self):
        try:
            logger.info(f'timer stop')
            self.timer.stop()
        except Exception as err:
            logger.error(err)
