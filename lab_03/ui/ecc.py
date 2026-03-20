# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 0, 120, 30))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 60, 100, 20))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 160, 100, 20))
        self.label_3.setObjectName("label_3")

        # ✅ FIX NAME
        self.btnGenerate = QtWidgets.QPushButton(self.centralwidget)
        self.btnGenerate.setGeometry(QtCore.QRect(450, 10, 120, 30))
        self.btnGenerate.setObjectName("btnGenerate")

        self.btnSign = QtWidgets.QPushButton(self.centralwidget)
        self.btnSign.setGeometry(QtCore.QRect(190, 390, 100, 30))
        self.btnSign.setObjectName("btnSign")

        self.btnVerify = QtWidgets.QPushButton(self.centralwidget)
        self.btnVerify.setGeometry(QtCore.QRect(440, 390, 100, 30))
        self.btnVerify.setObjectName("btnVerify")

        # ✅ FIX NAME
        self.txtMessage = QtWidgets.QTextEdit(self.centralwidget)
        self.txtMessage.setGeometry(QtCore.QRect(120, 50, 471, 80))
        self.txtMessage.setObjectName("txtMessage")

        self.txtSignature = QtWidgets.QTextEdit(self.centralwidget)
        self.txtSignature.setGeometry(QtCore.QRect(120, 140, 471, 80))
        self.txtSignature.setObjectName("txtSignature")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "ECC"))

        self.label.setText(_translate("MainWindow", "ECC Cipher"))
        self.label_2.setText(_translate("MainWindow", "Message"))
        self.label_3.setText(_translate("MainWindow", "Signature"))

        self.btnGenerate.setText(_translate("MainWindow", "Generate Keys"))
        self.btnSign.setText(_translate("MainWindow", "Sign"))
        self.btnVerify.setText(_translate("MainWindow", "Verify"))