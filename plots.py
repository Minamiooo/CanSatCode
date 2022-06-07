from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QGridLayout, QPushButton, QTableWidget)
from PyQt5.QtCore import QSize

import sys
import numpy as np
import pandas as pd
import pyqtgraph as pg

class Plots(QWidget):
    def __init__(self, fileName):
    
        super().__init__()

        self.MissionTime = []
        self.ContainerVoltage = []
        self.ContainerTemperature = []
        self.ContainerAltitude = []
        self.ContainerGPSLatitude = []
        self.ContainerGPSLongitude = []
        self.ContainerGPSAltitude = []
        self.PayloadVoltage = []
        self.PayloadTemperature = []
        self.PayloadAltitude = []

        data = pd.read_csv(fileName)
        self.MissionTime = data['MISSION_TIME'] #160 seconds max 
        self.ContainerVoltage = data['VOLTAGE'] #9V max 
        self.ContainerTemperature = data['TEMP'] #15 Celsius to 35 Celsius 
        self.ContainerAltitude = data['ALTITUDE'] #0 to 750m 
        self.ContainerGPSLatitude = data['GPS_LATITUDE'] 
        self.ContainerGPSLongitude = data['GPS_LONGITUDE'] 

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.graphWidget = pg.PlotWidget()
        pen = pg.mkPen(color=(255, 0, 0), width=2)

        self.x = self.MissionTime
        self.y = self.ContainerVoltage

        self.graphWidget.setBackground('w')
        self.graphWidget.showGrid(x=True, y=True)
        
        self.lineRef = self.graphWidget.plot(self.x, self.y, name="Voltage", pen=pen, symbol='o')
        self.graphWidget.setLabel('left', 
            '<span style=\"color:black;font-size:20px\">Voltage [Volts]</span>')
        self.graphWidget.setLabel('bottom', 
            '<span style=\"color:black;font-size:20px\">Mission Time [Seconds]</span>')
        
        self.update_plot_data(fileName)

        self.layout.addWidget(self.graphWidget,1,1)

    def update_plot_data(self, fileName):

        data = pd.read_csv(fileName)
        self.MissionTime = data['MISSION_TIME'] #160 seconds max 
        self.ContainerVoltage = data['VOLTAGE'] #9V max 
        self.ContainerTemperature = data['TEMP'] #15 Celsius to 35 Celsius 
        self.ContainerAltitude = data['ALTITUDE'] #0 to 750m 
        self.ContainerGPSLatitude = data['GPS_LATITUDE'] 
        self.ContainerGPSLongitude = data['GPS_LONGITUDE'] 

        self.x = self.MissionTime
        self.y = self.ContainerVoltage

        self.x.append(self.x)
        self.y.append(self.y)

        self.lineRef.setData(self.x, self.y)
        

        

        
