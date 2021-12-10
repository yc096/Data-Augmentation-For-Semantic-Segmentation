from aug_function.copy_paste import copy_paste
# Paper -> https://arxiv.org/pdf/2012.07177.pdf

class CopyPaste(object):
    def __init__(self,p):
        self.p = p
    def __call__(self, img_mask1,img_mask2):

        #main img/mask
        img1 = img_mask1[0]
        mask1 = img_mask1[1]
        #
        img2 = img_mask2[0]
        mask2 = img_mask2[1]

        img , mask  = copy_paste(img1,mask1,img2,mask2)

        return (img,mask)



