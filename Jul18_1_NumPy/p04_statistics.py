# -*- coding:utf-8 -*-
import numpy as np

# 통계

a = np.random.randint(1, 11, [2, 3])
print(a)
print("-----------")

b = np.sum(a) # 합계
print(b)

c = np.mean(a) # 평균
print(c)

d = a - c # 각 값에서 평균 빼기
d = d ** 2 # 제곱
d = np.mean(d) # 그거의 평균
print(d)

e = np.var(a) # 분산
print(e)

f = np.sqrt(e) # 분산에 루트
print(f)

g = np.std(a) # 표준편차
print(g)

# 분산/표준편차 : 평균에서 얼마나 떨어져있나

h = np.max(a)
print(h)
i = np.min(a)
print(i)

j = np.sum(a, axis=0) # 열방향 합계
print(j)
k = np.mean(a, axis=1) # 행방향 평균
print(k)
print("-----------")
print(a)
print("-----------")
l = np.argmax(a) # 최대값인덱스(위치)
print(l)
m = np.argmin(a) # 최소값인덱스(위치)
print(m)
n = np.argmax(a, axis=0)
print(n)
o = np.argmin(a, axis=1)
print(o)
print("-----------")
p = np.cumsum(a) # 누적 합
print(p)
q = np.cumprod(a) # 누적 곱
print(q)