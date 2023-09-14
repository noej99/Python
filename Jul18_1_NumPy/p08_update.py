# -*- coding:utf-8 -*-
import numpy as np

a = np.random.randint(1, 11, [2, 3])
print(a)

a[0][2] = 99
a[0, 1] = 0
print(a)
#            조건, 값, 대상
b = np.where(a % 2 == 0, 100, a)
print(b)



