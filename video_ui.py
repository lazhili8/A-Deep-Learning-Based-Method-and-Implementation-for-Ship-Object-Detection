import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QPixmap
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import *

from video_show_PyQT5 import Ui_MainWindow
import predict_video as pred_video

vid_input_path = ''


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.vid_ui = Ui_MainWindow()
        self.vid_ui.setupUi(self)  # 调用正确的 setupUi 方法

        self.vid_ui.select_vid.clicked.connect(self.openVideo)
        self.vid_ui.start_vid.clicked.connect(self.detVideo)

        # 创建 QMediaPlayer1 实例
        self.media_player_predicted = QMediaPlayer()
        # 设置视频输出
        self.media_player_predicted.setVideoOutput(self.vid_ui.predicted_video)

        # 创建 QMediaPlayer2 实例
        self.media_player_origin = QMediaPlayer()
        # 设置视频输出
        self.media_player_origin.setVideoOutput(self.vid_ui.origin_video)

        self.background = QLabel(self)
        pixmap = QPixmap('background/background.png')
        self.background.setPixmap(pixmap)
        self.background.setGeometry(0, 0, pixmap.width(), pixmap.height())  # 设置 QLabel 大小为图片大小
        self.background.lower()

        # 提升其他部件到前面
        self.vid_ui.select_vid.raise_()
        self.vid_ui.start_vid.raise_()
        self.vid_ui.origin_video.raise_()
        self.vid_ui.predicted_video.raise_()

    def play_predicted(self):
        # 加载视频文件
        print("play")
        video_path = "video_predicted/predicted_video.mp4"
        # self.media_player.setSource(QUrl.fromLocalFile(video_path))
        # QMediaContent(QFileDialog.getOpenFileUrl()[0])
        # print(QFileDialog.getOpenFileUrl()[0])
        # print(type(QFileDialog.getOpenFileUrl()[0]))
        # print(QUrl.fromLocalFile(video_path))
        # print(type(QUrl.fromLocalFile(video_path)))
        media = QMediaContent(QUrl.fromLocalFile(video_path))
        self.media_player_predicted.setMedia(media)


    def play_origin(self):
        # 加载视频文件
        print("play")
        video_path = vid_input_path
        # self.media_player.setSource(QUrl.fromLocalFile(video_path))
        # QMediaContent(QFileDialog.getOpenFileUrl()[0])
        # print(QFileDialog.getOpenFileUrl()[0])
        # print(type(QFileDialog.getOpenFileUrl()[0]))
        # print(QUrl.fromLocalFile(video_path))
        # print(type(QUrl.fromLocalFile(video_path)))
        media = QMediaContent(QUrl.fromLocalFile(video_path))
        self.media_player_origin.setMedia(media)


    def openVideo(self):
        """
        用于打开视频文件，获取文件路径，将路径存入全局变量 vid_input_path
        :return: none
        """
        global vid_input_path
        vid_input_path = QFileDialog.getOpenFileName(self, filter="*.mp4")[0]
        print("原始视频文件路径：{}".format(vid_input_path))

    def detVideo(self):
        print("开始检测视频")
        # 这里需要调用视频检测的函数，将检测结果保存到文件中
        # pred.main_video(_input=vid_input_path, _output='video_predicted/result.mp4')
        # 假设 pred.main_video 是用于视频检测的函数，_input 是视频文件路径，_output 是检测结果保存的路径

        # 检测视频
        pred_video.main(vid_input_path)

        # # 将检测结果显示在界面上的相应标签内
        # self.vid_ui.select_vid.setPixmap(QPixmap('video_predicted/result.jpg'))  # 显示视频第一帧的检测结果
        # self.vid_ui.start_vid.setPixmap(QPixmap('video_save/result.jpg'))  # 显示检测结果保存的图片

        # 播放视频
        main_win.play_predicted()
        main_win.play_origin()
        self.media_player_origin.play()
        self.media_player_predicted.play()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.setWindowTitle("Min_Player")
    main_win.show()
    sys.exit(app.exec())
