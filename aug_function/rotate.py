import cv2
def rotate(img, angle, interpolation=1, borderValue=0):
    """
    旋转一副图像(会裁剪)
    :param img:符合Opencv读入格式.
    :param angle:旋转的角度
    :param interpolation:插值方式
           INTER_NEAREST = 0
           INTER_LINEAR = 1
           INTER_CUBIC = 2
           INTER_AREA = 3
            !!interpolation还可以选为WARP_INVERSE_MAP=16,可以进行逆操作.!!
    :param borderValue:边界值,注意对于彩色图边界值应该给的是数组(R,G,B),只给255代表红色(255,0,0)
    """
    img_size_h, img_size_w = img.shape[:2]  # 获取图像尺寸
    cx, cy = int(img_size_w / 2), int(img_size_h / 2)  # 获得图像中心坐标
    M = cv2.getRotationMatrix2D((cx, cy), angle, 1) #获得变换矩阵
    img = cv2.warpAffine(
        img,
        M,
        (img_size_w, img_size_h),
        flags=interpolation,
        borderMode=cv2.BORDER_CONSTANT,
        borderValue=borderValue
    )
    return img
