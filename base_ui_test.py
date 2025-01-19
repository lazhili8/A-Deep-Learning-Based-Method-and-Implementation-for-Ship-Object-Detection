import sys

import PyQt5
import cv2
import torch
from PyQt5.QtGui import QPalette
from PyQt5.QtMultimedia import QMediaContent
from PyQt5.QtWidgets import QListView
from PySide6.QtCore import QUrl
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog, QWidget, QMessageBox, QPushButton
from PySide6.QtGui import QPixmap, QImage
import predict as pred
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QLabel, QFileDialog
from main_window import  Ui_MainWindow
from login import Ui_LoginWindow
from video_show import Ui_VideoWindow
from camera_show import Ui_CameraWindow
import predict as pred
import predict_video as pred_video
import login

# 定义全局变量
img_input_path = ''
vid_input_path = ''


class CameraWindow(QMainWindow,Ui_CameraWindow):
    def __init__(self):
        super().__init__()
        self.cam_ui = Ui_CameraWindow()
        self.cam_ui.setupUi(self)
        self.play_camera()

        # 创建摄像头对象
        self.cap = cv2.VideoCapture(0)

        # 设置返回按钮点击事件
        self.cam_ui.go_back2.clicked.connect(self.go_Back2)

        # 显示摄像头图像
        #self.show_camera_feed()
        self.background = QLabel(self)
        pixmap = QPixmap('background/background.png')
        self.background.setPixmap(pixmap)
        self.background.setGeometry(0, 0, pixmap.width(), pixmap.height())  # 设置 QLabel 大小为图片大小
        self.background.lower()
        self.show()
    '''def show_camera_feed(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            bytesPerLine = ch * w
            q_img = QImage(frame.data, w, h, bytesPerLine, QImage.Format_RGB888)
            self.ui.label.setPixmap(QPixmap.fromImage(q_img))
            self.ui.label.setScaledContents(True)
        else:
            self.ui.label.setText("Error: Failed to capture frame from camera!")
'''


    def go_Back2(self):
        self.close_camera()
        self.close()
        self.main_window = MainWindow()
        self.main_window.show()

    def play_camera(self):
        # 打开摄像头
        self.cap = cv2.VideoCapture(0)

        while True:
            ret, frame = self.cap.read()
            if ret:
                # 将 OpenCV 图像转换为 Qt 图像
                qt_image = self.convert_cv_to_qt(frame)

                # 设置显示摄像头图像的 QLabel 的图像
                self.show_camera.setPixmap(QPixmap.fromImage(qt_image))

                # 可选：设置 QLabel 根据图像大小自动缩放
                self.show_camera.setScaledContents(True)

    def convert_cv_to_qt(self, frame):
        # 转换颜色通道顺序 BGR -> RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # 获取图像尺寸和通道数
        height, width, channel = frame_rgb.shape

        # 创建 QImage 对象
        qt_image = QImage(frame_rgb.data, width, height, width * channel, QImage.Format_RGB888)

        return qt_image
    def close_camera(self):
        # 释放摄像头对象
        self.cap.release()



class VideoWindow(QMainWindow, Ui_VideoWindow):
    def __init__(self):
        super().__init__()
        self.vid_ui = Ui_VideoWindow()
        self.vid_ui.setupUi(self)  # 调用正确的 setupUi 方法
        #self.model = YourYOLOv7Model()  # 创建你的 YOLOv7 模型实例
        #self.model.load_state_dict(torch.load('model_data/yolov7_weights.pth'))  # 加载权重
        #self.model.eval()  # 将模型设置为评估模式
        self.vid_ui.select_vid.clicked.connect(self.openVideo)
        self.vid_ui.start_vid.clicked.connect(self.detVideo)
        self.vid_ui.go_back.clicked.connect(self.go_Back)

        self.vid_ui.play_button.clicked.connect(self.play)

        # 创建 QMediaPlayer 实例
        self.media_player = QMediaPlayer()
        # 设置视频输出
        self.media_player.setVideoOutput(self.vid_ui.origin_video)



        self.background = QLabel(self)
        pixmap = QPixmap('background/background.png')
        self.background.setPixmap(pixmap)
        self.background.setGeometry(0, 0, pixmap.width(), pixmap.height())  # 设置 QLabel 大小为图片大小
        self.background.lower()

        # 提升其他部件到前面
        self.vid_ui.select_vid.raise_()
        self.vid_ui.start_vid.raise_()
        self.vid_ui.go_back.raise_()
        self.vid_ui.play_button.raise_()
        self.vid_ui.origin_video.raise_()
        self.show()

    '''def load_model(self):
        # 加载模型的代码
        import torch
        from model_data.experimental import attempt_load

        model = attempt_load(weights='model_data/yolov7_weights.pth', map_location=torch.device('cpu'))

        # 如果你想要在 GPU 上加载模型，使用下面的代码：
        # device = torch.device('cuda')  # 使用 GPU
        # model = attempt_load(weights='model_data/yolov7_weights.pth', map_location=device)

        # 检查模型是否成功加载
        if model is not None:
            print("成功加载预训练权重文件。")
        else:
            print("加载预训练权重文件失败，请检查文件路径和模型定义代码。")
        return model
'''


    def play(self):
        # 加载视频文件
        print("play")
        video_path = "video/test3.mp4"
        # self.media_player.setSource(QUrl.fromLocalFile(video_path))
        # QMediaContent(QFileDialog.getOpenFileUrl()[0])
        self.media_player.setMedia(QMediaContent(QFileDialog.getOpenFileUrl()[0]))
        self.media_player.play()
    def openVideo(self):
        """
        用于打开视频文件，获取文件路径，将路径存入全局变量 vid_input_path
        :return: none
        """
        global vid_input_path
        vid_input_path = QFileDialog.getOpenFileName(self, filter="*.mp4")[0]
        print("原始视频文件路径：{}".format(vid_input_path))


        # # 在界面上显示选择的视频文件，例如使用一个 QLabel 组件来显示视频文件路径
        # video = cv2.VideoCapture(vid_input_path)
        # while True:
        #     ret, frame = video.read()
        #     if not ret:
        #         break
        #     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #     qimage = self.video_pred(frame)
        #     self.input_vid.setPixmap(QPixmap(self.convert2QImage(frame)))
        #     self.output.setPixmap(QPixmap.fromImage(qimage))

    ''' def convert2QImage(frame):
        """
        将视频帧转换为 QImage 对象
        :param frame: 视频帧，通常是一个 numpy 数组
        :return: QImage 对象
        """
        height, width, channel = frame.shape
        bytesPerLine = 3 * width
        return QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888)

    def display_video(video_path, label):
        """
        在指定的 QLabel 控件中显示视频
        :param video_path: 视频文件路径
        :param label: QLabel 控件对象
        """
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            print("Error: Unable to open video.")
            return

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # 将视频帧转换为 QImage 对象
            qimage = video_path.convert2QImage(frame)

            # 将 QImage 对象转换为 QPixmap 对象以在 QLabel 中显示
            pixmap = QPixmap.fromImage(qimage)

            # 在 QLabel 中显示视频帧
            label.setPixmap(pixmap)
            label.repaint()
    def video_pred(self,vid_input_path):
        results = self.model(vid_input_path)
        image = results.render()[0]
        return self.convert2QImage(image)
'''
    def detVideo(self):
        print("开始检测视频")
        # 这里需要调用视频检测的函数，将检测结果保存到文件中
        # pred.main_video(_input=vid_input_path, _output='video_predicted/result.mp4')
        # 假设 pred.main_video 是用于视频检测的函数，_input 是视频文件路径，_output 是检测结果保存的路径

        # 检测视频
        pred_video.main(vid_input_path)

        # 将检测结果显示在界面上的相应标签内
        self.vid_ui.select_vid.setPixmap(QPixmap('video_predicted/result.jpg'))  # 显示视频第一帧的检测结果
        self.vid_ui.start_vid.setPixmap(QPixmap('video_save/result.jpg'))  # 显示检测结果保存的图片

        #播放视频
        self.vid_ui.input_vid.setPixmap()


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
        """
        视频检测
        :return:
        """
        # 创建并显示 VideoWindow 实例
        self.video_window = VideoWindow()
        self.close()
        self.video_window.show()

    def camera_detection_clicked(self):
        """
        摄像头检测
        :return:
        """
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

    #win = MainWindow()
    #ui = login.Ui_MainWindow()
    #ui.setupUi(win)
    #win.show()

    sys.exit(app.exec())

