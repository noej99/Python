# -*- coding:utf-8 -*-

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from http.client import HTTPConnection
from json import loads
from datetime import datetime

FontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=FontFile, size=10).get_name()
plt.rc("font", family=fontName)

# 지하철
df = pd.read_csv("C:/noej/sourceFile/data/csv/subway.csv", names=["년", "월", "일", "노선", "타고", "내리고"])
df["이용객수"] = df["타고"] + df["내리고"]
print(df)

def getYoil(d):
    d = "%d%02d%02d" % (d["년"], d["월"], d["일"])
    d = datetime.strptime(d, "%Y%m%d")
    return datetime.strftime(d, "%a")
df["요일"] = df.apply(getYoil, axis=1)
print(df)

# 노선별 이용객수 분포
sns.violinplot(data=df, x="노선", y="이용객수", palette="spectral")

# 요일별 이용객수 분포
sns.violinplot(data=df, x="요일", y="이용객수", palette="Spectral")
plt.show()
