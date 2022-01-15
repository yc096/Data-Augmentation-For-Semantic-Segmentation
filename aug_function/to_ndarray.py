import torch
import numpy as np
def to_ndarray(img:torch.Tensor):
    '''
    将torch.float32格式的图像转为np.uint8格式图像
    '''
    if img.is_floating_point():
        img = img.mul(255).byte()   # self.byte() is equivalent to self.to(torch.uint8)
    if img.dim() == 2:
        return img.cpu().byte().numpy()
    np_img = np.transpose(img.cpu().numpy(),(1,2,0))
    return np_img