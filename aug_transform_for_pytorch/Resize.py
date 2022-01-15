import cv2


class Resize(object):
    '''
    返回指定尺寸的img和mask
    '''
    def __init__(self, resize=(256, 256)):
        self.resize_h, self.resize_w = resize
    def __call__(self, img_mask):
        img = img_mask[0]
        mask = img_mask[1]
        img = cv2.resize(img, (self.resize_w, self.resize_h), interpolation=cv2.INTER_LINEAR)
        mask = cv2.resize(mask, (self.resize_w, self.resize_h), interpolation=cv2.INTER_NEAREST)
        return img, mask

