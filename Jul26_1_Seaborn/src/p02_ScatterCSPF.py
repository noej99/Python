# -*- coding:utf-8 -*-

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

FontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=FontFile, size=10).get_name()
plt.rc("font", family=fontName)

df = pd.read_csv("C:/noej/sourceFile/data/csv/cspf.csv", names=["언제", "노선", " 역", "내고타", "내고내려", "그냥타", "그냥내려"])
df["그냥합"] = df["그냥타"] + df["그냥내려"]
print(df)

# 내고타, 그냥타 관계
# sns.scatterplot(data=df, x="내고타, y="그냥타)
# 내고타, 그냥타 관계 노선별 다른색
# sns.scatterplot(data=df, x="내고타", y="그냥타", hue="노선", palette="Accent")
#내고타, 내고내려 관계 (그냥타 + 그냥내려)로 크기
sns.scatterplot(data=df, x="내고타", y="내고내려", hue="그냥합", palette="Accent")
plt.show()