from PySide6.QtWidgets import (QWidget, QHBoxLayout, QPushButton, QSizePolicy, QSpacerItem)

class ButtonBar(QWidget):
    def __init__(self, width):
    
        super().__init__()

        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.spacer = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.button1 = QPushButton("Start")
        self.button2 = QPushButton("Stop")
        self.button3 = QPushButton("Begin Comms")
        self.button4 = QPushButton("Sim Mode Activate")
        self.button5 = QPushButton("Sim Mode Start")

        self.button1.setMaximumWidth(width)
        self.button2.setMaximumWidth(width)
        self.button3.setMaximumWidth(width)
        self.button4.setMaximumWidth(width)
        self.button5.setMaximumWidth(width)

        self.button1.setCheckable(True)
        self.button2.setCheckable(True)
        self.button3.setCheckable(True)
        self.button4.setCheckable(True)
        self.button5.setCheckable(True)

        self.layout.addSpacerItem(self.spacer)
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)
        self.layout.addWidget(self.button4)
        self.layout.addWidget(self.button5)
        self.layout.addSpacerItem(self.spacer)

        self.button1.clicked.connect(self.button1Clicked)
        self.button2.clicked.connect(self.button2Clicked)
        self.button3.clicked.connect(self.button3Clicked)
        self.button4.clicked.connect(self.button4Clicked)
        self.button5.clicked.connect(self.button5Clicked)

    def button1Clicked(self):
        pass
    def button2Clicked(self):
        pass
    def button3Clicked(self):
        pass
    def button4Clicked(self):
        pass
    def button5Clicked(self):
        pass
