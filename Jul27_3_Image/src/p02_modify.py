# -*- coding:utf-8 -*-

import cv2
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

FontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=FontFile, size=10).get_name()
plt.rc("font", family=fontName)

a = cv2.imread("C:/Users/jny09/bbong.jpg", cv2.IMREAD_GRAYSCALE)
print(a)

# 크기 조절
# a = cv2.resize(a, dsize=(100, 50)) # 100x50으로
# a = cv2.resize(a, dsize=(0,0), fx=0.3, fy=0.5) # x를 0.3배, y를 0.5배

# 자르기
# a = a[100:200, 300:400]

# 블러
# 그 픽셀 주위 50x30의 평균값으로 바꿔서 블러처리
# a = cv2.blur(a, (50, 30))

# 대비 늘리기(밝은거 더 밝게, 어두운거 더 어둡게)
# a = cv2.equalizeHist(a)

# 경계선(10보다 작으면 무시, 50보다 크면 선으로 인식)
a = cv2.Canny(a, 10, 50)
print(a)

# 저장하기
cv2.imwrite("C:/Users/Default/Pictures/bbong.jpg", a)

plt.imshow(a, cmap="gray")
plt.show()