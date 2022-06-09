import os
import time
from threading import Thread

fileName = "C:/Users/mattm/OneDrive/Documents/Code/CanSatCode/Flight_1076_C.csv"

def func1():
    while True:
        print(os.path.getsize(fileName))
        time.sleep(1)

def func2():
    while True:
        print("function 2")
        time.sleep(0.5)

def runA():
    while True:
        print('A\n')
        time.sleep(1)

def runB():
    while True:
        print('B\n')
        time.sleep(0.5)

if __name__ == "__main__":
    t1 = Thread(target = func1)
    t1.setDaemon(True)
    t1.start()
    while True:
        pass