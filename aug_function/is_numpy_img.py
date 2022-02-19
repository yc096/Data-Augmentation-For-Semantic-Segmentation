import numpy as np
def is_numpy_img(img):
    """
    用作所有功能函数中做类型检查判断。
    """
    return isinstance(img, np.ndarray) and img.ndim in {2, 3}