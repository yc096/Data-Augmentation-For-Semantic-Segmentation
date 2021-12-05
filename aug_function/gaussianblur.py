import cv2
import numpy as np
def gaussianblur(img,ksize=3):
    """
    使用高斯核模糊图像,label不做变换.
    :param img:符合Opencv读入格式,unit8类型.
    :param ksize:高斯模糊核,越大越模糊且只能为奇数.值建议在[3,2k+1~]
    """
    img = cv2.GaussianBlur(img,(ksize,ksize),sigmaX=0)
    return img


