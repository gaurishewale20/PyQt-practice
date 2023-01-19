import sys

from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QStatusBar, QToolBar

class Window(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("QMain Window")
        self.setCentralWidget(QLabel("I'm the Central Widget"))
        self._createMenu()
        self._createToolBar()
        self._createStatusBar()

    def _createMenu(self):
        menu = self.menuBar()
        menu.addMenu("&Menu")
        menu.addMenu("&File")
        menu.addMenu("&Edit")
        menu.addMenu("&View")
        menu.addAction("&Exit",self.close)

    def _createToolBar(self):
        tools = QToolBar()
        tools.addAction("Exit",self.close)
        self.addToolBar(tools)

    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("I m the Status Bar and I am invincible")
        self.setStatusBar(status)

if __name__ =="__main__":
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())
