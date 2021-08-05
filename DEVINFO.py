from PyQt5 import QtWidgets, uic
import webbrowser as wb
import os

dir = os.getcwd() + '\\data\\'
subui = uic.loadUiType(dir+'devinfo.ui')[0]
class DevInfo(QtWidgets.QDialog, subui):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self.setFixedSize(242,132)
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.discord)
        self.pushButton_2.clicked.connect(self.github)
        self.pushButton.clicked.connect(self.close)
        
    def github(self):
        wb.open('https://github.com/dpvpd/ImageCompare')
    def discord(self):
        wb.open('https://discord.gg/c8uucPufAT')

    def showModal(self):
        return super().exec_()