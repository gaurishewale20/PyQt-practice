# pycalc.py

"""PyCalc is a simple calculator built with Python and PyQt."""

import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

WINDOW_SIZE = 235

class CalcWindow(QMainWindow):
    """Calc's main window (GUI or view)."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyCalc")
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

def main():
    """Calc's main function."""
    calcApp = QApplication([])
    calcWindow = CalcWindow()
    calcWindow.show()
    sys.exit(calcApp.exec())

if __name__ == "__main__":
    main()