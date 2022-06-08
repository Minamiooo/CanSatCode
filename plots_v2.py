from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QGridLayout, QPushButton, QTableWidget)
from PySide6.QtCore import QSize

import sys
import numpy as np
import pandas as pd
import pyqtgraph as pg

class Plots(QWidget):
    def __init__(self):
    
        super().__init__()

        self.initialPlot()

    def initialPlot(self):
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        containerData = pd.read_csv("Flight_1076_C.csv")
        payloadData = pd.read_csv("Flight_1076_P.csv")

        #Container
        self.container = {
            "MissionTime": self.timeConvert(containerData['MISSION_TIME']), #160 seconds max 
            "Voltage": containerData['VOLTAGE'], #9V max
            "Temperature": containerData['TEMP'], #15 Celsius to 35 Celsius 
            "Altitude": containerData['ALTITUDE'], #0 to 750m 
            "Latitude": containerData['GPS_LATITUDE'],
            "Longitude": containerData['GPS_LONGITUDE']
        }
        #Payload
        self.payload = {
            "MissionTime": self.timeConvert(payloadData['MISSION_TIME']),
            "Voltage": payloadData['TP_VOLTAGE'], #9V max
            "Temperature": payloadData['TP_TEMP'],
            "Altitude": payloadData['TP_ALTITUDE'], #0 to 750m 
        }

        #Instantiate PlotWidget objects
        self.voltagePlotWidget = pg.PlotWidget()
        self.tempPlotWidget = pg.PlotWidget()
        self.altPlotWidget = pg.PlotWidget()
        self.GPSPlotWidget = pg.PlotWidget()

        redpen = pg.mkPen(color=(255, 0, 0), width=2)
        bluepen = pg.mkPen(color=(0, 0, 255), width=2)

        #Voltage Plot
        self.voltagePlotWidget.setBackground('w')
        self.voltagePlotWidget.showGrid(x=True, y=True)
        self.voltagePlotWidget.setTitle(
            "Voltage vs. Mission Time", color="k", size="10pt")
        self.voltagePlotWidget.addLegend()

        self.voltagePlotWidget.plot(
            self.container["MissionTime"], self.container["Voltage"], name="Container Voltage", pen=redpen, symbol='o')
        self.voltagePlotWidget.plot(
            self.payload["MissionTime"], self.payload["Voltage"], name="Payload Voltage", pen=bluepen, symbol='o')
        self.voltagePlotWidget.setLabel('left', 
            '<span style=\"color:black;font-size:10px\">Voltage [Volts]</span>')
        self.voltagePlotWidget.setLabel('bottom', 
            '<span style=\"color:black;font-size:10px\">Mission Time [Seconds]</span>')   

        #Temperature Plot
        self.tempPlotWidget.setBackground('w')
        self.tempPlotWidget.showGrid(x=True, y=True)
        self.tempPlotWidget.setTitle(
            "Temperature vs. Mission Time", color="k", size="10pt")
        self.tempPlotWidget.addLegend()

        self.tempPlotWidget.plot(
            self.container["MissionTime"], self.container["Temperature"], name="Container Temperature", pen=redpen, symbol='o')
        self.tempPlotWidget.plot(
            self.payload["MissionTime"], self.payload["Temperature"], name="Payload Temperature", pen=bluepen, symbol='o')
        self.tempPlotWidget.setLabel('left', 
            '<span style=\"color:black;font-size:10px\">Temperature [degree C]</span>')
        self.tempPlotWidget.setLabel('bottom', 
            '<span style=\"color:black;font-size:10px\">Mission Time [Seconds]</span>') 
       
        #Altitude Plot
        self.altPlotWidget.setTitle(
            "Altitude vs. Mission Time", color="k", size="10pt")
        self.altPlotWidget.setBackground('w')
        self.altPlotWidget.showGrid(x=True, y=True)
        self.altPlotWidget.addLegend()

        self.altPlotWidget.plot(
            self.container["MissionTime"], self.container["Altitude"], name="Container Altitude", pen=redpen, symbol='o')
        self.altPlotWidget.plot(
            self.payload["MissionTime"], self.payload["Altitude"], name="Payload Altitude", pen=bluepen, symbol='o')
        self.altPlotWidget.setLabel('left', 
            '<span style=\"color:black;font-size:10px\">Altitude [m]</span>')
        self.altPlotWidget.setLabel('bottom', 
            '<span style=\"color:black;font-size:10px\">Mission Time [Seconds]</span>') 

        #GPS Plot
        self.GPSPlotWidget.setBackground('w')
        self.GPSPlotWidget.showGrid(x=True, y=True)
        self.GPSPlotWidget.setTitle(
            "Latitude vs. Longitude", color="k", size="10pt")

        self.GPSPlotWidget.plot(
            self.container["Longitude"], self.container["Latitude"], name="GPS", pen=redpen, symbol='+')
        self.GPSPlotWidget.setLabel('left', 
            '<span style=\"color:black;font-size:10px\">Latitude [deg]</span>')
        self.GPSPlotWidget.setLabel('bottom', 
            '<span style=\"color:black;font-size:10px\">Longitude [deg]</span>')
                
        #Add Plots to GridLayout
        self.layout.addWidget(self.voltagePlotWidget,1,1)
        self.layout.addWidget(self.tempPlotWidget,1,2)
        self.layout.addWidget(self.altPlotWidget,2,1,1,2)
        self.layout.addWidget(self.GPSPlotWidget,1,3,2,2)

    def timeConvert(self, timeArr): #converts array of time codes HH:MM:SS to seconds
        timeArr = pd.to_datetime(timeArr, format='%H:%M:%S')
        timeArr = (3600*timeArr.dt.hour + 60*timeArr.dt.minute + timeArr.dt.second) #Assumes time starts at 0
        return timeArr.astype(float)

    def updatePlot(self): #QFileSystemWatcher sig & slot
        pass

