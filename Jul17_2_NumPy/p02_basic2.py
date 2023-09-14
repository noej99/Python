# -*- coding:utf-8 -*-

a = [10, 20, 30]
b = [1, 2, 3]
c = a + b
print(c)
d = []
for i, a in enumerate(a):
    d.append(a + b[i])
print(d)

# e = a * b
# print(e)

f = a * 2 # 반복
print(f)
##########################-> 자리별로 계산x, list append
import numpy as np
a2 = np.array(a)
b2 = np.array(b)
c2 = a2 + b2 # (1x2) + (1x2)
             # 같은 모양끼리는 자리같은 것끼리 계산
print(c2)
d2 = a2 * b2
print(d2)

e2 = a2 * 3 # (1x2) * (1)
            # broadcasting : 다른모양이면 차원수 높은쪽에 맞춰서 항목별로 계산 
print(e2)
print("------")

name = np.array(["김길동", "이길동", "박길동"])
kor = np.array([100, 80, 30])
eng = np.array([80, 66, 81])
mat = np.array([66, 55, 100])

#        자리별 계산     broadcasting
avg = (kor + eng + mat) / 3
print(avg)

over80 = avg > 80 # boolean가능
print(over80)

print(avg[over80]) # masking : 위치에 True인 것만
print(name[over80])
print(name[kor > 90])
# kor > 90 : [True False False]

# 영어점수가 50 <= x <= 70
# print(name[50 <= eng <=70])
# and/or 대신 &/|를 써야
print(name[(50 <= eng) & (eng <=70)])

