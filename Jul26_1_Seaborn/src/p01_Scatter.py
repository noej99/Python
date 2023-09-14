# -*- coding:utf-8 -*-

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

FontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=FontFile, size=10).get_name()
plt.rc("font", family=fontName)

# oracleDB owm날씨
con = connect("noej/j2527303@195.168.9.61:1521/xe")
sql = "select * from owm_weather"
df = pd.read_sql(sql, con)
con.close()
print(df)

sns.scatterplot(x="OW_TEMP", Y="OW_HUMI", data=df, hue="OW_DESC", size="OW_HUMI", palette="magma")
plt.show()
