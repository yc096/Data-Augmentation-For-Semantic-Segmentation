import cv2
##为了保持与其他函数的一致性
def resize(img,height,width,interpolation=1):
    """

    :param img: input image
    :param height:  resize_h
    :param width:   resize_w
    :param interpolation:
           INTER_NEAREST = 0
           INTER_LINEAR = 1
           INTER_CUBIC = 2
           INTER_AREA = 3
    :return:a resized image with specified height and width
    """
    return cv2.resize(img,(width,height),interpolation=interpolation)