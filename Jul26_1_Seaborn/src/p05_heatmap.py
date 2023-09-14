# -*- coding:utf-8 -*-

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

FontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=FontFile, size=10).get_name()
plt.rc("font", family=fontName)

df = pd.read_csv("C:/noej/sourceFile/data/csv/subway.csv", names=["년", "월", "일", "노선", "타고", "내리고"])
df["이용객수"] = df["타고"] + df["내리고"]

# 피벗테이블(테이블을 요약해놓은 테이블)
# 월별 이용객수를 노선으로 찾게
pt = df.pibot_table(columns="월", values="이용객수", index="노선")
print(df)

sns.heatmap(data=pt, cmap="summer")
plt.show()