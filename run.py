import cv2
import time

import torchvision.transforms.functional
import numpy as np
from aug_function.crop import crop
from aug_function.adjust_brightness import adjust_brightness
from aug_function.flip import flip
from aug_function.adjust_saturation import adjust_saturation
from aug_function.adjust_contrast import adjust_contrast
from aug_function.scale import scale
from aug_function.gaussianblur import gaussianblur
from aug_function.normalize import normalize,unnormalize
from aug_function.rotate import rotate
from aug_function.copy_paste import copy_paste
def imgShow(IMAGE, WINDOW_NAME=None):
    """
    显示一副图像,该图像符合opencv格式,且颜色通道为RGB.
    图像类型为np.uint8时,值范围[0,255].
    图像类型为np.float32时,值范围[0,1].
    对于彩色图像[3,H,W]
    对于灰度图像[H,W]
    """
    if WINDOW_NAME == None:
        WINDOW_NAME = str(time.time_ns())
    else:
        WINDOW_NAME = str(WINDOW_NAME)

    cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_AUTOSIZE)
    if IMAGE.ndim == 2:
        cv2.imshow(WINDOW_NAME,IMAGE)   #灰度图
    else:
        cv2.imshow(WINDOW_NAME,cv2.cvtColor(IMAGE,cv2.COLOR_RGB2BGR))


image = cv2.imread(r'C:\WorkSpace\Data-Augmentation-For-Semantic-Segmentation\images\image.jpg',1)
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
label = cv2.imread(r'C:\WorkSpace\Data-Augmentation-For-Semantic-Segmentation\images\label.jpg',0)
_,label = cv2.threshold(label,127,255,cv2.THRESH_BINARY)

image2 = cv2.imread(r'C:\WorkSpace\Data-Augmentation-For-Semantic-Segmentation\images\image2.jpg',1)
image2 = cv2.cvtColor(image2,cv2.COLOR_BGR2RGB)
label2 = cv2.imread(r'C:\WorkSpace\Data-Augmentation-For-Semantic-Segmentation\images\label2.jpg',0)
_,label2 = cv2.threshold(label2,127,255,cv2.THRESH_BINARY)

imgShow(image)
imgShow(label)
image,label = scale(image,label,1.45)
imgShow(image)
imgShow(label)
while True:
    cv2.waitKey(100000)

cv2.waitKey(10000000)

# Debug
# import cv2
# img = cv2.imread(r'C:\WorkSpace\Data-Augmentation-For-Semantic-Segmentation\images\image.jpg',1)
# mask = cv2.imread(r'C:\WorkSpace\Data-Augmentation-For-Semantic-Segmentation\images\label.jpg',0)
# cv2.imshow('1',img)
# cv2.imshow('2',mask)
#
# img , mask = RandomScale(scales=(0.5,0.75,1,1.25,1.5))((img,mask))
# cv2.imshow('3',img)
# cv2.imshow('4',mask)
# cv2.waitKey(0)
