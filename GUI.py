import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QTableWidget
from PyQt5.QtGui import QPalette, QColor, QIcon
from PyQt5.QtCore import QSize, Qt

class Color(QWidget): #creates a widget with a solid color for testing
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        buttonWidth = 100
        windowWidth = 800
        windowHeight = 600

        self.setWindowTitle("Ground Station")
        self.setWindowIcon(QIcon("strudel.png"))

        screen = app.primaryScreen()
        size = screen.size()
        if size.width() == 3840 and size.height() == 2160:
            buttonWidth = buttonWidth * 4
            windowWidth = windowWidth * 2
            windowHeight = windowHeight * 2

        mainLayout = QVBoxLayout()
        buttonLayout = QHBoxLayout()
        chartLayout = QGridLayout()

        button1 = QPushButton("Start"); button1.setMaximumWidth(buttonWidth); button1.setCheckable(True)
        button1.clicked.connect(self.button1Clicked)
        button2 = QPushButton("Stop"); button2.setMaximumWidth(buttonWidth); button2.setCheckable(True)
        button3 = QPushButton("Sim Mode Activate"); button3.setMaximumWidth(buttonWidth); button3.setCheckable(True)
        button4 = QPushButton("Sim Mode Start"); button4.setMaximumWidth(buttonWidth); button4.setCheckable(True)
        csvTable = Color('white'); csvTable.setMaximumHeight(150)

        buttonLayout.addWidget(button1)
        buttonLayout.addWidget(button2)
        buttonLayout.addWidget(button3)
        buttonLayout.addWidget(button4)

        chartLayout.addWidget(Color('red'),1,1) #Voltage
        chartLayout.addWidget(Color('blue'),1,2) #Temp
        chartLayout.addWidget(Color('green'),2,1,1,2) #Altitude
        chartLayout.addWidget(Color('yellow'),1,3,2,2) #GPS

        mainLayout.addLayout(buttonLayout)
        mainLayout.addLayout(chartLayout)

        mainLayout.addWidget(csvTable) 

        widget = QWidget()
        widget.setLayout(mainLayout) # Set main widget to vertical layout
        self.setCentralWidget(widget)
        self.setMinimumSize(QSize(windowWidth,windowHeight))
        self.showMaximized()

    def button1Clicked(self):
        # Q: will GUI freeze up with this while loop?
        #while datacollecting:
            # timer sleep
                # read when data its not being
            # read data from sensors and write to csv file
            # read csv fle and plot data (kayla)
                # read from csv using pyqt
                # plot with pyqt
        print("Clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()