import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn
from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg, NavigationToolbar2QT)
from matplotlib.figure import Figure
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QVBoxLayout, QWidget

from .resources import resources


class GraphForm(QWidget):
    def __init__(self, parent=None):
        super(GraphForm, self).__init__(parent)

        self.figure = plt.figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.toolbar = NavigationToolbar2QT(self.canvas, self)

        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)

        self.setLayout(layout)

        icon = QIcon()
        icon.addFile(u":/logo/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

    def plot(self, df):
        self.figure.clear()
        ax = self.figure.subplots()
        df.plot.line(ax=ax)
        self.canvas.draw()

    def plot_hist(self, df):
        self.figure.clear()
        self.ax = self.figure.add_subplot(111)
        df.hist(ax=self.ax)
        self.canvas.draw()
