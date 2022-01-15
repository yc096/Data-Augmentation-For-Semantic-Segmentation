import cv2
import numpy as np


def scale(img, mask, factor=1):
    """
    按比例放大或缩小图像.
    :param img: color-RGB-[H,W,C]
    :param mask:grayscale-[H,W]
    :param factor: 缩放因子,值范围建议(不强制)在(0,2~]
           1为返回原图
    """
    if factor == 1:
        return img, mask
    elif factor <= 0:
        raise ValueError('scale_factor != 0')

    h, w = img.shape[:2]
    new_h, new_w = int(h * factor), int(w * factor)

    # 缩放图像
    img = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_LINEAR)
    mask = cv2.resize(mask, (new_w, new_h), interpolation=cv2.INTER_NEAREST)

    # padding or crop
    x, y = int(np.random.uniform(0, abs(new_w - w))), int(np.random.uniform(0, abs(new_h - h)))

    if factor < 1.0:
        # padding
        img_padding = np.zeros([h, w, 3], dtype=np.uint8)
        img_padding[y:y + new_h, x:x + new_w, :] = img
        mask_padding = np.zeros([h, w], dtype=np.uint8)
        mask_padding[y:y + new_h, x:x + new_w] = mask
        return img_padding, mask_padding
    elif factor > 1.0:
        # crop
        img_crop = img[y:y + h, x:x + w, :]
        mask_crop = mask[y:y + h, x:x + w]
        return img_crop, mask_crop
