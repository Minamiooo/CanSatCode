from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QGridLayout, QPushButton, QTableWidget,QTableWidgetItem)

class Table(QWidget):
    def __init__(self):
    
        super().__init__()

        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        