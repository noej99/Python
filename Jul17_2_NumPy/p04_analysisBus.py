# -*- coding:utf-8 -*-
from datetime import datetime

# bus2015.csv
# 탄 < 내린 요일
f = open("C:/noej/sourceFile/data/csv/bus2015.csv", "r", encoding="utf-8")

rideDict = {"Sunday":0, "Monday":0,"Tuesday":0,"Wednesday":0,"Thursday":0,"Friday":0,"Saturday":0}
alightDict = {"Sunday":0, "Monday":0,"Tuesday":0,"Wednesday":0,"Thursday":0,"Friday":0,"Saturday":0}
for l in f.readlines():
#     if l.startswith("2015,02"):
#         break
#     print(l)
    l = l.replace("\n", "").split(",")
    
    yoil = datetime.strftime(datetime.strptime(l[0]+l[1]+l[2], "%Y%m%d"),"%A")
#     print(yoil)
    # 데이터내에 ,가 사용되어 ,로 split했을 때 앞에서부터 5번째, 6번째가 다른게 나옴
    # -> split해서 위치가 일정하지 않을 때 뒤에서부터 
    rideDict[yoil] += int(l[-2])
    alightDict[yoil] += int(l[-1])

yoils, rides, alights = [], [], []
for k, v in rideDict.items():
    yoils.append(k)
    rides.append(v)
    alights.append(alightDict[k])
f.close()
################################################
import numpy as np
yoils = np.array(yoils)
rides = np.array(rides)
alights = np.array(alights)

print(yoils[rides < alights]) # 탄 게 내린거 보다많아서 안나옴 []
print(yoils)
print(rides)
print(alights)



