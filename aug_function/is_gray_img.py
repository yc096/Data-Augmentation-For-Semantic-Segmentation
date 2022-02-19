import numpy as np
def is_gray_img(img: np.ndarray):
    """
    用作所有功能函数中做类型检查判断。
    """
    return (len(img.shape) == 2) or (len(img.shape) == 3 and img.shape[-1] == 1)