from PyQt5 import QtCore, QtGui, QtWidgets, uic
import os

dir = os.getcwd() + '\\data\\'
_translate = QtCore.QCoreApplication.translate


subui = uic.loadUiType(dir+'dirselect.ui')[0]
class Select(QtWidgets.QDialog, subui):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self.setFixedSize(316,123)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.select1)
        self.pushButton_2.clicked.connect(self.select2)
        self.pushButton_3.clicked.connect(self.accept)
        self.pushButton_4.clicked.connect(self.reject)
        
    def select1(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(self, '폴더 선택').replace('/','\\')+'\\'
        self.lineEdit.setText(_translate("Dialog", path))
    def select2(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(self, '폴더 선택').replace('/','\\')+'\\'
        self.lineEdit_2.setText(_translate("Dialog", path))

    def showModal(self):
        return super().exec_()