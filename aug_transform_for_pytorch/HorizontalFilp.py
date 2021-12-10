import random
from aug_function.flip import flip

class HorizontalFlip(object):

    def __init__(self, p=0.5):
        self.p = p

    def __call__(self, img_mask):
        if random.random() > self.p:
            return img_mask
        else:
            img = img_mask[0]
            mask = img_mask[1]
            return (flip(img,mode=1),flip(mask,mode=1))
