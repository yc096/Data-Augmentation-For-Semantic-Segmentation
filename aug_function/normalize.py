
import numpy as np


def normalize(img, mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225), max_pixel=255.0):
    """
    对一副图像进行标准化,label不做变换.
    要注意mean和std和图像的颜色通道是否一致.
    标准化公式为:img=(img-mean*max_pixel)/(std*max_pixel)
    :param img: 符合Opencv读入格式,unit8,float类型.
    :param mean,std:标准化参数,每个通道都要给出.值区间应该在[0,1]
    :param max_pixel:图像的最大像素值,uint8类型为255,因此会将mean和std变换到这个区间内.而float类型为1,此时mean和std无变化.
    :return:返回经过标准化的float类型图像.
    """

    mean = np.array(mean, dtype=np.float32) * max_pixel
    std = np.array(std, dtype=np.float32) * max_pixel

    # 默认彩色图像
    img = img.astype(np.float32)
    img -= mean
    img /= std
    # 图像标准化后,RGB数值虽有大有小、有正有负,但是数据的分布是一致的.
    return img
    # 可以用pytorch官方方式验证
    # import torch
    # from torchvision import transforms
    # img_std = torchvision.transforms.functional.to_tensor(image)
    # img_std = torchvision.transforms.functional.normalize(img_std,mean=[0.485, 0.456, 0.406],std=[0.229, 0.224, 0.225])
    # img_std = np.transpose(img_std.numpy(),[1,2,0])


def unnormalize(img, mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)):
    """
    对一副图像进行反标准化,,label不做变换.
    标准化公式为:img= img*std + mean
    :param img: 符合Opencv读入格式,float类型.
    :param mean,std:标准化参数,每个通道都要给出.值区间应该在[0,1]
    :return:返回float类型原始图像.
    """

    mean = np.array(mean, dtype=np.float32)
    std = np.array(std, dtype=np.float32)
    # 默认彩色图像
    img = img.astype(np.float32)
    img *= std
    img += mean

    return img
