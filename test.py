import pandas as pd

containerData = pd.read_csv("Flight_1076_C.csv")
timeArr = containerData["MISSION_TIME"]

for i in range(len(timeArr)):
    timeArr[i] = sum(x * int(t) for x, t in zip([3600, 60, 1], timeArr[i].split(":")))

print(timeArr)