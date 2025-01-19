import os
import numpy as np

def calculate_iou(box1, box2):
    """
    计算两个边界框的交并比（IoU）
    """
    # 计算交集的边界框
    x1 = max(box1[0], box2[0])
    y1 = max(box1[1], box2[1])
    x2 = min(box1[2], box2[2])
    y2 = min(box1[3], box2[3])

    # 计算交集的面积
    intersection_area = max(0, x2 - x1 + 1) * max(0, y2 - y1 + 1)

    # 计算两个边界框的面积
    box1_area = (box1[2] - box1[0] + 1) * (box1[3] - box1[1] + 1)
    box2_area = (box2[2] - box2[0] + 1) * (box2[3] - box2[1] + 1)

    # 计算并集的面积
    union_area = box1_area + box2_area - intersection_area

    # 计算交并比
    iou = intersection_area / union_area

    return iou

def calculate_precision_recall(predictions, targets, iou_threshold=0.5):
    """
    计算Precision、Recall和AP
    """
    true_positives = 0
    false_positives = 0
    false_negatives = 0

    for pred_box in predictions:
        matched = False
        for target_box in targets:
            iou = calculate_iou(pred_box[:-1], target_box[:-1])
            if iou >= iou_threshold and pred_box[-1] == target_box[-1]:
                true_positives += 1
                matched = True
                break
        if not matched:
            false_positives += 1

    false_negatives = len(targets) - true_positives

    precision = true_positives / (true_positives + false_positives)
    recall = true_positives / (true_positives + false_negatives)

    return precision, recall

def calculate_average_precision(predictions, targets, iou_threshold=0.5):
    """
    计算平均精度（AP）
    """
    precisions = []
    recalls = []
    for i in range(len(predictions)):
        precision, recall = calculate_precision_recall(predictions[:i+1], targets, iou_threshold)
        precisions.append(precision)
        recalls.append(recall)

    ap = np.trapz(precisions, recalls)

    return ap

# 读取预测结果和真实标签文件夹中的文件，解析目标框信息
def read_boxes_from_folder(folder_path):
    boxes_list = []
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r') as file:
            boxes = []
            for line in file:
                # 解析每行的目标框信息，假设格式为 "x_min, y_min, x_max, y_max, class_name"
                box_info = line.strip().split(',')
                box = [int(coord) for coord in box_info[:4]] + [box_info[4]]
                boxes.append(box)
            boxes_list.append(boxes)
    return boxes_list

# 示例用法
predictions_folder = "path/to/predictions_folder"
targets_folder = "VOCdevkit/VOC2007/Annotations"

predictions = read_boxes_from_folder(predictions_folder)
targets = read_boxes_from_folder(targets_folder)

# 计算 Precision、Recall 和 AP
precision, recall = calculate_precision_recall(predictions, targets)
ap = calculate_average_precision(predictions, targets)

print("Precision:", precision)
print("Recall:", recall)
print("Average Precision:", ap)
