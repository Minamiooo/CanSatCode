import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QGridLayout, QPushButton, QTableWidget)
from PyQt5.QtGui import QPalette, QColor, QIcon
from PyQt5.QtCore import QSize, Qt
import pandas as pd
import pyqtgraph as pg
import Plotting

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

        #Initialize Variables
        buttonWidth = 100
        windowWidth = 800
        windowHeight = 600
        tableHeight = 150

        #Set Window Properties
        self.setWindowTitle("Ground Station")
        self.setWindowIcon(QIcon("strudel.png"))

        screen = app.primaryScreen()
        size = screen.size()
        if size.width() == 3840 and size.height() == 2160: #If 4k resolution
            buttonWidth *= 4
            windowWidth *= 2
            windowHeight *= 2
            tableHeight *= 2

        #Instantiate Layouts
        mainLayout = QVBoxLayout()
        buttonLayout = QHBoxLayout()
        chartLayout = QGridLayout()

        #Set Buttons
        button1 = QPushButton("Start"); button1.setMaximumWidth(buttonWidth); button1.setCheckable(True)
        button1.clicked.connect(self.button1Clicked)
        button2 = QPushButton("Stop"); button2.setMaximumWidth(buttonWidth); button2.setCheckable(True)
        button3 = QPushButton("Sim Mode Activate"); button3.setMaximumWidth(buttonWidth); button3.setCheckable(True)
        button4 = QPushButton("Sim Mode Start"); button4.setMaximumWidth(buttonWidth); button4.setCheckable(True)

        #Set Table
        csvTable = Color('red'); csvTable.setMaximumHeight(tableHeight)

        #Add Buttons
        buttonLayout.addWidget(button1)
        buttonLayout.addWidget(button2)
        buttonLayout.addWidget(button3)
        buttonLayout.addWidget(button4)

        #Add Chart Elements
        # chartLayout.addWidget(Color('red'),1,1) #Voltage
        # chartLayout.addWidget(Color('blue'),1,2) #Temp
        # chartLayout.addWidget(Color('green'),2,1,1,2) #Altitude
        # chartLayout.addWidget(Color('yellow'),1,3,2,2) #GPS

        mainLayout.addLayout(buttonLayout)
        # mainLayout.addLayout(chartLayout)

        #---------------------------------------------------
        MissionTime = []
        ContainerVoltage = []
        ContainerTemperature = []
        ContainerAltitude = []
        ContainerGPSLatitude = []
        ContainerGPSLongitude = []
        ContainerGPSAltitude = []
        PayloadVoltage = []
        PayloadTemperature = []
        PayloadAltitude = []

        data = pd.read_csv('containertest.csv') # ADD FILE NAME HERE FOR CSV DATA
        MissionTime = data['MISSION_TIME'].tolist() #160 seconds max 
        ContainerVoltage = data['VOLTAGE'].tolist() #9V max 
        ContainerTemperature = data['TEMP'].tolist() #15 Celsius to 35 Celsius 
        ContainerAltitude = data['ALTITUDE'].tolist() #0 to 750m 
        ContainerGPSLatitude = data['GPS_LATITUDE'].tolist() 
        ContainerGPSLongitude = data['GPS_LONGITUDE'].tolist() 
        
        # Setting up Plot/Layouts
        pg_layout = pg.GraphicsLayoutWidget()
        pg_layout.setBackground('w') 
        
        p1 = pg_layout.addPlot(row=0, col=0)
        
        Vc = p1.plot(x=MissionTime, y=ContainerVoltage, pen='r')
        Vp = p1.plot(x=MissionTime, y=PayloadVoltage, pen='b')
        p1.setTitle("Voltage vs. Mission Time")

        p2 = pg_layout.addPlot(row=0, col=1)
        Tc = p2.plot(x=MissionTime, y=ContainerTemperature, pen='r')
        Tp = p2.plot(x=MissionTime, y=PayloadTemperature, pen='b')
        p2.setTitle("Temperature vs. Mission Time")
        
        p3 = pg_layout.addPlot(row=2, col=0, colspan=2)
        Ac = p3.plot(x=MissionTime, y=ContainerAltitude, pen='r')
        Ap = p3.plot(x=MissionTime, y=PayloadAltitude, pen='b')
        p3.setTitle("Altitude vs. Mission Time")
        
        p4 = pg_layout.addPlot(row=0, col=2, rowspan=4, colspan=4)
        p4.plot(ContainerGPSLongitude, ContainerGPSLatitude, symbol='+')
        
        # Adding Labels and Range to Each Plot
        # Plot 1 - Voltage (9V max, 160 seconds max)
        p1.setLabel('left',"Voltage (Volts)")
        p1.setLabel('bottom', "Mission Time (seconds)")
        p1.setXRange(0, 160)
        p1.setYRange(0, 9)
        
        # Plot 2 - Temperature (15 Celsius to 35 Celsius, 160 seconds max)
        p2.setLabel('left',"Temperature (Celsius)")
        p2.setLabel('bottom', "Mission Time (seconds)")
        p2.setXRange(0, 160)
        p2.setYRange(15, 35)
        
        # Plot 3 - Altitude (750m max, 160 seconds max)
        p3.setLabel('left',"Altitude (meters)")
        p3.setLabel('bottom', "Mission Time (seconds)")
        p3.setXRange(0, 160)
        p3.setYRange(0, 750)
        
        # Plot 4 - GPS
        p4.setLabel('left',"Latitude")
        p4.setLabel('bottom', "Longitude")
        p4.setXRange(-80.6287, -80.5628)
        p4.setYRange(37.1851, 37.2087)

        mainLayout.addWidget(pg_layout)
        #---------------------------------------------------
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