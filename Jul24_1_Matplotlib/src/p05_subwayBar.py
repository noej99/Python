# -*- coding:utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

FontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=FontFile, size=10).get_name()
plt.rc("font", family=fontName)

df1 = pd.read_csv("C:/noej/sourceFile/data/csv/shResult.txt", sep="\t", names=["노선", "탄"])
df2 = pd.read_csv("C:/noej/sourceFile/data/csv/shResult2.txt", sep="\t", names=["노선", "내린"])
df = pd.merge(df1, df2)
print(df)

no = df["노선"]
ride = df["탄"]
alight = df["내린"]

plt.bar(no, ride, color="red")
plt.bar(no, alight, color="green", bottom=ride)
plt.show()
