# -*- coding:utf-8 -*-

# visual studio 2022설치하고
# pip install --upgrade pip setuptools wheel
# pip install opencv-python==3.4.0.12
import cv2
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

FontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=FontFile, size=10).get_name()
plt.rc("font", family=fontName)

# ML/DL
# 이미지/사운드/영상 : 컴에는 10101로 저장
#    그 데이터를 인코딩만 할 줄 알면

# 픽셀이 아예 흰색 : 255
# 픽셀이 아예 검정 : 0
# 픽셀 하나를 0 ~ 255로
a = cv2.imread("C:/Users/Default/Pictures/test.png", cv2.IMREAD_GRAYSCALE)
print(a)
print("--------")

# 픽셀 하나를 [B G R]로

b = cv2.imread("C:/Users/Default/Pictures/test.png", cv2.IMREAD_COLOR)
# BGR -> RGB로
b = cv2.cvtColor(b, cv2.COLOR_BGR2RGB)
print(b)

plt.imshow(b)
plt.show()
