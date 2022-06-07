from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys
import os
from random import randint

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        self.x = list(range(100))
        self.y = [randint(0,100) for _ in range(100)]

        self.graphWidget.setBackground('w')

        pen = pg.mkPen(color=(255, 0, 0), width=5)
        self.graphWidget.addLegend() #must be called before plot()
        self.graphWidget.showGrid(x=True, y=True)

        self.lineRef = self.graphWidget.plot(self.x, self.y, name="Sensor 1", pen=pen, symbol='o')
        self.graphWidget.setLabel('left', 
            '<span style=\"color:red;font-size:20px\">y axis</span>')
        self.graphWidget.setLabel('bottom', 
            '<span style=\"color:red;font-size:20px\">x axis</span>')

        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def update_plot_data(self):
        
        self.x = self.x[1:]
        self.x.append(self.x[-1] + 1)

        self.y = self.y[1:]
        self.y.append( randint(0,100))

        self.lineRef.setData(self.x, self.y)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

