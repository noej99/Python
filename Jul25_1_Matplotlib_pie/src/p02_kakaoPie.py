# -*- coding:utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

FontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=FontFile, size=10).get_name()
plt.rc("font", family=fontNa

df = pd.read_csv("C:/noej/sourceFile/data/csv/kakaoResult.txt", sep="\t", names=["누구", "몇번"])
df = df[df["누구"].str.contains("습니다") == False]
df = df.sort_values(by="몇번", ascending=False)
print(df)

name = df["누구"]
count = df["몇번"]

# 비율
plt.pie(count, labels=name, autopct="%.1f%%")
plt.title("카톡")
plt.show()
