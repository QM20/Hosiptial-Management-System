# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'summary_widget.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

class summary_widget(QWidget):
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
        self.table = QtWidgets.QTableWidget(self)
        self.table.setGeometry(QtCore.QRect(10, 80, 811, 351))
        self.table.setObjectName("table")
        #从数据库读数据
        self.table.setColumnCount(7)
        self.table.setRowCount(10)
        for row_number in range(10):
            for col_number in range(7):
                if col_number == 6:
                    self.table.setCellWidget(row_number,col_number,self.button_for_row(row_number))
                else:
                    self.table.setItem(row_number, col_number, QtWidgets.QTableWidgetItem("1111"))


        # logo
        logo = QtGui.QPixmap("logo716.png").scaled(self.logo_lable.width(), self.logo_lable.height())
        self.logo_lable.setPixmap(logo)
        # background
        jpg = QtGui.QPixmap("bg.jpg").scaled(self.background_lable.width(), self.background_lable.height())
        self.background_lable.setPixmap(jpg)
        self.logo_lable.raise_()
        self.table.raise_()


        self.retranslateUi()
    def button_for_row(self,id):
        choose_button = QtWidgets.QPushButton('选择')
        #choose_button.clicked.connect(lambda: self.viewTable(id))


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        #self.background_lable.setText(_translate("Form", "TextLabel"))
        #self.logo_lable.setText(_translate("Form", "TextLabel"))
        self.back_button.setText(_translate("Form", "返回"))


