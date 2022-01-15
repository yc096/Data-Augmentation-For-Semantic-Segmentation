import cv2
import random

class RandomHorizontalFlip(object):
    '''
    随机水平反转
    self.flip_mode : 0垂直翻转 1水平翻转 -1垂直水平翻转
    '''
    def __init__(self, p=0.5):
        self.p = p
        self.flip_mode = 1

    def __call__(self, img_mask):
        if random.random() > self.p:
            return img_mask
        else:
            img = img_mask[0]
            mask = img_mask[1]
            img = cv2.flip(img, self.flip_mode)
            mask = cv2.flip(mask, self.flip_mode)
            return img, mask
