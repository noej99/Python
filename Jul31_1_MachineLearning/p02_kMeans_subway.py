# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from sklearn.cluster._kmeans import KMeans

FontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=FontFile, size=10).get_name()
plt.rc("font", family=fontName)

df = pd.read_csv("C:/noej/sourceFile/data/csv/subway.csv", names=["년", "월", "일", "노선", "역", "탄", "내린"])

# 역별 타/내린 평균 구해서
df = df.groupby("역")[["탄", "내린"]].mean()
print(df)

# 비슷한 역끼리 그룹
trainData = df.to_numpy()
km = KMeans(10)
df["그룹"] = km.fit_predict(trainData)
print(df)

# sns.scatterplot(x="탄", y="내린", hue="그룹", data=df, palette="pastel")
# plt.show()
print("-----")

# 역명 -> 그룹 역 출력
name = input("역 : ")
# print(df.loc[name])
# print(df.loc[name]["그룹"])
print(df[df["그룹"] == df.loc[name]["그룹"]])
