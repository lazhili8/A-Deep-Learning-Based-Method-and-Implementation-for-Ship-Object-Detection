# -*- coding: utf-8 -*-
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import *



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        # 输入原始视频（Label，可删除）
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

        # 输出预测视频（Label，可删除）
        self.output_vid = QLabel(self.centralwidget)
        self.output_vid.setObjectName(u"output_vid")
        self.output_vid.setGeometry(QRect(660, 30, 521, 451))
        self.output_vid.setScaledContents(True)
        self.output_vid.setAlignment(Qt.AlignCenter)
        self.output_vid.setFont(font)
        self.output_vid.setStyleSheet("color: cyan;")

        # 选择原始视频
        self.select_vid = QPushButton(self.centralwidget)
        self.select_vid.setObjectName(u"select_vid")
        self.select_vid.setGeometry(QRect(570, 170, 81, 51))

        # 开始预测
        self.start_vid = QPushButton(self.centralwidget)
        self.start_vid.setObjectName(u"start_vid")
        self.start_vid.setGeometry(QRect(570, 220, 81, 51))

        # 原始视频播放
        self.origin_video = QVideoWidget(self.centralwidget)
        self.origin_video.setObjectName(u"origin_video")
        self.origin_video.setGeometry(0, 540, 860, 540)

        # 预测视频播放
        self.predicted_video = QVideoWidget(self.centralwidget)
        self.predicted_video.setObjectName(u"predicted_video")
        self.predicted_video.setGeometry(860, 540, 860, 540)

        # VideoWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")

        # 背景图片
        self.background = QLabel(self.centralwidget)
        self.background.setObjectName(u"background")
        self.background.setGeometry(0, 0, 1920, 1080)
        self.background.setScaledContents(True)
        self.background.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)


    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.input_vid.setText(QCoreApplication.translate("MainWindow", u"\u539f\u59cb\u89c6\u9891", None))
        self.output_vid.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u6d4b\u7ed3\u679c", None))
        self.select_vid.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u89c6\u9891", None))
        self.start_vid.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u68c0\u6d4b", None))
    # retranslateUi




