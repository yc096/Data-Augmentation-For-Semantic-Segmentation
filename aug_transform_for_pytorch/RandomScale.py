import random
from aug_function.resize import resize  #为了保持与其他函数的一致性
class RandomScale(object):
    def __init__(self,scales=(1,)):
        self.scales = scales

    def __call__(self, img_mask):
        img = img_mask[0]
        mask = img_mask[1]
        H,W = img.shape[:2]
        scale = random.choice(self.scales)
        H,W = int(H*scale),int(W*scale)
        img = resize(img,H,W,1)
        mask = resize(mask,H,W,0)
        return (img,mask)
