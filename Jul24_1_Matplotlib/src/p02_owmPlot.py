# -*- coding:utf-8 -*-
from cx_Oracle import connect
import pandas as pd

con = connect("noej/j2527303@195.168.9.61:1521/xe")
sql = "select * from owm_weather"
df = pd.read_sql(sql, con)
con.close()

df = df.sor_values(by="OW_DATE")
print(df)

# Pandas DataFrame -> NumPy array
# a = df.to_numpy()
# print(a)

date = df["OW_DATE"]
temp = df["OW_TEMP"]
humi = df["OW_HUMI"]

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

FontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=FontFile, size=10).get_name()
plt.rc("font", family=fontName)

_, cf1 = plt.subplots()
p1 = cf1.plot(date, temp, "r-")
cf1.set_xlabel("언제")
cf1.set_ylabel("기온")

cf2 = cf1.twinx()
p2 = cf2.plot(date, humi, "b-")
cf2.set_ylabel("습도")
cf1.legend(p1+p2, ["기온", "습도"])
plt.title("날씨")
plt.show()


