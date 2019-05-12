# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from caoqiming.function_widget import function_widget
from caoqiming.capture_widget import capture_widget
from caoqiming.face_rec_widget import face_rec_widget
from caoqiming.train_widget import train_widget
from caoqiming.summary_widget import summary_widget

class Ui_Main_Dialog(object):
    def setupUi(self, Main_Dialog):
        Main_Dialog.setObjectName("Main_Dialog")
        Main_Dialog.resize(845, 480)
        self.Login_widget = QtWidgets.QWidget(Main_Dialog)
        self.Login_widget.setGeometry(QtCore.QRect(0, 0, 931, 601))
        self.Login_widget.setObjectName("Login_widget")
        self.system_name_2 = QtWidgets.QLabel(self.Login_widget)
        self.system_name_2.setGeometry(QtCore.QRect(350, 30, 181, 71))
        self.system_name_2.setObjectName("System_name_2")
        self.account_2 = QtWidgets.QLabel(self.Login_widget)
        self.account_2.setGeometry(QtCore.QRect(230, 140, 55, 18))
        self.account_2.setObjectName("account_2")
        self.password_2 = QtWidgets.QLabel(self.Login_widget)
        self.password_2.setGeometry(QtCore.QRect(230, 240, 55, 18))
        self.password_2.setObjectName("Password_2")
        self.account_input = QtWidgets.QLineEdit(self.Login_widget)
        self.account_input.setGeometry(QtCore.QRect(360, 140, 113, 26))
        self.account_input.setObjectName("lineEdit_3")
        self.password_input = QtWidgets.QLineEdit(self.Login_widget)
        self.password_input.setGeometry(QtCore.QRect(360, 230, 113, 26))
        self.password_input.setObjectName("lineEdit_4")
        self.login_button = QtWidgets.QPushButton(self.Login_widget)
        self.login_button.setGeometry(QtCore.QRect(280, 320, 80, 26))
        self.login_button.setObjectName("pushButton_3")
        self.logout_button = QtWidgets.QPushButton(self.Login_widget)
        self.logout_button.setGeometry(QtCore.QRect(390, 320, 80, 26))
        self.logout_button.setObjectName("pushButton_4")
        #background
        self.background = QtWidgets.QLabel(self.Login_widget)
        self.background.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        self.background.setObjectName("background")
        jpg = QtGui.QPixmap("bg.jpg").scaled(self.background.width(), self.background.height())
        self.background.setPixmap(jpg)
        #logo
        self.logo_lable = QtWidgets.QLabel(self.Login_widget)
        self.logo_lable.setGeometry(QtCore.QRect(10, 10, 22, 40))
        self.logo_lable.setObjectName("logo_lable")
        logo = QtGui.QPixmap("logo716.png").scaled(self.logo_lable.width(), self.logo_lable.height())
        self.logo_lable.setPixmap(logo)


        #new对象
        self.function_widget=function_widget(Main_Dialog)
        self.function_widget.close()
        self.capture_widget=capture_widget(Main_Dialog)
        self.capture_widget.close()
        self.face_rec_widget=face_rec_widget(Main_Dialog)
        self.face_rec_widget.close()
        self.train_widget=train_widget(Main_Dialog)
        self.train_widget.close()
        self.summary_widget=summary_widget(Main_Dialog)
        self.summary_widget.close()

        #置顶显示部件
        self.system_name_2.raise_()
        self.account_2.raise_()
        self.password_2.raise_()
        self.account_input.raise_()
        self.password_input.raise_()
        self.login_button.raise_()
        self.logout_button.raise_()






        self.retranslateUi(Main_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Main_Dialog)

    def retranslateUi(self, Main_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Main_Dialog.setWindowTitle(_translate("Main_Dialog", "Dialog"))
        self.system_name_2.setText(_translate("Main_Dialog", "基于动作识别的跳伞演练系统"))
        self.account_2.setText(_translate("Main_Dialog", "账号"))
        self.password_2.setText(_translate("Main_Dialog", "密码"))
        self.login_button.setText(_translate("Main_Dialog", "登录"))
        self.logout_button.setText(_translate("Main_Dialog", "退出"))



