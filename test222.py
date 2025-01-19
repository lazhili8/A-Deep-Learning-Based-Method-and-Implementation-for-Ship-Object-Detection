import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtCore import QUrl

class VideoPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("视频播放器")
        self.setGeometry(100, 100, 800, 600)

        # 创建 QMediaPlayer 实例
        self.media_player = QMediaPlayer(None)

        # 创建 QVideoWidget 实例
        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)

        self.video_widget = QVideoWidget(self.centralwidget)
        self.video_widget.setGeometry(150, 50, 700, 500)

        # 设置视频输出
        self.media_player.setVideoOutput(self.video_widget)

        # 加载视频文件
        video_path = "D:/clown.mp4"  # 将此处的路径替换为你的视频文件路径
        print("kk")
        media_content = QUrl.fromLocalFile(video_path)

        # 设置媒体源
        self.media_player.setSource(media_content)

        # 播放视频
        print("kk")
        self.media_player.play()
        print("kk")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = VideoPlayer()
    player.show()
    sys.exit(app.exec())
