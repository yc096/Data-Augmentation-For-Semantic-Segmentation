import cv2
import numpy as np
def adjust_contrast(img, factor):
    """
    调整一幅图像的对比度
    :param img:符合Opencv读入格式,unit8类型.
    :param factor:控制对比度强度.值范围应该在[0,2~].
           0为纯灰图 1为原图
    """
    lut = np.arange(0, 255 + 1) * factor
    if is_gray_img(img):
        mean = img.mean()
    else:
        mean = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY).mean()
    lut = lut + (1 - factor) * mean
    lut = np.clip(lut, 0, 255).astype(img.dtype)
    img = cv2.LUT(img, lut)
    return img

def is_gray_img(img: np.ndarray):
    return (len(img.shape) == 2) or (len(img.shape) == 3 and img.shape[-1] == 1)