# -*- coding:utf-8 -*-

f = open("C:/noej/sourceFile/data/csv/KmaWeather.csv", "r", encoding="utf-8")
count = 0
weatherSumDict = {"12":0, "15":0, "18":0, "21":0, "24":0}
weatherCntDict = {"12":0, "15":0, "18":0, "21":0, "24":0}
for l in f.readlines():
    l = l.replace("\n", "").split(",")
    weatherSumDict[l[3]] += float(l[4])
    weatherCntDict[l[3]] += 1

h = []
t = []
for k, v in weatherSumDict.items():
    h.append(k)
    t.append (v / weatherCntDict[k])

f.close()
#######################################
import numpy as np
h = np.array(h)
t = np.array(t)
# 제일 추운거 몇시
# print(h[np.argmin(t)], np.round(t[np.argmin(t)], 1))
print(h[t == np.min(t)], np.round(np.min(t), 1))


# 제일 더운거 몇시
# 동률일때 앞에 있는거만 나옴
# print(h[np.argmax(t)], np.round(t[np.argmax(t)], 1))
# print(np.max(t))
# print(t == np.max(t))
print(h[t == np.max(t)], np.round(np.max(t), 1))

# 총 평균기온
print(np.round(np.mean(t), 1))

# 총 평균기온보다 더운거 몇시
h2 = h[t > np.mean(t)]
t2 = t[t > np.mean(t)]
for i in range(h2.size):
    print(h2[i], t2[i])

