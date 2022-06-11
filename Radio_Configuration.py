# This file deals with all Team Strudels #1076 radio handling  
# For use, csv_gen and the digi library are needed
import serial, time, csv
import csv_gen as c
import MQTT_Configuration as mqtt
from digi.xbee.devices import XBeeDevice, RemoteXBeeDevice, XBee16BitAddress

### Initiliaze the port and XBee communication
gcs_xbeeserial = serial.Serial(port = "COM3", baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
gcs_xbee = XBeeDevice("COM3", 9600)
container64address = "8888" #  "0013A20041F1CE3F" # denotes container 64 bit hex address
con_xbee = RemoteXBeeDevice(gcs_xbee, XBee16BitAddress.from_hex_string(container64address))
### Initiliaze the port and XBee communication

def Initialize():
    gcs_xbeeserial = serial.Serial(port = "COM3", baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
    c.build_csv() # creates csv files
    mqtt.connect_mqtt()

def regularmode(): # possibly not doing this
    gcs_xbeeserial.close()
    gcs_xbee = XBeeDevice("COM3", 9600)
    gcs_xbee.open()
    container64address = "8888" #  "0013A20041F1CE3F" # denotes container hex address
    con_xbee = RemoteXBeeDevice(gcs_xbee, XBee16BitAddress.from_hex_string(container64address))
    gcs_xbee.send_data_async_16(con_xbee,"10222000")
    gcs_xbee.close()
    Initialize()

def Read_data():
    data = gcs_xbeeserial.readline()
    newdata = data[9:-2]
    #print(len(newdata))
    if newdata != '':
        newdata = newdata.decode()   
        newdata = newdata.split(",")
        print(newdata)
        #if newdata[4] == 'C':
        c.append_csv(newdata)
        #elif newdata[4] == 'T':
        #    c.appendpayload_csv(newdata) # append written data to csv 
    else:
        pass

#while True:
    #Read_data()

def End_comms():
    gcs_xbeeserial.close()
    print('XBee Communication has stopped')

"""
    In the case of rain, a simulation mode has been created. Commands below enable and begin simulation data transmission. 
    They are to be used in conjunction with commands such as Initialize() and Read_Data() since all processes will be 
    mostly the same
    
"""

def SIMULATION_ENABLE():
    gcs_xbee.send_data_async(con_xbee,"12112000")

def SIMULATION_START():
    with open('practicefile.csv','r') as file:
        pressure = csv.reader(file)
        pressure = list(pressure)
        for rows in pressure:
            gcs_xbee._send_data_async_64(container64address,'',rows) # sends data via xbee library
            time.sleep(1)