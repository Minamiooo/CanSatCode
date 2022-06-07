import sys
import numpy as np
import pandas as pd
import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication

# Initial arrays
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Practice Numbers
    #MissionTime = [1, 25, 50, 100, 150]
    #ContainerVoltage = [4, 5, 4.5, 5, 5.5]
    #ContainerTemperature = [16, 18, 22, 27, 25]
    #ContainerAltitude = [50, 200, 600, 750, 650]
    #ContainerGPSLatitude = [37.1982193732975, 37.1982074022768, 37.1981551938267, 37.1980681085355, 37.198000850163]
    #ContainerGPSLongitude = [-80.5827774266241, -80.5827720557983, -80.5827727159543, -80.5827801973479, -80.5827941707729]
    #PayloadVoltage = [2, 3, 3.5, 3, 4]
    #PayloadTemperature = [17, 20, 25, 30, 28]
    #PayloadAltitude = [48, 180, 500, 700, 600]
    
    # insert csv data
    data = pd.read_csv('test.csv') # ADD FILE NAME HERE FOR CSV DATA
    MissionTime = data['MISSION_TIME'] #160 seconds max 
    ContainerVoltage = data['VOLTAGE'] #9V max 
    ContainerTemperature = data['TEMP'] #15 Celsius to 35 Celsius 
    ContainerAltitude = data['ALTITUDE'] #0 to 750m 
    ContainerGPSLatitude = data['GPS_LATITUDE'] 
    ContainerGPSLongitude = data['GPS_LONGITUDE'] 
    
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
    # (-80.6287, -80.5628, 37.2087, 37.1851)
    
    pg_layout.show()
    
    status = app.exec_()
    sys.exit(status)
