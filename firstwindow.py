# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/home/QtProjects/firstwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FirstWindow(object):
    def setupUi(self, FirstWindow):
        FirstWindow.setObjectName("FirstWindow")
        FirstWindow.resize(665, 571)
        self.centralwidget = QtWidgets.QWidget(FirstWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 653, 32))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(140, 60, 390, 32))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(140, 90, 390, 32))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(135, 120, 400, 32))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 510, 101, 32))
        self.pushButton_9.setObjectName("pushButton_9")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 190, 641, 311))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(470, 510, 181, 32))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(10, 160, 151, 32))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(440, 160, 211, 32))
        self.pushButton_12.setObjectName("pushButton_12")
        FirstWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(FirstWindow)
        self.statusbar.setObjectName("statusbar")
        FirstWindow.setStatusBar(self.statusbar)

        self.retranslateUi(FirstWindow)
        QtCore.QMetaObject.connectSlotsByName(FirstWindow)

    def retranslateUi(self, FirstWindow):
        _translate = QtCore.QCoreApplication.translate
        FirstWindow.setWindowTitle(_translate("FirstWindow", "База данных"))
        self.pushButton.setText(_translate("FirstWindow", "Пользователи"))
        self.pushButton_2.setText(_translate("FirstWindow", "Персонажи"))
        self.pushButton_3.setText(_translate("FirstWindow", "Достижения"))
        self.pushButton_4.setText(_translate("FirstWindow", "Локации"))
        self.pushButton_5.setText(_translate("FirstWindow", "Статистика"))
        self.pushButton_6.setText(_translate("FirstWindow", "Круговая диаграмма (количество сыгранных часов)"))
        self.pushButton_7.setText(_translate("FirstWindow", "Столбчатая диаграмма (заработанное золото по дням)"))
        self.pushButton_8.setText(_translate("FirstWindow", "Линейная диаграмма (число побеждённых мобов по дням)"))
        self.pushButton_9.setText(_translate("FirstWindow", "Меню"))
        self.pushButton_10.setText(_translate("FirstWindow", "Сохранить изменения"))
        self.pushButton_11.setText(_translate("FirstWindow", "Добавить элемент"))
        self.pushButton_12.setText(_translate("FirstWindow", "Удалить выбранный элемент"))
