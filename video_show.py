

import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtWidgets import *
from PySide6.QtMultimediaWidgets import QVideoWidget




class Ui_VideoWindow(object):
    def setupUi(self, VideoWindow):
        if not VideoWindow.objectName():
            VideoWindow.setObjectName(u"VideoWindow")
        VideoWindow.resize(1265, 831)
        self.centralwidget = QWidget(VideoWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        # 输入原始视频（Label）
        self.input_vid = QLabel(self.centralwidget)
        self.input_vid.setObjectName(u"input_vid")
        self.input_vid.setGeometry(QRect(250, 80, 150, 50))
        self.input_vid.setScaledContents(True)
        self.input_vid.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.input_vid.setFont(font)
        self.input_vid.setStyleSheet("color: cyan;")

        # 输出预测视频（Label）
        self.output_vid = QLabel(self.centralwidget)
        self.output_vid.setObjectName(u"output_vid")
        self.output_vid.setGeometry(QRect(855, 80, 150, 50))
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

        self.go_back = QPushButton(self.centralwidget)
        self.go_back.setObjectName(u"go_back")
        self.go_back.setGeometry(QRect(570, 270, 81, 51))

        # 原始视频播放
        self.original_video = QVideoWidget(self.centralwidget)
        self.original_video.setObjectName(u"original_video")
        self.original_video.setGeometry(0, 170, 570, 570)

        # 预测视频播放
        self.predicted_video = QVideoWidget(self.centralwidget)
        self.predicted_video.setObjectName(u"predicted_video")
        self.predicted_video.setGeometry(651, 170, 570, 570)

        # VideoWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(VideoWindow)
        self.statusbar.setObjectName(u"statusbar")


        # 背景图片
        self.background = QLabel(self.centralwidget)
        self.background.setObjectName(u"background")
        self.background.setGeometry(0, 0, 1265, 831)
        self.background.setScaledContents(True)
        self.background.setAlignment(Qt.AlignCenter)

        VideoWindow.setCentralWidget(self.centralwidget)

        VideoWindow.setStatusBar(self.statusbar)

        self.retranslateUi(VideoWindow)

        QMetaObject.connectSlotsByName(VideoWindow)


    # setupUi

    def retranslateUi(self, VideoWindow):
        VideoWindow.setWindowTitle(QCoreApplication.translate("VideoWindow", u"VideoWindow", None))
        self.input_vid.setText(QCoreApplication.translate("VideoWindow", u"\u539f\u59cb\u89c6\u9891", None))
        self.output_vid.setText(QCoreApplication.translate("VideoWindow", u"\u68c0\u6d4b\u7ed3\u679c", None))
        self.select_vid.setText(QCoreApplication.translate("VideoWindow", u"\u9009\u62e9\u89c6\u9891", None))
        self.go_back.setText(QCoreApplication.translate("VideoWindow", u"\u8fd4\u56de\u4e0a\u4e00\u7ea7", None))
        self.start_vid.setText(QCoreApplication.translate("VideoWindow", u"\u5f00\u59cb\u68c0\u6d4b", None))
    # retranslateUi
