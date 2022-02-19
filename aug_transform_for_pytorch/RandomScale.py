import random
from aug_function.scale import scale
class RandomScale(object):
    def __init__(self,scales=(1,),p=0.5):
        self.scales = scales
        self.p = p

    def __call__(self, img_mask):
        if random.random() > self.p:
            return img_mask

        img = img_mask[0]
        mask = img_mask[1]
        random_scale = random.choice(self.scales)
        img,mask = scale(img,mask,random_scale,)
        return (img,mask)



