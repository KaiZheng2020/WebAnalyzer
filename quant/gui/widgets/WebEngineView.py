from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView


class WebEngineView(QWebEngineView):
    def createWindow(self, type: QWebEnginePage.WebWindowType) -> 'QWebEngineView':
        return self
