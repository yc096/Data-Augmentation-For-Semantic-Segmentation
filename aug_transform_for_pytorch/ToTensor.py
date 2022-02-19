import torch
from aug_function.to_tensor import to_tensor
class ToTensor(object):
    def __call__(self, img_mask):
        # 图像
        img = img_mask[0]
        mask = img_mask[1]
        img = to_tensor(img )
        mask = torch.from_numpy(mask).contiguous()
        mask = mask.long()
        return (img, mask)
