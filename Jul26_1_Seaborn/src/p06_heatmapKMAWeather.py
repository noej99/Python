# -*- coding:utf-8 -*-

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

FontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=FontFile, size=10).get_name()
plt.rc("font", family=fontName)

# 기상청 날씨
con = connect("noej/j2527303@195.168.9.61:1521/xe")
sql = "select * from kma_weather"
df = pd.read_sql(sql, con)
con.close()
print(df)

# 시간별 기온을 날씨로 찾게 -> heatmap
pt = df.pivot_table(columns="KW_HOUR", values="KW_TEMP", index="KW_WFKOR")
print(pt)

sns.heatmap(data=pt, cmap="autumn")

plt.show()