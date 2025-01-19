# -*- coding: utf-8 -*-
from PySide6 import QtCore
################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)


class Ui_LoginWindow(object):
    def __init__(self):
        self.lineEdit_L_password = None
        self.lineEdit_L_account = None

    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(800, 600)
        LoginWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        LoginWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QWidget(LoginWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(360, 110, 300, 400))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 300, 400))
        self.label.setStyleSheet(u"background-color: rgba(16,30,41,240);\n"
"border-radius:10px;")
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 150, 231, 41))
        self.lineEdit.setStyleSheet(u"background-color: rgba(0, 0, 0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(265,255,255,255);\n"
"padding-bottom:7px;\n"
"color:rgba(255,255,255,200)")
        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(30, 220, 231, 41))
        self.lineEdit_2.setStyleSheet(u"background-color: rgba(0, 0, 0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(265,255,255,255);\n"
"padding-bottom:7px;\n"
"color:rgba(255,255,255,200)")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 290, 231, 61))
        self.pushButton.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton:hover{\n"
"background-color:rgba(2,65,118,150);\n"
"color:rgba(255,255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2,65,118,100);\n"
"}\n"
"")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 40, 121, 91))
        self.label_2.setAlignment(Qt.AlignCenter)
        pixmap = QPixmap('photo/photo.png')
        self.label_2.setPixmap(pixmap)


        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"LoginWindow", None))
        self.label.setText("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"\u8d26\u53f7\u540d\u79f0\uff1a", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"\u8d26\u53f7\u5bc6\u7801\uff1a", None))
        self.pushButton.setText(QCoreApplication.translate("LoginWindow", u"\u767b\u5f55", None))
        self.label_2.setText("")
    # retranslateUi

