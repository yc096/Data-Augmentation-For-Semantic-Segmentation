import torch
def to_tensor(img):
    '''
    将ndarray格式的image转为符合pytorch的格式
    :param img:
    :return:
    '''
    if img.ndim == 2:
        img = img[:, :, None]
    img = img.transpose((2, 0, 1))
    img = torch.from_numpy(img).contiguous()
    if isinstance(img, torch.ByteTensor):   #
        return img.float().div(255)
    else:
        return img