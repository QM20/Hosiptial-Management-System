# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'train_widget.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import *
from PyQt5.QtGui  import *
import time
import cv2
class train_widget(QWidget):
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
        self.capture_lable.setText("")
        self.capture_lable.setObjectName("capture_lable")


        self.title_lable1 = QtWidgets.QLabel(self)
        self.title_lable1.setGeometry(QtCore.QRect(220, 60, 101, 18))
        self.title_lable1.setObjectName("title_lable1")
        self.title_lable2 = QtWidgets.QLabel(self)
        self.title_lable2.setGeometry(QtCore.QRect(680, 60, 81, 18))
        self.title_lable2.setObjectName("title_lable2")
        self.real_time_label = QtWidgets.QLabel(self)
        self.real_time_label.setGeometry(QtCore.QRect(0, 90, 531, 331))
        self.real_time_label.setObjectName("real_time_label")
        self.next_button = QtWidgets.QPushButton(self)
        self.next_button.setGeometry(QtCore.QRect(530, 440, 80, 26))
        self.next_button.setObjectName("next_button")
        self.summary_button = QtWidgets.QPushButton(self)
        self.summary_button.setGeometry(QtCore.QRect(630, 440, 80, 26))
        self.summary_button.setObjectName("summary_button")
        self.exit_train_button = QtWidgets.QPushButton(self)
        self.exit_train_button.setGeometry(QtCore.QRect(740, 440, 80, 26))
        self.exit_train_button.setObjectName("exit_train_button")
        self.table = QtWidgets.QTableWidget(self)
        self.table.setGeometry(QtCore.QRect(580, 80, 256, 351))
        self.table.setObjectName("table")
        self.table.setColumnCount(2)
        self.table.setRowCount(9)

        for i in range(9):

            self.table.setRowHeight(i,50)
        self.table.setColumnWidth(0, 130)
        self.table.setColumnWidth(1, 130)
        self.table.setItem(0, 0, QTableWidgetItem("姓名"))
        self.table.setItem(1, 0, QTableWidgetItem("班级"))
        self.table.setItem(2, 0, QTableWidgetItem("起跳速度"))
        self.table.setItem(3, 0, QTableWidgetItem("扣分原因"))
        self.table.setItem(4, 0, QTableWidgetItem("扣分分数"))
        self.table.setItem(5, 0, QTableWidgetItem("指导意见"))
        self.table.setItem(6, 0, QTableWidgetItem("训练日期"))
        self.table.setItem(7, 0, QTableWidgetItem("总得分"))
        self.table.setItem(8, 0, QTableWidgetItem("合格与否"))
        self.table.verticalHeader().hide()
        self.table.horizontalHeader().hide()



        # logo
        logo = QtGui.QPixmap("logo716.png").scaled(self.logo_lable.width(), self.logo_lable.height())
        self.logo_lable.setPixmap(logo)
        # background
        jpg = QtGui.QPixmap("bg.jpg").scaled(self.background_lable.width(), self.background_lable.height())
        self.background_lable.setPixmap(jpg)
        # video
        video = QtGui.QPixmap("分析.jpg").scaled(self.real_time_label.width(), self.real_time_label.height())
        self.real_time_label.setPixmap(video)

        self.back_button.raise_()
        self.title_lable1.raise_()
        self.title_lable2.raise_()
        self.next_button.raise_()
        self.summary_button.raise_()
        self.exit_train_button.raise_()




        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        # self.background_lable.setText(_translate("Form", "TextLabel"))
        # self.logo_lable.setText(_translate("Form", "TextLabel"))
        self.back_button.setText(_translate("Form", "返回"))
        self.title_lable1.setText(_translate("Form", "实时视频分析"))
        self.title_lable2.setText(_translate("Form", "本次训练结果"))
        # self.real_time_label.setText(_translate("Form", "TextLabel"))
        self.next_button.setText(_translate("Form", "下一位"))
        self.summary_button.setText(_translate("Form", "训练总结"))
        self.exit_train_button.setText(_translate("Form", "退出训练"))

    def begin_record(self):
        #从视频读到帧，进行姿态分析，一帧帧写入lable
        #判断起跳起始与结束
        #在结束动作后，计算得分set右边的框
        #停止读视频，函数结束
        self.table.setItem(0, 1, QTableWidgetItem("李强"))
        self.table.setItem(1, 1, QTableWidgetItem("2班"))
        self.table.setItem(2, 1, QTableWidgetItem("5m/s"))
        self.table.setItem(3, 1, QTableWidgetItem("腿部与地面没有平行"))
        self.table.setItem(4, 1, QTableWidgetItem("-3"))
        self.table.setItem(5, 1, QTableWidgetItem("XXXXXXXX"))
        self.table.setItem(6, 1, QTableWidgetItem("2019年4月7日"))
        self.table.setItem(7, 1, QTableWidgetItem("97"))
        self.table.setItem(8, 1, QTableWidgetItem("是"))




        pass

