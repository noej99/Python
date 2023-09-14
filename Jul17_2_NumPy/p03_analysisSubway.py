# -*- coding:utf-8 -*-

f = open("C:/noej/sourceFile/data/csv/subway.csv", "r", encoding="utf-8")

rideDict = {}
alightDict = {}
for l in f.readlines():
    l = l.replace("\n", "").split(",")
    if l[4] in rideDict:
        # rideDict에 있으면
        rideDict[l[4]] += int(l[5])
        alightDict[l[4]] += int(l[6])
    else:
        # 없으면
        rideDict[l[4]] = int(l[5])
        alightDict[l[4]] = int(l[6])
name = []
ride = []
alight = []
for k, v in rideDict.items(): # (키, 값) tuple형태로 리턴
    name.append(k)
    ride.append(v)
    alight.append(alightDict[k])    
f.close()
########################
# 탄 < 내린 역 이름
import numpy as np
name = np.array(name)
ride = np.array(ride)
alight = np.array(alight)
print(name[ride < alight])






