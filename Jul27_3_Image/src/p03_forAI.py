# -*- coding:utf-8 -*-

import cv2

# [
#    [p p p]
#    [p p p]
# ] => 2차원

a = cv2.imread("C:/Users/jny09/bbong.jpg", cv2.IMREAD_GRAYSCALE)
print(a)

# [
#    [[B G R] [B G R] [B G R]]
#    [[B G R] [B G R] [B G R]]
# ] => 3차원
b = cv2.imread("C:/Users/jny09/bbong.jpg", cv2.IMREAD_COLOR)
print(b)
print("-----")

# 무슨 데이터든 1차원으로 만들면 됨
b = b.flatten()
print(b)