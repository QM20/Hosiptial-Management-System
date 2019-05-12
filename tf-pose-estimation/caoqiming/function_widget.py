# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'function_widget.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

class function_widget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)  # 相当于下面那句
        self.setupUi()
    def setupUi(self):
        # Form.setObjectName("Form")
        # Form.resize(845, 480)
        self.background_lable = QtWidgets.QLabel(self)
        self.background_lable.setGeometry(QtCore.QRect(0, 0, 845, 480))
        self.background_lable.setObjectName("background_lable")
        self.logo_lable = QtWidgets.QLabel(self)
        self.logo_lable.setGeometry(QtCore.QRect(10, 10, 31, 41))
        self.logo_lable.setObjectName("logo_lable")
        self.back_button = QtWidgets.QPushButton(self)
        self.back_button.setGeometry(QtCore.QRect(70, 20, 80, 26))
        self.back_button.setObjectName("back_button")
        self.capture_button = QtWidgets.QPushButton(self)
        self.capture_button.setGeometry(QtCore.QRect(210, 150, 111, 51))
        self.capture_button.setObjectName("capture_button")
        self.train_button = QtWidgets.QPushButton(self)
        self.train_button.setGeometry(QtCore.QRect(460, 150, 111, 51))
        self.train_button.setObjectName("train_button")
        self.history_button = QtWidgets.QPushButton(self)
        self.history_button.setGeometry(QtCore.QRect(210, 270, 111, 51))
        self.history_button.setObjectName("history_button")
        self.setting_button = QtWidgets.QPushButton(self)
        self.setting_button.setGeometry(QtCore.QRect(460, 270, 111, 51))
        self.setting_button.setObjectName("setting_button")
        self.function_lable = QtWidgets.QLabel(self)
        self.function_lable.setGeometry(QtCore.QRect(350, 60, 101, 51))
        self.function_lable.setObjectName("function_lable")

        jpg = QtGui.QPixmap("bg.jpg").scaled(self.background_lable.width(), self.background_lable.height())
        self.background_lable.setPixmap(jpg)
        logo = QtGui.QPixmap("logo716.png").scaled(self.logo_lable.width(), self.logo_lable.height())
        self.logo_lable.setPixmap(logo)


        self.logo_lable.raise_()
        self.back_button.raise_()
        self.capture_button.raise_()
        self.train_button.raise_()
        self.history_button.raise_()
        self.setting_button.raise_()
        self.function_lable.raise_()



        self.retranslateUi()
        #QtCore.QMetaObject.connectSlotsByName()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        #Form.setWindowTitle(_translate("Form", "Form"))
        self.back_button.setText(_translate("Form", "返回"))
        self.capture_button.setText(_translate("Form", "人员录入"))
        self.train_button.setText(_translate("Form", "开始训练"))
        self.history_button.setText(_translate("Form", "训练历史"))
        self.setting_button.setText(_translate("Form", "系统设置"))
        self.function_lable.setText(_translate("Form", "功能选择"))


