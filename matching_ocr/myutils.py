import cv2#格式bgr

def sort_contours(cnts,method="left-to-right"):
    '''
    排序轮廓坐标
    :param cnts: 轮廓的集合
    :param method:
    :return: 默认从左到右
    '''
    reverse =False
    i=0
    if method == "left-to-right" or method == "bottom-to-top":
        reverse =True
    if method == "top-to-bottom" or method == "bottom-to-top":
        i=1
    boundingBoxes = [cv2.boundingRect(c) for c in cnts]#用一个最小的矩形，把找到的形状包起来x,y,h,w
    '''
    sorted(iterable, cmp=None, key=None, reverse=False)
        对所有可迭代的对象进行排序操作
        iterable -- 可迭代对象
        cmp -- 比较的函数，这个具有两个参数，参数的值都是从可迭代对象中取出，此函数必须遵守的规则为，
        大于则返回1，小于则返回-1，等于则返回0
        key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，
        指定可迭代对象中的一个元素来进行排序
        reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认
    '''
    (cnts, boundingBoxes) = zip(*sorted(zip(cnts,boundingBoxes),key=lambda b:b[1][i],reverse=reverse))
    return cnts, boundingBoxes


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