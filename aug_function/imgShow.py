import time
import cv2
def imgShow(IMAGE, WINDOW_NAME=None):
    """
    显示一副图像,该图像符合opencv格式,且颜色通道为RGB.
    图像类型为np.uint8时,值范围[0,255].
    图像类型为np.float32时,值范围[0,1].
    对于彩色图像[H,W,3]
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
        cv2.imshow(WINDOW_NAME, cv2.cvtColor(IMAGE, cv2.COLOR_RGB2BGR))