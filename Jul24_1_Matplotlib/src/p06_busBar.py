# -*- coding:utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

FontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=FontFile, size=10).get_name()
plt.rc("font", family=fontName)

df = pd.read_csv("C:/noej/sourceFile/data/csv/bus2015Result.txt", sep="\t", names=["요일", "합계"])
print(df)

df1 = df[df["요일"].str.contains("데이터수")]
df1["요일"] = df1["요일"].apply(lambda y:y.replace("_데이터수", ""))

df2 = df[df["요일"].str.contains("합")]
df2["요일"] = df2["요일"].apply(lambda y:y.replace("_합", ""))

yoil = df1["요일"]
cnts = df1["합계"]
sums = list(df2["합계"]) # 0,1,2,...쓰게

print(yoil)
avgs = []
for i, v in enumerate(cnts):
    avgs.append(sums[i] / v)
print(avgs)

plt.bar(yoil, avgs)
plt.show()