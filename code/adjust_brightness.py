import cv2
import numpy as np
def adjust_brightness(img, factor):
    """
    调整一幅图像的亮度,label不做变换.
    :param img:符合Opencv读入格式,unit8类型.
    :param factor:控制亮度强度.值范围应该在[0,2~].
           0为纯黑图 1为原图
    """
    lut = np.arange(0, 255 + 1) * factor
    lut = np.clip(lut, 0, 255).astype(np.uint8)
    img = cv2.LUT(img, lut)
    return img
