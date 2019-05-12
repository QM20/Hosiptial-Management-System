# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'capture_widget.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

class capture_widget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)  # 相当于下面那句
        self.setupUi()
    def setupUi(self):
        self.background_lable = QtWidgets.QLabel(self)
        self.background_lable.setGeometry(QtCore.QRect(0, 0, 845, 480))
        self.background_lable.setObjectName("background_lable")
        self.logo_lable = QtWidgets.QLabel(self)
        self.logo_lable.setGeometry(QtCore.QRect(10, 10, 31, 41))
        self.logo_lable.setObjectName("logo_lable")
        self.back_button = QtWidgets.QPushButton(self)
        self.back_button.setGeometry(QtCore.QRect(70, 20, 80, 26))
        self.back_button.setObjectName("back_button")
        self.capture_lable = QtWidgets.QLabel(self)
        self.capture_lable.setGeometry(QtCore.QRect(300, 50, 181, 121))
        self.capture_lable.setObjectName("capture_lable")
        self.record_button = QtWidgets.QPushButton(self)
        self.record_button.setGeometry(QtCore.QRect(270, 340, 91, 41))
        self.record_button.setObjectName("record_button")
        self.clear_button = QtWidgets.QPushButton(self)
        self.clear_button.setGeometry(QtCore.QRect(460, 340, 91, 41))
        self.clear_button.setObjectName("clear_button")
        self.name_lable = QtWidgets.QLabel(self)
        self.name_lable.setGeometry(QtCore.QRect(320, 230, 55, 18))
        self.name_lable.setObjectName("name_lable")
        self.class_lable = QtWidgets.QLabel(self)
        self.class_lable.setGeometry(QtCore.QRect(320, 310, 55, 18))
        self.class_lable.setObjectName("class_lable")
        self.name_input = QtWidgets.QLineEdit(self)
        self.name_input.setGeometry(QtCore.QRect(450, 230, 113, 26))
        self.name_input.setObjectName("lineEdit")
        self.password_input = QtWidgets.QLineEdit(self)
        self.password_input.setGeometry(QtCore.QRect(450, 300, 113, 26))
        self.password_input.setObjectName("lineEdit_2")

        # background
        jpg = QtGui.QPixmap("bg.jpg").scaled(self.background_lable.width(), self.background_lable.height())
        self.background_lable.setPixmap(jpg)
        #face
        face = QtGui.QPixmap("人脸.jpg").scaled(self.capture_lable.width(), self.capture_lable.height())
        self.capture_lable.setPixmap(face)
        # logo
        logo = QtGui.QPixmap("logo716.png").scaled(self.logo_lable.width(), self.logo_lable.height())
        self.logo_lable.setPixmap(logo)

        self.back_button.raise_()
        self.capture_lable.raise_()
        self.record_button.raise_()
        self.clear_button.raise_()
        self.name_lable.raise_()
        self.class_lable.raise_()
        self.name_input.raise_()
        self.password_input.raise_()


        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        #self.background_lable.setText(_translate("Form", "TextLabel"))
        #self.logo_lable.setText(_translate("Form", "TextLabel"))
        self.back_button.setText(_translate("Form", "返回"))
        #self.capture_lable.setText(_translate("Form", "功能选择"))
        self.record_button.setText(_translate("Form", "录入"))
        self.clear_button.setText(_translate("Form", "清空输入信息"))
        self.name_lable.setText(_translate("Form", "姓名"))
        self.class_lable.setText(_translate("Form", "班级"))
        self.name_input.setText(_translate("Form", "请输入姓名"))
        self.password_input.setText(_translate("Form", "请输入班级"))


