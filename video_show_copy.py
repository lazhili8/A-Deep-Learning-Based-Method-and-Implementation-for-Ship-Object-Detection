# -*- coding: utf-8 -*-
from PyQt5.QtMultimedia import QMediaContent
from PySide6 import QtCore
from PySide6.QtMultimedia import QMediaPlayer
################################################################################
## Form generated from reading UI file 'video_show.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
                               QSizePolicy, QStatusBar, QWidget)


class Ui_VideoWindow(object):
    def setupUi(self, VideoWindow):
        if not VideoWindow.objectName():
            VideoWindow.setObjectName(u"MainWindow")
        VideoWindow.resize(1265, 831)
        VideoWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        VideoWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QWidget(VideoWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.input_vid = QLabel(self.centralwidget)
        self.input_vid.setObjectName(u"input_vid")
        self.input_vid.setGeometry(QRect(40, 30, 521, 451))
        self.input_vid.setScaledContents(True)
        self.input_vid.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.input_vid.setFont(font)
        self.input_vid.setStyleSheet("color: cyan;")
        self.output_vid = QLabel(self.centralwidget)
        self.output_vid.setObjectName(u"output_vid")
        self.output_vid.setGeometry(QRect(660, 30, 521, 451))
        self.output_vid.setScaledContents(True)
        self.output_vid.setAlignment(Qt.AlignCenter)
        self.output_vid.setFont(font)
        self.output_vid.setStyleSheet("color: cyan;")
        self.select_vid = QPushButton(self.centralwidget)
        self.select_vid.setObjectName(u"select_vid")
        self.select_vid.setGeometry(QRect(570, 170, 81, 51))
        self.start_vid = QPushButton(self.centralwidget)
        self.start_vid.setObjectName(u"start_vid")
        self.start_vid.setGeometry(QRect(570, 220, 81, 51))
        self.go_back = QPushButton(self.centralwidget)
        self.go_back.setObjectName(u"go_back")
        self.go_back.setGeometry(QRect(570, 270, 81, 51))
        VideoWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(VideoWindow)
        self.statusbar.setObjectName(u"statusbar")




        self.background = QLabel(self.centralwidget)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(0, 0, 1530, 700))
        self.background.setScaledContents(True)
        self.background.setAlignment(Qt.AlignCenter)
        VideoWindow.setCentralWidget(self.centralwidget)

        self.input_vid.raise_()
        self.output_vid.raise_()
        self.select_vid.raise_()
        self.start_vid.raise_()
        self.go_back.raise_()

        VideoWindow.setStatusBar(self.statusbar)

        self.retranslateUi(VideoWindow)

        QMetaObject.connectSlotsByName(VideoWindow)

    # setupUi

    def retranslateUi(self, VideoWindow):
        VideoWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.input_vid.setText(QCoreApplication.translate("MainWindow", u"\u539f\u59cb\u89c6\u9891", None))
        self.output_vid.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u6d4b\u7ed3\u679c", None))
        self.select_vid.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u89c6\u9891", None))
        self.start_vid.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u68c0\u6d4b", None))
        self.go_back.setText(QCoreApplication.translate("MainWindow", u"\u8fd4\u56de\u4e0a\u4e00\u7ea7", None))
    # retranslateUi
