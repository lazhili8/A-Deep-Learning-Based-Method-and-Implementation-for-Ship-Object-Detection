import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QLabel, QFileDialog, QVBoxLayout
from PySide6.QtCore import Slot


class AnotherPage(QWidget):
    def __init__(self, video_path):
        super().__init__()
        self.setWindowTitle("识别后的视频")
        layout = QVBoxLayout()
        label = QLabel(f"展示识别后的视频: {video_path}")
        layout.addWidget(label)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("主窗口")

        # 创建按钮
        self.start_detection_button = QPushButton("开始视频检测")
        self.start_detection_button.clicked.connect(self.open_file_dialog)

        # 设置主窗口布局
        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.start_detection_button)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    @Slot()
    def open_file_dialog(self):
        # 打开文件选择对话框
        file_path, _ = QFileDialog.getOpenFileName(self, "选择视频文件", "", "视频文件 (*.mp4 *.avi)")

        if file_path:
            # 打开另一个界面展示识别后的视频
            self.another_page = AnotherPage(file_path)
            self.another_page.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
