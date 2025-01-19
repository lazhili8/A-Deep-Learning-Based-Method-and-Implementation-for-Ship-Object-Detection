import os
import os.path
import numpy as np
import xml.etree.ElementTree as xmlET
from PIL import Image, ImageDraw


def main(mode='normal', pic_name='none'):
    classes = ('__background__',  # always index 0
               'ship')

    file_path_img = 'img_predicted'
    file_path_xml = 'VOCdevkit/VOC2007/Annotations'
    save_file_path = 'img_save'

    jpgName = os.listdir(file_path_img)

    for idx in range(len(jpgName)):
        filename = jpgName[idx].split('.')[0]
        if pic_name == 'none':
            tree = xmlET.parse(file_path_xml + '/' + filename + '.xml')
        else:
            tree = xmlET.parse(file_path_xml + '/' + pic_name.split('.jpg')[0] + '.xml')
        objs = tree.findall('object')
        num_objs = len(objs)
        boxes = np.zeros((num_objs, 5), dtype=np.uint16)

        for ix, obj in enumerate(objs):
            bbox = obj.find('bndbox')
            # Make pixel indexes 0-based
            x1 = float(bbox.find('xmin').text) - 1
            y1 = float(bbox.find('ymin').text) - 1
            x2 = float(bbox.find('xmax').text) - 1
            y2 = float(bbox.find('ymax').text) - 1

            x1 = abs(x1)
            x2 = abs(x2)
            y1 = abs(y1)
            y2 = abs(y2)

            print("box:{} ,{}  {} ,{}".format(x1,y1,x2,y2))

            cla = obj.find('name').text
            label = classes.index(cla)

            boxes[ix, 0:4] = [x1, y1, x2, y2]
            boxes[ix, 4] = label

        image_name = os.path.splitext(filename)[0]
        # img = Image.open(os.path.join(file_path_img, image_name + '.jpg'))
        img = Image.open(file_path_img + '/' + image_name + '.jpg')
        draw = ImageDraw.Draw(img)
        for ix in range(len(boxes)):
            xmin = int(boxes[ix, 0])
            ymin = int(boxes[ix, 1])
            xmax = int(boxes[ix, 2])
            ymax = int(boxes[ix, 3])
            draw.rectangle([xmin, ymin, xmax, ymax], outline=(0, 255, 0))
            # draw.text([xmin, ymin], classes[boxes[ix, 4]], (255, 0, 0))
        if mode == 'normal':
            img.save(os.path.join(save_file_path, image_name + '.jpg'))
        else:
            img.save(save_file_path + '/result.jpg')
