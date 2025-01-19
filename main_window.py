# -*- coding: utf-8 -*-
from PySide6 import QtCore
################################################################################
## Form generated from reading UI file 'main_window.ui'
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setFixedSize(1530,700)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.output1 = QLabel(self.centralwidget)
        self.output1.setObjectName(u"output1")
        self.output1.setGeometry(QRect(1530 - 511, 0, 511, 461))
        font = QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.output1.setFont(font)
        self.output1.setScaledContents(True)
        self.output1.setAlignment(Qt.AlignCenter)
        self.output1.setStyleSheet("color: cyan;")
        self.output2 = QLabel(self.centralwidget)
        self.output2.setObjectName(u"output2")
        self.output2.setGeometry(QRect(510, 220, 511, 461))
        self.output2.setFont(font)
        self.output2.setStyleSheet(u"background-image: url(:/your_resource_prefix/background.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"background-size: cover;\n"
"")
        self.output2.setScaledContents(True)
        self.output2.setAlignment(Qt.AlignCenter)
        self.output2.setStyleSheet("color: cyan;")
        self.input = QLabel(self.centralwidget)
        self.input.setObjectName(u"input")
        self.input.setStyleSheet("color: cyan;")
        self.input.setGeometry(QRect(0, 0, 510, 461))
        self.input.setFont(font)
        self.input.setScaledContents(True)
        self.input.setAlignment(Qt.AlignCenter)
        self.det_image = QPushButton(self.centralwidget)
        self.det_image.setObjectName(u"det_image")
        self.det_image.setGeometry(QRect(750, 170, 71, 51))
        self.open_image = QPushButton(self.centralwidget)
        self.open_image.setObjectName(u"open_image")
        self.open_image.setGeometry(QRect(750, 119, 71, 51))

        # 视频检测按钮
        self.video_detection = QPushButton(self.centralwidget)
        self.video_detection.setObjectName(u"video_detection")
        self.video_detection.setGeometry(QRect(821, 170, 71, 51))

        # 摄像头检测按钮
        self.camera_detection = QPushButton(self.centralwidget)
        self.camera_detection.setObjectName(u"camera_detection")
        self.camera_detection.setGeometry(QRect(821, 119, 71, 51))

        self.background = QLabel(self.centralwidget)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(0, 0, 1530, 700))
        self.background.setScaledContents(True)
        self.background.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.background.raise_()
        self.output1.raise_()
        self.output2.raise_()
        self.input.raise_()
        self.det_image.raise_()
        self.open_image.raise_()
        self.video_detection.raise_()
        self.camera_detection.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u674e\u51ef\u5fd72052520\u6bd5\u4e1a\u8bbe\u8ba1", None))
        self.output1.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u68c0\u6d4b\u7ed3\u679c", None))
        self.output2.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u6d4b\u7ed3\u679c\u4e0e\u539f\u59cb\u56fe\u7247\u76f8\u5bf9\u7167", None))
        self.input.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u539f\u59cb\u56fe\u7247", None))
        self.det_image.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u68c0\u6d4b", None))
        self.open_image.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u56fe\u7247", None))
        self.video_detection.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u9891\u68c0\u6d4b", None))
        self.camera_detection.setText(QCoreApplication.translate("MainWindow", u"\u6444\u50cf\u5934\u68c0\u6d4b", None))
    # retranslateUi


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
