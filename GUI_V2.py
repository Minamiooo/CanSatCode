import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QTableWidget)
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
import buttons, plots_v2

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

        Plots = plots_v2.Plots()
        mainLayout.addWidget(Plots)

        #Finalize
        widget = QWidget()
        self.setCentralWidget(widget)

        widget.setLayout(mainLayout)

        self.setMinimumSize(QSize(windowWidth,windowHeight))
        self.showMaximized()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()