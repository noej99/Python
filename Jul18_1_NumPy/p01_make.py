# -*- coding:utf-8 -*-
import numpy as np

# tensorflow 등 후속기술에서 사용
# -> 인공신경망 초기값
# 더미데이터 만들때

a = np.zeros([3, 2]) # 3x2, 0들
print(a)

b = np.ones([3, 2]) # 1들
print(b)

c = np.empty([3, 2]) # 의미없는 값들
print(c)

print("--------------")

d = np.arange(5) # 0 ~ (5-1)
print(d)

e = np.arange(2, 6) # 2 ~ (6-1)
print(e)

f = np.arange(2, 10, 3) # 2 ~ (10-1) 3칸씩
print(f)

print("--------------")

g = np.random.rand(3, 2) # 0.0 ~ 0.99까지 3x2 
print(g)

h = np.random.randn(3, 2) # 평균0, 표준편차1 랜덤 3x2
print(h)

i = np.random.randint(2, 10, [3, 2]) # 2 ~ (10-1)까지 정수랜덤 3x2
print(i)





