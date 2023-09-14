# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

FontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=FontFile, size=10).get_name()
plt.rc("font", family=fontName)

df = pd.read_csv("C:/noej/sourceFile/data/csv/sh3Result2.csv", names=["단어", "횟수"])
df = df.sort_values(by="횟수", ascending=False)
print(df)

sns.barplot(x="단어", y="횟수", data=df.head(20))
plt.show()

