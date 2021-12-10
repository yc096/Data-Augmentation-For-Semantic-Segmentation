import random
from aug_function.rotate import rotate

class RandomRotation(object):

    def __init__(self,angle=360):
        """
        :param angle: choice -> (0,angle)
        """
        self.angle = angle

    def __call__(self, img_mask):
        img = img_mask[0]
        mask = img_mask[1]
        rotate_angle = self.angle * random.random()
        img = rotate(img,rotate_angle,interpolation=1)
        mask = rotate(mask,rotate_angle,interpolation=0)
        return (img,mask)

