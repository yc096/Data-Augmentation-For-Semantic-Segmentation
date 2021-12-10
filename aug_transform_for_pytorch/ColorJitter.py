import random
from aug_function.adjust_brightness import adjust_brightness
from aug_function.adjust_contrast import adjust_contrast
from aug_function.adjust_saturation import adjust_saturation

class ColorJitter(object):
    def __init__(self,brightness=0.5, contrast=0.5, saturation=0.5):
        self.brightness = random.uniform(max(0, 1 - brightness), 1 + brightness)
        self.contrast = random.uniform(max(0, 1 - contrast), 1 + contrast)
        self.saturation = random.uniform(max(0, 1 - saturation), 1 + saturation)
    def __call__(self,img_mask):
        img = img_mask[0]
        # mask not transform
        img = adjust_brightness(img,self.brightness)
        img = adjust_contrast(img,self.contrast)
        img = adjust_saturation(img,self.saturation)
        return (img,img_mask[1])
