# pycalc.py

"""PyCalc is a simple calculator built with Python and PyQt."""

import sys


from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLineEdit, QPushButton, QVBoxLayout
from functools import partial

WINDOW_SIZE = 235
DISPLAY_HEIGHT = 35
BUTTON_SIZE = 40
ERROR_MSG = "ERR"

class CalcWindow(QMainWindow):
    """Calc's main window (GUI or view)."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyCalc")
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)
        self._createDisplay()
        self._createButtons()

    def _createDisplay(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(DISPLAY_HEIGHT)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)

    def _createButtons(self):
        self.buttonsMap = {}
        buttonsLayout = QGridLayout()
        keyBoard = [
            ["7", "8", "9", "/", "C"],
            ["4", "5", "6", "*", "("],
            ["1", "2", "3", "-", ")"],
            ["0", "00", ".", "+", "="],
        ]

        for row, keys in enumerate(keyBoard):
            for col, key in enumerate(keys):
                self.buttonsMap[key] = QPushButton(key)
                self.buttonsMap[key].setFixedSize(BUTTON_SIZE, BUTTON_SIZE)
                buttonsLayout.addWidget(self.buttonsMap[key], row, col)

        self.generalLayout.addLayout(buttonsLayout)

    def setDisplayText(self, text):
        # Sets Display Text
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        # returns Display Text
        return self.display.text()

    def clearDisplayText(self):
        # clears Display Text
        self.setDisplayText("")

def evaluateExpression(expression):
    try:
        result = str(eval(expression,{},{}))
    except Exception:
        result = ERROR_MSG
    return result

# Controller Class

class CalcController:
    def __init__(self, model, view):
        self._evaluate = model
        self._view = view
        self._connectSignalsAndSlots()

    def calculateResult(self):
        result = self._evaluate(expression = self._view.displayText())
        self._view.setDisplayText(result)

    def buildExpression(self, subExpresion):
        if self._view.displayText() == ERROR_MSG:
            self._view.clearDisplayText()
        expression = self._view.displayText() + subExpresion
        self._view.setDisplayText(expression)

    def _connectSignalsAndSlots(self):
        for keySymbol, button in self._view.buttonsMap.items():
            if keySymbol not in {"=", "C"}:
                button.clicked.connect(partial(self.buildExpression, keySymbol))
        self._view.buttonsMap["="].clicked.connect(self.calculateResult)
        self._view.display.returnPressed.connect(self.calculateResult)
        self._view.buttonsMap["C"].clicked.connect(self._view.clearDisplayText)

def main():
    """Calc's main function."""
    calcApp = QApplication([])
    calcWindow = CalcWindow()
    calcWindow.show()
    CalcController(model=evaluateExpression, view = calcWindow)
    sys.exit(calcApp.exec())

if __name__ == "__main__":
    main()