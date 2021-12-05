import cv2
def crop(img, x=0, y=0, crop_size=(256, 256), interpolation=1):
    """
    裁剪一张图片
    :param img:符合Opencv读入格式.
    :param x,y:裁剪框的左上坐标
    :param crop_size:裁剪大小
    :param interpolation:
           INTER_NEAREST = 0
           INTER_LINEAR = 1
           INTER_CUBIC = 2
           INTER_AREA = 3
    """
    img_size_h,img_size_w = img.shape[:2]  # 获取图像尺寸
    dy = y + crop_size[0]  # 裁剪框高度
    dx = x + crop_size[1]  # 裁剪框宽度

    # 判断裁剪框是否越界
    if dy > img_size_h:
        dy = img_size_h
    if dx > img_size_w :
        dx = img_size_w

    if img.ndim == 3:
        result = img[y:dy, x:dx, :]
    else:
        result = img[y:dy, x:dx]

    #裁剪图像resize大小根据情况改变
    result = cv2.resize(result, (crop_size[1],crop_size[0]), interpolation=interpolation)
    return result