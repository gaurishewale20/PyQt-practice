import sys

from PyQt6.QtWidgets import QApplication, QGridLayout, QWidget, QPushButton

app = QApplication([])

window = QWidget()
window.setWindowTitle("QGrid Layout")

layout = QGridLayout()
layout.addWidget(QPushButton("Button (0,0)"), 0,0)
layout.addWidget(QPushButton("Button (0,1)"), 0,1)
layout.addWidget(QPushButton("Button (0,2)"), 0,2)
layout.addWidget(QPushButton("Button (1,0)"), 1,0)
layout.addWidget(QPushButton("Button (1,1)"), 1,1)
layout.addWidget(QPushButton("Button (1,2)"), 1,2)
layout.addWidget(QPushButton("Button (2,0)"), 2,0)
layout.addWidget(QPushButton("Button (2,1) + 2 Columns span"), 2,1, 1,2) # row , colum, rowspan, colspan

window.setLayout(layout)
window.show()
sys.exit(app.exec())