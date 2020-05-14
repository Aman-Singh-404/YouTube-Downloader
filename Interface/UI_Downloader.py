# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Desktop/YouTube-Downloader/Interface/Downloader.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(830, 475)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(0, 0, 420, 45))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_1.setFont(font)
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 47, 420, 5))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.thumbnailL = QtWidgets.QLabel(self.centralwidget)
        self.thumbnailL.setGeometry(QtCore.QRect(10, 240, 400, 225))
        self.thumbnailL.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(179, 176, 174);\n"
"border-radius: 2%;\n"
"")
        self.thumbnailL.setAlignment(QtCore.Qt.AlignCenter)
        self.thumbnailL.setObjectName("thumbnailL")
        self.statusL = QtWidgets.QLabel(self.centralwidget)
        self.statusL.setGeometry(QtCore.QRect(430, 320, 380, 25))
        self.statusL.setObjectName("statusL")
        self.progressPB = QtWidgets.QProgressBar(self.centralwidget)
        self.progressPB.setGeometry(QtCore.QRect(440, 355, 360, 25))
        self.progressPB.setProperty("value", 0)
        self.progressPB.setObjectName("progressPB")
        self.streamsTW = QtWidgets.QTreeWidget(self.centralwidget)
        self.streamsTW.setGeometry(QtCore.QRect(420, 10, 400, 300))
        self.streamsTW.setObjectName("streamsTW")
        self.streamsTW.headerItem().setTextAlignment(0, QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.streamsTW.headerItem().setFont(0, font)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setEnabled(False)
        self.label_3.setGeometry(QtCore.QRect(5, 120, 160, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.directoryL = QtWidgets.QLabel(self.centralwidget)
        self.directoryL.setEnabled(False)
        self.directoryL.setGeometry(QtCore.QRect(10, 155, 400, 30))
        self.directoryL.setAutoFillBackground(False)
        self.directoryL.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px inset rgb(179, 176, 174);\n"
"border-radius: 2%;\n"
"")
        self.directoryL.setText("")
        self.directoryL.setObjectName("directoryL")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(5, 50, 160, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.urlLE = QtWidgets.QLineEdit(self.centralwidget)
        self.urlLE.setGeometry(QtCore.QRect(10, 85, 400, 30))
        self.urlLE.setObjectName("urlLE")
        self.loadurlPB = QtWidgets.QPushButton(self.centralwidget)
        self.loadurlPB.setGeometry(QtCore.QRect(140, 200, 120, 30))
        self.loadurlPB.setObjectName("loadurlPB")
        self.cancelPB = QtWidgets.QPushButton(self.centralwidget)
        self.cancelPB.setGeometry(QtCore.QRect(10, 200, 120, 30))
        self.cancelPB.setObjectName("cancelPB")
        self.downloadPB = QtWidgets.QPushButton(self.centralwidget)
        self.downloadPB.setEnabled(False)
        self.downloadPB.setGeometry(QtCore.QRect(270, 200, 140, 30))
        self.downloadPB.setObjectName("downloadPB")
        self.messageL = QtWidgets.QLabel(self.centralwidget)
        self.messageL.setGeometry(QtCore.QRect(440, 390, 360, 75))
        self.messageL.setText("")
        self.messageL.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.messageL.setWordWrap(True)
        self.messageL.setObjectName("messageL")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_1.setText(_translate("MainWindow", "YouTube Download"))
        self.thumbnailL.setText(_translate("MainWindow", "Thumbnail Preview"))
        self.statusL.setText(_translate("MainWindow", "Progress Status:"))
        self.streamsTW.headerItem().setText(0, _translate("MainWindow", "Streams"))
        self.label_3.setText(_translate("MainWindow", "Enter directory path:"))
        self.label_2.setText(_translate("MainWindow", "Enter YouTube URL:"))
        self.loadurlPB.setText(_translate("MainWindow", "Load URL"))
        self.cancelPB.setText(_translate("MainWindow", "Cancel"))
        self.downloadPB.setText(_translate("MainWindow", "Download stream(s)"))
