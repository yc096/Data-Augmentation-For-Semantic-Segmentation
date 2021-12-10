import cv2
import numpy as np
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
        raise ValueError('scale_factor != 0')

    h, w = img.shape[:2]
    new_h,new_w = int(h * factor) , int(w * factor)

    #缩放图像
    img = cv2.resize(img,(new_w,new_h),interpolation=interpolation)

    # padding or crop
    x, y = int(np.random.uniform(0, abs(new_w - w))), int(np.random.uniform(0, abs(new_h - h)))

    if factor < 1.0:
        # padding
        if img.ndim == 3:
            img_padding = np.zeros([h, w, 3], dtype=np.uint8)
            img_padding[y:y + new_h, x:x + new_w, :] = img
            return img_padding
        elif img.ndim == 2:
            img_padding = np.zeros([h, w], dtype=np.uint8)
            img_padding[y:y + new_h, x:x + new_w] = img
            return img_padding
    elif factor > 1.0:
        # crop
        if img.ndim == 3:
            img_crop = img[y:y + h, x:x + w, :]
            return img_crop
        elif img.ndim == 2:
            img_crop = img[y:y + h, x:x + w]
            return img_crop

