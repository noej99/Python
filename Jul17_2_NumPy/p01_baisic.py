# -*- coding:utf-8 -*-

# cmd
#    pip install numpy

# 2차원 list : 객체 list는 어쩌고...
score = [[100, 90, 50], [80, 90, 30]]
print(type(score)) # 무슨 객체인지
print(score) # 무슨 객체인지
print(score[0])
print(score[0][1])
print(score[1][2])
score[1][0] = 0
# score[1][0:3] = 0 한번에 여러개 값 바꾸는게 불가능
print(score[1][0:3])
print(score)

print("-------")

# NumPy(NumPy의 array) : 기본 Python list보다 기능 좋은 list

import numpy as np  # import 모듈명 as 별칭 -> 별칭.???
# score2 = np.array(score)
score2 = np.array(score, dtype=np.float64) # 자료형 변경 dtype=np.float??
print(type(score2))
print(score2) # 출력형태 가독성이 좀 낫다?
print(score2[0])
print(score2[0][1]) # Python list스타일
print(score2[1, 2]) # NumPy스타일
# score2[1][0] = 100
score2[1, 0] = 100
score2[1, 0:3] = 0 # slicing(한번에 여러개 값 바꾸기)
print(score2)
print(score2.dtype) # 자료형
print(score2.shape) # ?행?열
print(score2.size) # 총 갯수

# NumPy를 Pandas/Matplotlib/Tensorflow등이 활용




















