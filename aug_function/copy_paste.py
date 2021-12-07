# paper ---> https://arxiv.org/pdf/2012.07177.pdf
# 简介参考 https://my.oschina.net/u/4580264/blog/4812710    or  https://blog.csdn.net/oYeZhou/article/details/111696577
# 参考代码 https://github.com/qq995431104/Copy-Paste-for-Semantic-Segmentation/blob/main/copy_paste.py
# 1.随机选择两幅训练图像
# 3.随机水平翻转
# 2.随机尺度抖动缩放
# 4.随机选择一幅图像中的目标子集
# 5.粘贴在另一幅图像中随机的位置
import cv2
import numpy as np
import random
import time


# 用于完成水平翻转
def flip(img, mode=1):
    """
    翻转一副图像
    :param img:符合Opencv读入格式,颜色通道为RGB,unit8类型.
    :param mode: 0垂直翻转 1水平翻转 -1垂直水平翻转
    """
    return cv2.flip(img, mode)


# 用于完成大尺度缩放
def large_scale_jittering(img, mask, min_scale=0.5, max_scale=1.5):

    # 获取尺度信息
    scale_ratio = np.random.uniform(min_scale, max_scale)  # 随机获取变换尺度
    h, w = img.shape[:2]  # 获取原始图像高宽
    new_h, new_w = int(h * scale_ratio), int(w * scale_ratio)  # 获得新的图像高宽
    if scale_ratio == 1:
        return img, mask

    # 缩放图像
    img = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_LINEAR)
    mask = cv2.resize(mask, (new_w, new_h), interpolation=cv2.INTER_NEAREST)

    # padding or crop
    x, y = int(np.random.uniform(0, abs(new_w - w))), int(np.random.uniform(0, abs(new_h - h)))

    if scale_ratio < 1.0:
        # padding
        img_padding = np.zeros([h, w, 3], dtype=np.uint8)
        mask_padding = np.zeros([h, w], dtype=np.uint8)
        img_padding[y:y + new_h, x:x + new_w, :] = img
        mask_padding[y:y + new_h, x:x + new_w] = mask
        return (img_padding, mask_padding)
    elif scale_ratio > 1.0:
        # crop
        img_crop = img[y:y + h, x:x + w, :]
        mask_crop = mask[y:y + h, x:x + w]
        return (img_crop, mask_crop)


def img_add(img1,img2,mask2):
    """

    :param img1:
    :param img2:
    :param mask2:
    :return:
    """
    h,w = img1.shape[:2]    #获取主图像的高宽

    mask = np.asarray(mask2, dtype=np.uint8)
    sub = cv2.add(img2,np.zeros(img2.shape,dtype=np.uint8),mask=mask)  #裁剪出辅助图像的区域

    mask02 = cv2.resize(mask,(w,h),interpolation=cv2.INTER_NEAREST) #辅助图像的mask映射到主图像上
    sub2 = cv2.add(img1,np.zeros(img1.shape,dtype=np.uint8),mask=mask02)    #

    img1 = img1 - sub2

    img1 = img1 + cv2.resize(sub,(w,h),interpolation=cv2.INTER_NEAREST)
    return img1


def copy_paste(img1, mask1, img2, mask2):
    """

    :param img1:
    :param mask1:
    :param img2:
    :param mask2:
    :return:
    """

    p = 0.5  # 增强概率


    # 对两组图像随机水平反转
    if random.random() > p:
        img1 = flip(img1)
        mask1 = flip(mask1)
    if random.random() > p:
        img2 = flip(img2)
        mask2 = flip(mask2)

    # 对两组图像随机尺度变换
    if random.random() > p:
        img1, mask1 = large_scale_jittering(img1, mask1)
    if random.random() > p:
        img2, mask2 = large_scale_jittering(img2, mask2)

    # 对两组图像随机
    image = img_add(img1, img2, mask2)
    label = img_add(mask1, mask2, mask2)

    return image,label



