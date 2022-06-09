import pandas as pd


#timeArr = pd.array(["00:00:00","00:04:13","01:03:59"])
containerData = pd.read_csv("Flight_1076_C.csv")
timeArr = containerData["MISSION_TIME"]

def timeConvert(arr):
    arr = pd.to_datetime(arr, format='%H:%M:%S')
    arr = (3600*arr.dt.hour + 60*arr.dt.minute + arr.dt.second) #Assumes time starts at 0
    return arr.astype(float)

container = {
            "MissionTime": timeConvert(containerData['MISSION_TIME']).tolist(), #160 seconds max 
            "Voltage": containerData['VOLTAGE'].tolist(), #9V max
            "Temperature": containerData['TEMP'].tolist(), #15 Celsius to 35 Celsius 
            "Altitude": containerData['ALTITUDE'].tolist(), #0 to 750m 
            "Latitude": containerData['GPS_LATITUDE'].tolist(),
            "Longitude": containerData['GPS_LONGITUDE'].tolist()
        }



# for i in range(len(timeArr)):
#     t = sum(x * int(t) for x, t in zip([3600, 60, 1], timeArr[i].split(":")))
#     timeArr[i] = timeArr[i].apply(int)

print(container["MissionTime"][-1])


# def timeConvert(timeArr):
#     timeArr.astype(int)
#     for i in range(len(timeArr)):
#         h, m, s = timeArr[i].split(':')
#         timeArr[i] = 3600*int(h) + 60*int(m) + int(s)
#     return timeArr

# print(timeConvert(timeArr))