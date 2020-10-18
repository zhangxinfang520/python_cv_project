import cv2#格式bgr
import numpy as np


def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    '''
用来调整图像大小的函数；
    :param image:图片源
    :param width:输出图片的宽度
    :param height:输出图片的高度
    :param inter: CV_INTER_NEAREST  最邻近插值点法
                  CV_INTER_LINEAR  双线性插值法
                  CV_INTER_AREA 邻域像素再取样插补
                  CV_INTER_CUBIC 双立方插补，4*4大小的补点
    :return:
    '''
    dim = None
    (h,w) = image.shape[0:2]
    if width is None and height is None :
        return image
    if width is None:
        r = height/float(h)
        dim = (int(w*r),height)
    else:
        r = width/float(w)
        dim = (width,int(r*h))
    resized = cv2.resize(image,dim,interpolation=inter)
    return resized

def order_points(pts):
    '''
    获取输入点的坐标
    :param pts:
    :return:
    '''
    #一共四个点坐标
    rect = np.zeros((4, 2), dtype="float32")
    # 按顺序找到对应坐标0123分别是 左上，右上，右下，左下(顺时针)
    # 计算左上，右下
    #axis =1 将矩阵的每一行向量相加
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]
    # 计算右上和左下
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]

    return rect


def four_print_transfrom(image, pts):
    '''
    进行转化为正常格式
    :param image:图像
    :param pts:轮廓的坐标
    :return:
    '''
    #获取输入点的坐标
    rect = order_points(pts)
    (tl,tr,br,bl) = rect
    # 计算输入的w和h值
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))
    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))
    # 变换后对应坐标位置
    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype="float32")
    #计算变换矩阵
    #返回由源图像中矩形到目标图像矩形变换的矩阵
    #cv2.getPerspectiveTransform(src, dst) → retval
    #src：源图像中待测矩形的四点坐标
    #sdt：目标图像中矩形的四点坐标
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
    # 返回变换后结果
    return warped