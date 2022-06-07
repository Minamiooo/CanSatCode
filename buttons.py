from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QPushButton)
from PyQt5.QtCore import QSize

class ButtonBar(QWidget):
    def __init__(self):
    
        super().__init__()

        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.button1 = QPushButton("Start")
        self.button2 = QPushButton("Stop")
        self.button3 = QPushButton("Begin Comms")
        self.button4 = QPushButton("Sim Mode Activate")
        self.button5 = QPushButton("Sim Mode Start")

        #button.setMaximumWidth(width)
        self.button1.setCheckable(True)
        self.button2.setCheckable(True)
        self.button3.setCheckable(True)
        self.button4.setCheckable(True)
        self.button5.setCheckable(True)

        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)
        self.layout.addWidget(self.button4)
        self.layout.addWidget(self.button5)
