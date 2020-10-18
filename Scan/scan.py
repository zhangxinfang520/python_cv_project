import argparse
import numpy as np
import cv2
from Scan.myutils import resize,order_points,four_print_transfrom

#设置参数
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image", required=True, help="Path to the image to be scanned")
args = vars(parser.parse_args())


#图片读取
image = cv2.imread(args["image"])
#坐标会发生相应的变化
ratio = image.shape[0]/500.0

orig = image.copy()

image = resize(orig,height=500)

#预处理
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#高斯分布 以平滑图像，消除噪声
gray = cv2.GaussianBlur(gray, (5, 5), 0)
#边缘检测
edged = cv2.Canny(gray, 75, 200)
print("STEP 1:边缘检测 ")
cv2.imshow("Image", image)
cv2.imshow("src",edged)
cv2.waitKey(0)
cv2.destroyAllWindows()

#轮廓检测
cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0]
#cv2.contourArea(cnt， True)  # 计算轮廓的面积
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]

#遍历轮廓
for c in cnts:
    #计算轮廓近似
    #arcLength(InputArray curve, bool closed);
        # curve，输入的二维点集（轮廓顶点），可以是 vector 或 Mat 类型。
        # closed，用于指示曲线是否封闭。
    peri = cv2.arcLength(c,closed=True)#计算封闭轮廓的周长或曲线的长度
    #approxPolyDP(contour, epsilon, True)
    #c表示输入的点集
    #esiilon表示从原始轮廓到近似轮廓的最大距离，他是一个准确度参数
    #closed，用于指示曲线是否封闭。
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    #当有四个点的时候就取出
    if len(approx)==4:
        screenCnt = approx
        break

#展示结果
print("STEP 2 :获取轮廓")
cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)
cv2.imshow("outline",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#透视转换
warped = four_print_transfrom(orig, screenCnt.reshape(4, 2) * ratio)
#二值处理
warped = cv2.cvtColor(warped,cv2.COLOR_BGR2GRAY)
ref = cv2.threshold(warped,100,255,cv2.THRESH_BINARY)[1]
cv2.imwrite("scan.jpg",ref)

# 展示结果
print("STEP 3: 变换")
cv2.imshow("Original", resize(orig, height = 650))
cv2.imshow("Scanned", resize(ref, height = 650))
cv2.waitKey(0)

