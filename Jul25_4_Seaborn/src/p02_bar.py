# -*- coding:utf-8 -*-

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from http.client import HTTPConnection
from json import loads

FontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=FontFile, size=10).get_name()
plt.rc("font", family=fontName)

huc = HTTPConnection("openapi.seoul.go.kr:8088")
huc.request("GET", "/575a4655496b636839386f58586542/json/RealtimeCityAir/1/25/")
rb = huc.getresponse().read()
huc.close()

dustData = loads(rb)["RealtimeCityAir"]["row"]
df = pd.DataFrame(dustData)
print(df)

# sns..barplot(data=df) #pd.DataFrame넣으면 알아서 그리기는 함
# 통계가 필요하면 알아서(권역별 PM10평균)
# 검은선 : 신뢰구간 95%
# sns.barplot(x="MSRRGN_NM", y="PM10", data=df, palette="Pastel1")

# 검은선 : 표준편차
# sns.barplot(ci="sd", x="MSRRGN_NM", y="PM10", data=df, palette="summer")

# 갯수(권역별 데이터 몇개씩
# sns.countplot(x="MSRRGN_NM", data=df, palette="autumn")

# 권역별 데이터 몇개씩, 상태별로 색깔다르게
sns.countplot(x="MSRRGN_NM", hue="IDEX_NM", data=df, palette="autumn")
plt.show()
print("------")

# oracleDB에 있는 기상청 날시
con = connect("noej/j2527303@195.168.9.61:1521/xe")
sql = "select * from kma_weather order by kw_date, kw_hour"
df2 = pd.read_sql(sql, con)
con.close()
print(df2)

# sns.barplot(x="KW_HOUR", y="KW_TEMP", data=df2, palette="rocket")
sns.barplot(x="KW_HOUR", y="KW_TEMP", hue="KOR_WEATHER", data=df2, palette="rocket")
# sns.barplot(x="KW_WEATHER", y="KW_TEMP", data=df2, palette="rocket")

# 시간대별 데이터 몇개씩(날씨별로 따로
# sns.countplot(x="KW_HOUR", hue="KW_WEATHER", dat=df2, palette="rocket")
plt.show()

