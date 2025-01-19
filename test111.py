import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimediaWidgets import QVideoWidget

class VideoPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("视频播放器")
        self.setGeometry(100, 100, 800, 600)

        # 创建 QMediaPlayer 实例
        self.media_player = QMediaPlayer(None)

        # 创建 QVideoWidget 实例
        self.video_widget = QVideoWidget(self)
        self.video_widget.setGeometry(50, 50, 700, 500)

        # 设置视频输出
        self.media_player.setVideoOutput(self.video_widget)

        # 加载视频文件
        video_path = "video/AAA.avi"  # 将此处的路径替换为你的视频文件路径
        media_content = QMediaContent(QUrl.fromLocalFile(video_path))
        self.media_player.setMedia(media_content)

        # 播放视频
        self.media_player.play()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = VideoPlayer()
    player.show()
    sys.exit(app.exec_())
