# -*- coding:utf-8 -*-
import numpy as np

a = np.random.randint(1, 101, [3, 5])
b = np.random.randint(1, 101, [3, 5])
print(a)
print(b)
print("----------------")
c = a + b
print(c)
print("----------------")
d = np.concatenate([a, b]) # 붙이기
print(d)
print("----------------")
e = np.append(a, b) # 붙여서 1차원으로 - v (딥러닝, 인공신경망)
print(e)
print("----------------")
# NumPy, Pandas, TF, ...
# axis = 0 : 열방향
# axis = 1 : 행방향
f = np.concatenate([a, b], axis=1)
print(f)
print("----------------")
g = np.append(a, b, axis=0) # d랑 같음(concatenate랑 같아짐)
print(g)
print("----------------")
h = np.append(a, b, axis=1) # f랑 같음(concatenate랑 행방향)
print(h)
print("====================")

aa = np.array_split(a, 2) # 대책없이 2개로 나누기
print(aa)
print("----------------")
# bb = np.split(b, 2) # 똑같이 2개로 나누기(똑같이 못나누면 error)
# print(bb)
bb = np.split(b, 3)
print(bb)







