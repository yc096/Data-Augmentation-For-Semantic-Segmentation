import cv2
def scale(img, factor=1,interpolation=1):
    """
    按比例放大或缩小图像.
    :param img:符合Opencv读入格式,unit8类型.
    :param factor: 缩放因子,值范围建议(不强制)在(0,2~]
           1为返回原图
    :param interpolation:
           INTER_NEAREST = 0
           INTER_LINEAR = 1
           INTER_CUBIC = 2
           INTER_AREA = 3
    """
    if factor ==1 :
        return img
    elif factor==0:
        factor=0.1
    img_size_h, img_size_w = img.shape[:2]  # 获取图像尺寸
    img_size_h, img_size_w = int(img_size_h*factor),int(img_size_w*factor)  #按缩放尺寸
    img = cv2.resize(img,(img_size_w,img_size_h),interpolation=interpolation)
    return img