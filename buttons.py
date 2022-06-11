from PySide2.QtWidgets import (QWidget, QHBoxLayout, QPushButton, QSizePolicy, QSpacerItem)
from PySide2.QtCore import QRunnable, Slot, QThreadPool
from GUI_V2 import running
import time

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

        self.threadpool = QThreadPool()
        
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

        self.button1.clicked.connect(self.startButton1Thread)
        self.button2.clicked.connect(self.startButton2Thread)
        self.button3.clicked.connect(self.startButton3Thread)
        self.button4.clicked.connect(self.startButton4Thread)
        self.button5.clicked.connect(self.startButton5Thread)

    def startButton1Thread(self):
        button1worker = Button1Worker()
        self.threadpool.start(button1worker)
    
    def startButton2Thread(self):
        button2worker = Button2Worker()
        self.threadpool.start(button2worker)

    def startButton3Thread(self):
        button3worker = Button3Worker()
        self.threadpool.start(button3worker)

    def startButton4Thread(self):
        button4worker = Button4Worker()
        self.threadpool.start(button4worker)

    def startButton5Thread(self):
        button5worker = Button5Worker()
        self.threadpool.start(button5worker)


class Button1Worker(QRunnable):
    @Slot()
    def run(self): #Code to be executed
        while running:
            print("button1")
            time.sleep(1)

class Button2Worker(QRunnable):
    @Slot()
    def run(self): #Code to be executed
        while running:
            print("button2")
            time.sleep(1)

class Button3Worker(QRunnable):
    @Slot()
    def run(self): #Code to be executed
        while running:
            print("button3")
            time.sleep(1)

class Button4Worker(QRunnable):
    @Slot()
    def run(self): #Code to be executed
        while running:
            print("button4")
            time.sleep(1)

class Button5Worker(QRunnable):
    @Slot()
    def run(self): #Code to be executed
        while running:
            print("button5")
            time.sleep(1)
