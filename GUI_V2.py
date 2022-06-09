import sys
from PySide2.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QTableWidget)
from PySide2.QtCore import QSize, QFileSystemWatcher, QTimer, QObject, Qt
from PySide2.QtGui import QIcon
import buttons, plots_v2, os, time
from threading import Thread

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
        buttonBar = buttons.ButtonBar(buttonWidth)
        mainLayout.addWidget(buttonBar)

        self.Plots = plots_v2.Plots()
        mainLayout.addWidget(self.Plots)

        self.paths = "C:/Users/mattm/OneDrive/Documents/Code/CanSatCode/Flight_1076_C.csv"

        self.state = True
        self.thread()
        # self.watcher = QFileSystemWatcher(paths)
        # self.watcher.fileChanged.connect(self.watcher, print("change in file"))#self.updatePlot()
        # self.watcher.directoryChanged.connect(print("directory changed"))

        #Finalize
        widget = QWidget()
        self.setCentralWidget(widget)

        widget.setLayout(mainLayout)

        self.setMinimumSize(QSize(windowWidth,windowHeight))
        self.showMaximized()

    def thread(self):
        self.t1 = Thread(target=self.newPlot)
        self.t1.start()
        time.sleep(0.5)
  

    def newPlot(self):
        coarse = Qt.CoarseTimer
        while self.state is True:
            self.Plots.updatePlot()
            # self.timer = QTimer()
            # self.timer.moveToThread(self.t1)
            # self.timer.start(500)
            # size = os.path.getsize(self.paths)
            # if os.path.getsize(self.paths) != size:
            #self.Plots.updatePlot()
            
            
            
    def stopThread(self):
        self.t1.join()
     
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()

    window.state = False
 