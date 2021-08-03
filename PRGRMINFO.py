from PyQt5 import QtWidgets, uic
import webbrowser as wb
import os

dir = os.getcwd() + '\\data\\'
subui = uic.loadUiType(dir+'prgrminfo.ui')[0]
class ProgramInfo(QtWidgets.QDialog, subui):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self.setFixedSize(306,169)
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.gotourl)
        self.pushButton.clicked.connect(self.close)
        
    def gotourl(self):
        wb.open('https://github.com/dpvpd/ImageCompare')

    def showModal(self):
        return super().exec_()