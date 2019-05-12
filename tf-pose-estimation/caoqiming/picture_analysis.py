# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'picture_analysis.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

class picture_analysis(QWidget):
    def __init__(self, parent):
        super().__init__(parent)  # 相当于下面那句
        self.setupUi()
    def setupUi(self,):
        self.background_lable = QtWidgets.QLabel(self)
        self.background_lable.setGeometry(QtCore.QRect(0, 0, 845, 480))
        self.background_lable.setObjectName("background_lable")
        self.logo_lable = QtWidgets.QLabel(self)
        self.logo_lable.setGeometry(QtCore.QRect(10, 10, 31, 41))
        self.logo_lable.setObjectName("logo_lable")
        self.back_button = QtWidgets.QPushButton(self)
        self.back_button.setGeometry(QtCore.QRect(70, 20, 80, 26))
        self.back_button.setObjectName("back_button")

        self.picture = QtWidgets.QLabel(self)
        self.picture.setGeometry(QtCore.QRect(30, 70, 741, 361))
        self.picture.setObjectName("picture")

        self.picture.raise_()
        self.back_button.raise_()
        self.logo_lable.raise_()
        # logo
        logo = QtGui.QPixmap("logo716.png").scaled(self.logo_lable.width(), self.logo_lable.height())
        self.logo_lable.setPixmap(logo)
        # background
        jpg = QtGui.QPixmap("bg.jpg").scaled(self.background_lable.width(), self.background_lable.height())
        self.background_lable.setPixmap(jpg)
        self.logo_lable.raise_()
        self.table.raise_()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName()

    def retranslateUi(self,):
        _translate = QtCore.QCoreApplication.translate
        #self.background_lable.setText(_translate("Form", "TextLabel"))
        #self.logo_lable.setText(_translate("Form", "TextLabel"))
        self.back_button.setText(_translate("Form", "返回"))
        self.picture.setText(_translate("Form", "TextLabel"))


