# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.save_Record = QtWidgets.QPushButton(self.centralwidget)
        self.save_Record.setGeometry(QtCore.QRect(630, 530, 100, 30))
        self.save_Record.setObjectName("save_Record")
        self.time = QtWidgets.QLabel(self.centralwidget)
        self.time.setGeometry(QtCore.QRect(20, 10, 150, 30))
        self.time.setObjectName("time")
        self.next_Day = QtWidgets.QPushButton(self.centralwidget)
        self.next_Day.setGeometry(QtCore.QRect(630, 490, 100, 30))
        self.next_Day.setObjectName("next_Day")
        self.set_Food = QtWidgets.QPushButton(self.centralwidget)
        self.set_Food.setGeometry(QtCore.QRect(630, 450, 100, 30))
        self.set_Food.setObjectName("set_Food")
        self.food_Display = QtWidgets.QLabel(self.centralwidget)
        self.food_Display.setGeometry(QtCore.QRect(20, 40, 150, 30))
        self.food_Display.setObjectName("food_Display")
        self.food_Display_Past = QtWidgets.QLabel(self.centralwidget)
        self.food_Display_Past.setGeometry(QtCore.QRect(20, 70, 200, 30))
        self.food_Display_Past.setObjectName("food_Display_Past")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 120, 200, 30))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.appeared_Cat_List = QtWidgets.QLabel(self.centralwidget)
        self.appeared_Cat_List.setGeometry(QtCore.QRect(150, 180, 500, 200))
        self.appeared_Cat_List.setText("")
        self.appeared_Cat_List.setAlignment(QtCore.Qt.AlignCenter)
        self.appeared_Cat_List.setObjectName("appeared_Cat_List")
        self.food_Display_Remain = QtWidgets.QLabel(self.centralwidget)
        self.food_Display_Remain.setGeometry(QtCore.QRect(20, 100, 200, 30))
        self.food_Display_Remain.setObjectName("food_Display_Remain")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "mio"))
        self.save_Record.setText(_translate("MainWindow", "保存游戏进度"))
        self.time.setText(_translate("MainWindow", "这是开学第1周第1天"))
        self.next_Day.setText(_translate("MainWindow", "下一天"))
        self.set_Food.setText(_translate("MainWindow", "猫粮投放量"))
        self.food_Display.setText(_translate("MainWindow", "今天要喂的猫粮量 50"))
        self.food_Display_Past.setText(_translate("MainWindow", "昨天实际喂了的猫粮量 0"))
        self.label.setText(_translate("MainWindow", "昨天出现的猫咪"))
        self.food_Display_Remain.setText(_translate("MainWindow", "协会还剩的猫粮量 10000"))
