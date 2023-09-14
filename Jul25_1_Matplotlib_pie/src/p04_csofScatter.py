# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

FontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=FontFile, size=10).get_name()
plt.rc("font", family=fontNa

# 노선별 내고타, 그냥타, 내고내린, 그냥내린거 평균
df = pd.read_csv("C:/noej/sourceFile/data/csv/cspf.csv", names=["월", "노선", "역", "내고탐", "그냥탐", "내고내림", "그냥내림"])
print(df)

df2 = df.groupby("노선")[["내고탐", "그냥탐", "내고내림", "그냥내림"]].mean()
print(df2)

no = df2.index # 1호선, 2호선, ...
no2 = np.arange(len(no)) # 0, 1, ...
prn = df2["내고탐"]
frn = df2["그냥탐"]
pan = df2["내고내림"]
fan = df2["그냥내림"]

f = (frn + fan) / 2
f = (f / f.max()) * 1000

# 돈내고 많이 타면, 돈내고 많이 내림
# 근데 그거랑 무임시리즈랑은 무관

plt.scatter(prn, pan, s=f, color="green", alpha=0.5)
plt.title("지하철")
plt.show()