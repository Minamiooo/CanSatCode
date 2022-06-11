import sys
from PySide2.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QTableWidget)
from PySide2.QtCore import QSize, QFileSystemWatcher, QTimer, QObject, Qt, Signal, Slot, QRunnable, QThreadPool
from PySide2.QtGui import QIcon
from matplotlib.pyplot import plot
import buttons, plots_v2, os, time
from threading import Thread
from plots_v2 import Plots
import csv_gen as c

global running
running = True

c.build_csv()

class PlotWorker(QRunnable):
    @Slot()
    def run(self): #Code to be executed
        while running:
            plots.updatePlot() #!!!!!!!!!!
            print("plot updated")
            time.sleep(.3)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Ground Station")
        self.setWindowIcon(QIcon("strudel.png"))

        #Initialize Variables
        buttonWidth = 150
        windowWidth = 800
        windowHeight = 600
        tableHeight = 150
        
        screen = app.primaryScreen()
        size = screen.size()
        if size.width() == 3840 and size.height() == 2160: #If 4k resolution
            buttonWidth *= 4
            windowWidth *= 2
            windowHeight *= 2
            tableHeight *= 2

        mainLayout = QVBoxLayout()

        #Add Widgets to mainLayout
        global buttonBar
        buttonBar = buttons.ButtonBar(buttonWidth)
        mainLayout.addWidget(buttonBar)

        global plots
        plots = plots_v2.Plots()
        mainLayout.addWidget(plots)

        # self.paths = "C:/Users/mattm/OneDrive/Documents/Code/CanSatCode/Flight_1076_C.csv"

        self.threadpool = QThreadPool() #Instantiate updateplot thread object
        self.startThread()
        # self.watcher = QFileSystemWatcher(paths)
        # self.watcher.fileChanged.connect(self.watcher, print("change in file"))#self.updatePlot()
        # self.watcher.directoryChanged.connect(print("directory changed"))

        #Finalize
        widget = QWidget()
        self.setCentralWidget(widget)

        widget.setLayout(mainLayout)

        self.setMinimumSize(QSize(windowWidth,windowHeight))
        self.showMaximized()

    def startThread(self):
        plotworker = PlotWorker()
        self.threadpool.start(plotworker)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()

    running = False
 