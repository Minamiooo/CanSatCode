# CSV Generation for payload and container
import pandas as pd
import os.path 
import csv
from csv import writer

headerCON = ['TEAM_ID', 'MISSION_TIME', 'PACKET_COUNT','PACKET_TYPE','MODE','TP_RELEASED','ALTITUDE','TEMP','VOLTAGE','GPS_TIME',
            'GPS_LATITUDE','GPS_LONGITUDE','GPS_ALTITUDE','GPS_SATS','SOFTWARE_STATE','CMD_ECHO']

headerPAY = ['TEAM_ID', 'MISSION_TIME', 'PACKET_COUNT','PACKET_TYPE','TP_ALTITUDE','TP_TEMP','TP_VOLTAGE','GYRO_R','GYRO_P','GYRO_Y','ACCEL_R','ACCEL_P','ACCEL_Y'
            ,'MAG_R','MAG_P','MAG_Y','POINTING_ERROR','TP_SOFTWARE_STATE']

# build_csv builds the csv file to store all data in
def build_csv():
    
    if os.path.exists("C:/Users/aarra/Python/CANSAT/Flight_1076_C.csv") == False:
    
        with open('Flight_1076_C.csv','w') as file:
            writerCON = csv.writer(file, delimiter = ",")
            writerCON.writerow(headerCON)
            file.close()

        with open('Flight_1076_P.csv','w') as file:
            writerPAY = csv.writer(file, delimiter = ',')
            writerPAY.writerow(headerPAY)
            file.close()
    else:
        pass

# append_csv makes sure the csv files exist then adds data to them as it is received  
def append_csv(container_data):
    
    if os.path.exists("C:/Users/aarra/Python/CANSAT/Flight_1076_C.csv") == True:
    
        with open('Flight_1076_C.csv','a') as file:
            writerCON = csv.writer(file)
            writerCON.writerow(container_data)
            file.close()
    else:
        build_csv()

        with open('Flight_1076_C.csv','a') as file:
            writerCON = csv.writer(file)
            writerCON.writerow(container_data)
            file.close()

def appendpayload_csv(payload_data):
        if os.path.exists("C:/Users/aarra/Python/CANSAT/Flight_1076_C.csv") == True:
            with open('Flight_1076_P.csv','a') as file:
                writerPAY = csv.writer(file)
                writerPAY.writerow(payload_data)
                file.close()
        else:
            build_csv()
            
            with open('Flight_1076_P.csv','a') as file:
                writerPAY = csv.writer(file)
                writerPAY.writerow(payload_data)
                file.close()




def append_pandas(data):
    
    if os.path.exists("C:/Users/aarra/Python/CANSAT/Flight_1076_C.csv") == True:
        dataframe = pd.DataFrame(data)
        dataframe.to_csv('C:/Users/aarra/Python/CANSAT/Flight_1076_C.csv', mode='a', index=False, header=False)
    else:
        build_csv()
        dataframe = pd.DataFrame(data)
        dataframe.to_csv('C:/Users/aarra/Python/CANSAT/Flight_1076_C.csv', mode='a', index=False, header=False )
        pass
