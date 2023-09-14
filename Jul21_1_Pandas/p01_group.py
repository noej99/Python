# -*- encoding:utf-8 -*-

import pandas as pd
from cx_Oracle import connect

# 물가정보

df = pd.read_csv("C:/noej/sourceFile/data/csv/lnps.csv", names=["위치", "품명", "가격", "종류", "구"])
print(df)
print("-----")

print(df["가격"].mean()) # 평균가
print(df.groupby("종류")["가격"].mean()) # 종류별 평균가
print("-----")

# 구별 -> 종류별 최고가
print(df.groupby(["구", "종류"])["가격"].max())

# OracleDB에 있는 기상청데이터
# 날씨별 평균기온

con = connect("noej/j2527303@195.168.9.61:1521/xe")

# Pandas
sql = "select * from kma_weather"
df2 = pd.read_sql(sql, con)
print(df2.groupby("KW_WEATHER")["KW_TEMP"].mean())

# SQL
sql = "select KW_WEATHER, avg(KW_TEMP) from kma_weather group by KW_WEATHER"
df2 = pd.read_sql(sql, con)
print(df2)
con.close()