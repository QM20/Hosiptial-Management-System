import sys
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt,QCoreApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from caoqiming.login import Ui_Main_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
import time
class mwindow(QWidget, Ui_Main_Dialog):
    def __init__(self):
        super().__init__()
        #super(mwindow, self).__init__()
        self.setupUi(self)
        self.stack = []
        self.stack.append(self.Login_widget)
        self.logistic_cn()
        self.setWindowFlags(Qt.FramelessWindowHint)  # 去掉标题栏的代码

        self.show()

    def logistic_cn(self):
        self.logout_button.clicked.connect(QCoreApplication.instance().quit)
        self.login_button.clicked.connect(self.show_function_widget)
        self.function_widget.back_button.clicked.connect(self.back)
        self.function_widget.capture_button.clicked.connect(self.show_capture_widget)
        self.function_widget.train_button.clicked.connect(self.show_face_rec_widget)
        self.function_widget.history_button.clicked.connect(self.show_history_widget)
        #self.function_widget.setting_button.clicked.connect()
        self.capture_widget.back_button.clicked.connect(self.back)
        self.capture_widget.record_button.clicked.connect(self.judge_face)
        self.capture_widget.clear_button.clicked.connect(self.clear_line)
        self.face_rec_widget.back_button.clicked.connect(self.back)
        self.face_rec_widget.check_button.clicked.connect(self.check_face_right)
        self.face_rec_widget.recheck_button.clicked.connect(self.recheck_face)
        self.train_widget.back_button.clicked.connect(self.back)
        self.train_widget.next_button.clicked.connect(self.show_next)
        self.train_widget.summary_button.clicked.connect(self.show_summary_widget)
        self.train_widget.exit_train_button.clicked.connect(self.exit_system)
        self.summary_widget.back_button.clicked.connect(self.back)


    def back(self):
        self.stack[-1].close()
        self.stack.pop()
        self.stack[-1].show()
    #人员录入页
    def judge_face(self):
        #进行实时opencv人脸识别，框出人脸
        #框出后读取框内信息，若错误则弹框
        #进行分析，并存储进入数据库
        pass
    def clear_line(self):
        #清空两个输入框
        pass


    def recheck_face(self):
        pass




    def show_function_widget(self):
        self.stack[-1].close()
        self.stack.append(self.function_widget)
        self.stack[-1].show()

    def show_capture_widget(self):
        self.stack[-1].close()
        self.stack.append(self.capture_widget)
        self.stack[-1].show()
    def show_face_rec_widget(self):
        self.stack[-1].close()
        self.stack.append(self.face_rec_widget)
        self.stack[-1].show()

    def check_face_right(self):
        self.stack[-1].close()
        self.stack.append(self.train_widget)
        self.stack[-1].show()
        self.train_widget.begin_record()




    def show_history_widget(self):
        pass

    # 训练页
    def show_next(self):
        self.stack[-1].close()
        self.stack.pop()
        self.stack[-1].show()

    def show_summary_widget(self):
        self.stack[-1].close()
        self.stack.append(self.summary_widget)
        self.stack[-1].show()
        for row_number in range(10):
            for col_number in range(7):
                if col_number == 6:
                    self.summary_widget.table.setCellWidget(row_number,col_number,self.button_for_row(row_number))
                else:
                    self.summary_widget.table.setItem(row_number, col_number, QtWidgets.QTableWidgetItem("1111"))

    def button_for_row(self,row_number):
        self.summary_widget.choose_button = QtWidgets.QPushButton('选择')
        self.summary_widget.choose_button.clicked.connect(lambda: self.view_each_picture(row_number))


    def view_each_picture(self,row_number):
        pass

    def exit_system(self):
        self.stack[-1].close()
        self.stack=self.stack[0:1]
        self.stack[0].show()







    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_drag:
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False
        self.setCursor(QCursor(Qt.ArrowCursor))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = mwindow()
    sys.exit(app.exec_())