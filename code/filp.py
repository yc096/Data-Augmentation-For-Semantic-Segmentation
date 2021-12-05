import cv2
def filp(img, mode=1):
    """
    翻转一副图像
    :param img:符合Opencv读入格式,颜色通道为RGB,unit8类型.
    :param mode: 0垂直翻转 1水平翻转 -1垂直水平翻转
    """
    return cv2.flip(img, mode)