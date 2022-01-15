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


# Debug
import cv2
img = cv2.imread(r'C:\WorkSpace\Data-Augmentation-For-Semantic-Segmentation\images\image.jpg',1)
mask = cv2.imread(r'C:\WorkSpace\Data-Augmentation-For-Semantic-Segmentation\images\label.jpg',0)
cv2.imshow('1',img)
cv2.imshow('2',mask)

img , mask = RandomScale(scales=(0.5,0.75,1,1.25,1.5))((img,mask))
cv2.imshow('3',img)
cv2.imshow('4',mask)
cv2.waitKey(0)
