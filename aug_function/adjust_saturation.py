import cv2
import numpy as np

def is_gray_img(img: np.ndarray):
    return (len(img.shape) == 2) or (len(img.shape) == 3 and img.shape[-1] == 1)

def adjust_saturation(img, factor, gamma=0):
    """
    调整一幅图像的饱和度,label不做变换.
    :param img:符合Opencv读入格式,颜色通道为RGB,unit8类型.
    :param factor:控制饱和度强度.值范围应该在[0,2~].
           0为灰度图 1为原图
    """
    if factor == 1:
        return img

    if is_gray_img(img):
        gray = img
        return gray
    else:
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)

    if factor == 0:
        return gray
    result = cv2.addWeighted(img, factor, gray, 1 - factor, gamma=gamma)
    result = np.clip(result, 0, 255).astype(img.dtype)
    return result

