import sys
import time

import cv2
import torch

from PySide6.QtCore import QUrl, QTimer
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog, QWidget, QMessageBox, QPushButton
from PySide6.QtGui import QPixmap, QImage, Qt
import predict as pred
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QLabel, QFileDialog
from main_window import  Ui_MainWindow
from login import Ui_LoginWindow
from video_show import Ui_VideoWindow
from camera_show import Ui_CameraWindow

import predict_video as pred_video
import predict_camera as pred_camera
import login
img_input_path = ''
vid_input_path = ''
Err_video_path = 'error_video/clown.mp4'
ErrMedia = QUrl.fromLocalFile(Err_video_path)
cam_input_path = 0

class CameraWindow(QMainWindow, Ui_CameraWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cam_ui = Ui_CameraWindow()


        self.background = QLabel(self)
        pixmap = QPixmap('background/background.png')
        self.background.setPixmap(pixmap)
        self.background.setGeometry(0, 0, pixmap.width(), pixmap.height())  # 设置 QLabel 大小为图片大小
        self.background.lower()
        self.cap = cv2.VideoCapture()
        self.button_set()

        '''
        图像显示主要用到了QTimer这个Qt中的计时器组件:
        instance = QTimer(widget)  # 初始化生成计时器实例
        instance.start(timeout)  # 每 timeout 时间后在父组件的基础上发出一个计时信号
        instance.timeout.connect(self.show_picture)  # 我们可以设计一个槽函数用于不断接收这个计时信号，从而实现图像帧的不断显示
        instance.stop  # 关闭计时器
        '''
        self.timer = QTimer(self)
        #self.timer.timeout.connect(self.show_picture)

    '''
    槽函数，该槽函数用于接收及处理 “打开摄像头” 按钮发来的按钮信号
    '''

    def open_camera(self):
        number = self.comboBox.currentIndex()  # 获取当前复选框的索引值，其是依次排列的0、1、2、...
        flag = self.cap.open(number)  # 打开指定的摄像头，若成功打开，该函数会返回 Ture、否之则返回False
        if flag is False:
            QMessageBox.information(self, "警告", "该设备未正常工作", QMessageBox.Ok)
        else:
            self.label.setEnabled(True)  # 此句可删
            self.pushButton.setEnabled(False)
            self.pushButton_2.setEnabled(True)
            self.timer.start()  # Qt计时器开始运行，不断的发出计时信号，不断的跳入到show_pic槽函数中，不断的显示图像

    def detCamera(self):
        print("开始检测摄像头")
        pred_camera.main()  # 执行摄像头检测的操作

    def go_Back2(self):
        self.close()
        self.main_window = MainWindow()
        self.main_window.show()
    def button_set(self):
        #self.pushButton.clicked.connect(self.open_camera)
        #self.pushButton_2.clicked.connect(self.close_camera)
        self.pushButton_3.clicked.connect(self.detCamera)  # 将按钮与 detCamera 方法关联起来
        self.go_back2.clicked.connect(self.go_Back2)
        #self.pushButton.setEnabled(True)
        #self.pushButton_2.setEnabled(False)
    '''
    槽函数，该槽函数用于接收及处理 “关闭摄像头” 按钮发来的按钮信号
    '''
'''
    def close_camera(self):
        self.cap.release()  # 释放摄像头对象
        self.pushButton.setEnabled(True)
        self.pushButton_2.setEnabled(False)
        self.timer.stop()  # 停止计时器，不再显示图像帧
        self.label.setText(" ")  # 清空Label，使之重回黑屏状态
    '''




'''
    def show_picture(self):
        ret, frame = self.cap.read()
        if ret:
            if frame is not None:
                cur_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                height, width = cur_frame.shape[:2]  # cur_frame=会返回图像的高、宽与颜色通道数，截前2
                
                #QImage用于访问、转化图像格式操作图像等,其返回值是一个已经转化好格式的QImage对象。
                #QImage支持格式枚举描述的几种图像格式，包括单色、8位、32位和alpha混合图像。当然也包括Opencv的 mat 类型数组枚举形式
                #格式: QImage(枚举对象图像帧,宽,高,转化成的颜色格式)
                
                pixmap = QImage(cur_frame, width, height, QImage.Format_RGB888)
                
                #QPixmap用于在屏幕上显示图像, 其返回值是一个QPixmap对象
                #QPixmap.fromImage函数用于将QImage对象转化为QPixmap对象，注意QPixmap并非一个图像帧，而是Qt中用于图像展示的一个类对象实例
                #其本身也是一种抽象的封装，可被Qt中其他的类对象进行图像显示操作。
                
                pixmap = QPixmap.fromImage(pixmap)
                # 获取是视频流和 label 窗口的长宽比值的最大值，适应label窗口播放，不然显示不全
                ratio = max(width / self.label.width(), height / self.height())
                pixmap.setDevicePixelRatio(ratio)  # 以适应比例将图像帧置入 Label 中进行播放
                # 视频流置于label中间部分播放
                self.label.setAlignment(Qt.AlignCenter)
                self.label.setPixmap(pixmap)
'''


class VideoWindow(QMainWindow, Ui_VideoWindow):
    global Err_video_path
    def __init__(self):
        super().__init__()

        self.vid_ui = Ui_VideoWindow()
        self.vid_ui.setupUi(self)  # 调用正确的 setupUi 方法

        self.vid_ui.select_vid.clicked.connect(self.openVideo)
        self.vid_ui.start_vid.clicked.connect(self.detVideo)

        # 创建 QMediaPlayer1 实例
        self.media_player_predicted = QMediaPlayer()
        # 设置视频输出
        self.media_player_predicted.setVideoOutput(self.vid_ui.predicted_video)

        # 创建 QMediaPlayer2 实例
        self.media_player_original = QMediaPlayer()
        # 设置视频输出
        self.media_player_original.setVideoOutput(self.vid_ui.original_video)

        self.vid_ui.go_back.clicked.connect(self.go_Back)

        self.background = QLabel(self)
        pixmap = QPixmap('background/background.png')
        self.background.setPixmap(pixmap)
        self.background.setGeometry(0, 0, pixmap.width(), pixmap.height())  # 设置 QLabel 大小为图片大小
        self.background.lower()

        # 提升其他部件到前面
        self.vid_ui.select_vid.raise_()
        self.vid_ui.start_vid.raise_()
        self.vid_ui.original_video.raise_()
        self.vid_ui.predicted_video.raise_()
        self.vid_ui.go_back.raise_()


    def openVideo(self):
        """
        用于打开视频文件，获取文件路径，将路径存入全局变量 vid_input_path
        :return: none
        """
        global vid_input_path
        vid_input_path = QFileDialog.getOpenFileName(self, filter="*.mp4 *.avi")[0]
        print("原始视频文件路径：{}".format(vid_input_path))
        # 在界面上显示选择的视频文件，例如使用一个 QLabel 组件来显示视频文件路径
        '''video = cv2.VideoCapture(vid_input_path)
        while True:
            ret, frame = video.read()
            if not ret:
                break
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            qimage = self.video_pred(frame)
            self.input_vid.setPixmap(QPixmap(self.convert2QImage(frame)))
            self.output.setPixmap(QPixmap.fromImage(qimage))
'''
    def detVideo(self):
        print("开始检测视频")
        # 停止播放视频
        self.media_player_original.stop()
        self.media_player_predicted.stop()
        self.media_player_original.setSource(ErrMedia)
        self.media_player_predicted.setSource(ErrMedia)
        # 这里需要调用视频检测的函数，将检测结果保存到文件中
        # pred.main_video(_input=vid_input_path, _output='video_predicted/result.mp4')
        # 假设 pred.main_video 是用于视频检测的函数，_input 是视频文件路径，_output 是检测结果保存的路径
        # 检测视频
        pred_video.main(vid_input_path)
        # 将检测结果显示在界面上的相应标签内
        # self.vid_ui.select_vid.setPixmap(QPixmap('video_predicted/result.jpg'))  # 显示视频第一帧的检测结果
        # self.vid_ui.start_vid.setPixmap(QPixmap('video_save/result.jpg'))  # 显示检测结果保存的图片

        time.sleep(1)

        # 加载原始视频
        self.play_original()
        # 加载预测视频
        self.play_predicted()

        # 播放视频
        print("开始播放原始视频")
        self.media_player_original.play()
        print("开始播放预测视频")
        self.media_player_predicted.play()


    def play_predicted(self):
        # 加载预测视频文件
        print("play predicted")
        video2_path = "video_predicted/predicted_video.mp4"
        media2 = QUrl.fromLocalFile(video2_path)
        # 设置媒体源
        self.media_player_predicted.setSource(media2)
    def play_original(self):
        # 加载原始视频文件
        print("play original")
        video1_path = vid_input_path
        media1 = QUrl.fromLocalFile(video1_path)
        # 设置媒体源
        self.media_player_original.setSource(media1)


    def go_Back(self):
        self.close()  # 关闭当前窗口
        self.main_window = MainWindow()  # 创建主窗口实例
        self.main_window.show()  # 显示主窗口


class LoginWindow(QWidget,Ui_LoginWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.login_in)

        self.show()

    def login_in(self):
        account = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        if account == "lkz" and password == "123456":
            self.win = MainWindow()
            self.close()
        else:
            print("用户名或密码错误哦")



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.bind_slots()
        self.background.setPixmap(QPixmap('background/background.png'))
        self.show()



    def detImage(self):
        print("开始检测")
        pred.main(_input=img_input_path)
        self.output1.setPixmap(QPixmap('img_predicted/result.jpg'))
        self.output2.setPixmap(QPixmap('img_save/result.jpg'))

    def openImage(self):
        """
        用于打开图片，获取文件路径，将路径存入全局变量 img_input_path
        :return: none
        """
        global img_input_path
        img_input_path = QFileDialog.getOpenFileName(self, filter="*.jpg")[0]
        print("原始图像文件路径：{}".format(img_input_path))
        self.input.setPixmap(QPixmap(img_input_path))

    def bind_slots(self):
        self.det_image.clicked.connect(self.detImage)
        self.open_image.clicked.connect(self.openImage)
        self.video_detection.clicked.connect(self.video_detection_clicked)# 绑定视频检测按钮的点击事件到槽函数
        self.camera_detection.clicked.connect(self.camera_detection_clicked)  # 绑定摄像头检测按钮的点击事件到槽函数
    def video_detection_clicked(self):
        # 创建并显示 VideoWindow 实例
        self.video_window = VideoWindow()
        self.close()
        self.video_window.show()

    def camera_detection_clicked(self):
        # 创建并显示 CameraWindow 实例
        self.camera_window = CameraWindow()
        self.close()
        self.camera_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    #login_in = Ui_MainWindow()
    win = LoginWindow()
    #ui = login.Ui_LoginWindow()
    #ui.setupUi(win)
    #win.show()
    #video_win = VideoWindow()

    #win = MainWindow()
    #ui = login.Ui_MainWindow()
    #ui.setupUi(win)
    #win.show()


    sys.exit(app.exec())

