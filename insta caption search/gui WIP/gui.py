from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QGridLayout
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
import sys
import re

savedata = {}

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QIcon('qt.png'))
        self.setWindowTitle("QtPy6")
        self.setContentsMargins(20, 20, 20, 20)

        layout = QGridLayout()

        self.setLayout(layout)

        title = QLabel("Keywords to Dictionary Program")
        layout.addWidget(title, 0, 0, 1, 3, Qt.AlignmentFlag.AlignCenter)

        label1 = QLabel("Category: ")
        layout.addWidget(label1, 1, 0)

        label2 = QLabel("Keyword: ")
        layout.addWidget(label2, 2, 0)

        self.input1 = QLineEdit()
        layout.addWidget(self.input1, 1, 1)

        self.input2 = QLineEdit()
        layout.addWidget(self.input2, 2, 1)

        savebutton = QPushButton("Submit")
        savebutton.setFixedWidth(50)
        savebutton.clicked.connect(self.save)
        layout.addWidget(savebutton, 3, 1, Qt.AlignmentFlag.AlignRight)

        savelistbutton = QPushButton("WIP")
        savelistbutton.setFixedWidth(50)
        savelistbutton.clicked.connect(self.savelist)
        layout.addWidget(savelistbutton, 3, 1, Qt.AlignmentFlag.AlignLeft)

    def removeq(string):
        string.remove("'")
        print(string)

    def save(self):
        cat = self.input1.text().lower()
        key = self.input2.text().lower()

        savedata[cat] = key.split(', ')
        print(savedata)
        
    def savelist(self):
        window2.show()

    def export(self):
        cat = self.input1.text()
        key = self.input2.text()
        

app = QApplication(sys.argv)
window = Window()
window2 = Window()

window.setStyleSheet("""
    QWidget {
        background-color: "#1f1f45";
        color: "white";
    }

    QPushButton {
        background-color: "white";
        color: "#1f1f45";
        font-size: 12px;
    }

    QLineEdit {
        background-color: "white";
        color: "#1f1f45";
        }


""")

window2.setStyleSheet("""
    QWidget {
        background-color: "#821c39";
        color: "white";
    }

    QPushButton {
        background-color: "white";
        color: "#821c39";
        font-size: 12px;
    }

    QLineEdit {
        background-color: "white";
        color: "#821c39";
        }


""")
window.show()
window2.hide()
sys.exit(app.exec())