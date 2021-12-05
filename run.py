import cv2
import time
from code.crop import crop
from code.adjust_brightness import adjust_brightness
from code.filp import filp
from code.adjust_saturation import adjust_saturation
from code.adjust_contrast import adjust_contrast

def imgShow(IMAGE, WINDOW_NAME=None):
    """
    显示一副图像,该图像符合opencv格式,且颜色通道为RGB.
    图像类型为np.uint8时,值范围[0,255].
    图像类型为np.float32时,值范围[0,1].
    对于彩色图像[3,H,W]
    对于灰度图像[H,W]
    """
    if WINDOW_NAME == None:
        WINDOW_NAME = str(time.time_ns())
    else:
        WINDOW_NAME = str(WINDOW_NAME)

    cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_AUTOSIZE)
    if IMAGE.ndim == 2:
        cv2.imshow(WINDOW_NAME,IMAGE)   #灰度图
    else:
        cv2.imshow(WINDOW_NAME,IMAGE)


image = cv2.imread(r'C:\WorkSpace\Data-Augmentation\images\image.jpg')
label = cv2.imread(r'C:\WorkSpace\Data-Augmentation\images\label.jpg')

imgShow(image)
# imgShow(label)

imgShow(adjust_saturation(image,0))
# imgShow(adjust_saturation(label,1))


cv2.waitKey(10000000)

