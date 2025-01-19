# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PySide_UI.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QMainWindow,
                               QMenuBar, QPushButton, QSizePolicy, QStatusBar,
                               QWidget)


class Ui_CameraWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1265, 831)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(207, 0, 851, 571))
        self.label.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(217, 590, 291, 130))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(759, 590, 291, 130))
        self.go_back2 = QPushButton(self.centralwidget)
        self.go_back2.setObjectName(u"go_back2")
        self.go_back2.setGeometry(QRect(508, 655, 251, 65))
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(508, 590, 251, 65))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 850, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, CameraWindow):
        CameraWindow.setWindowTitle(QCoreApplication.translate("CameraWindow", u"MainWindow", None))
        self.label.setText("")
        self.pushButton.setText(QCoreApplication.translate("CameraWindow", u"\u6253\u5f00\u6444\u50cf\u5934", None))
        self.pushButton_2.setText(QCoreApplication.translate("CameraWindow", u"\u5173\u95ed\u6444\u50cf\u5934", None))
        self.go_back2.setText(QCoreApplication.translate("CameraWindow", u"\u8fd4\u56de\u4e0a\u4e00\u7ea7", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("CameraWindow", u"\u7b14\u8bb0\u672c\u6444\u50cf\u5934",
                                                                None))
        self.comboBox.setItemText(1, QCoreApplication.translate("CameraWindow", u"\u5916\u7f6e\u6444\u50cf\u5934", None))

    # retranslateUi
