import cv2
import numpy as np


def normalize(img, mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225), max_pixel=255.0):
    """
    对一副图像进行标准化,,label不做变换.
    标准化公式为:img=(img-mean*max_pixel)/(std*max_pixel)
    :param img: 符合Opencv读入格式,unit8类型.
    :param mean,std:标准化参数,每个通道都要给出.
    :param max_pixel:图像的最大像素值,img值在[0,255],因此会将mean和std变换到这个区间内.
    :return:
    """
    mean = np.array(mean, dtype=np.float32) * max_pixel
    std = np.array(std, dtype=np.float32) * max_pixel

    img = img.astype(np.float32)
    img -= mean[None, None, :]
    img /= std[None, None, :]

    img = img.astype(np.uint8)  # 图像标准化后,RGB数值不一样有大有小、有正有负,但是数据的分布是一直的.因此如果将图像直接转换为unit8或者float查看图像时,图像已经没有观看的价值了.
    return img
