import sys 
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("Screen1.ui",self)
        self.button1.clicked.connect(self.goToScreen2)

    def goToScreen2(self):
        screen2 = Screen2()
        widget.addWidget(screen2)
        widget.setCurrentWidget(screen2)

class Screen2(QMainWindow):
    def __init__(self):
        super(Screen2,self).__init__()
        loadUi("Screen2.ui",self)
        self.button1.clicked.connect(self.goToMainScreen)

    def goToMainScreen(self):
        widget.removeWidget(self)
        widget.setCurrentWidget(mainwindow)

# main
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
mainwindow = MainWindow()
widget.addWidget(mainwindow)
widget.setFixedHeight(600)
widget.setFixedWidth(800)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting due to error")
