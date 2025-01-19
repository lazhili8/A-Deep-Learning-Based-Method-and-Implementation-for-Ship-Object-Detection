import cv2
import os

# 图片文件夹路径
image_folder = 'images'
# 视频文件路径
video_name = 'output_video/output_video.mp4'

# 获取图片文件夹中的所有图片文件
images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]

# 获取第一张图片的宽度和高度
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

# 创建视频对象
video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'mp4v'), 30, (width, height))

# 逐个将图片添加到视频中，每张图片持续1秒
for image in images:
    for _ in range(30):  # 写入30帧同一张图片
        video.write(cv2.imread(os.path.join(image_folder, image)))

# 释放视频对象
video.release()
