# -*- encoding:utf-8 -*-
import pandas as pd
from cx_Oracle import connect

con = connect("noej/j2527303@195.168.9.61:1521/xe")

sql = "select * from kma_weather"
con.close()

df = pd.read_sql(sql, con)
print(df)
print("--------")

# 최고기온
print(df["KW_TEMP"].max())
print("--------")

# 평균기온
print(df["KW_TEMP"].mean())
print("--------")

# 최고기온 언제, 몇시
print(df[df["KW_TEMP"] == df["KW_TEMP"].max()][["KW_DATE", "KW_HOUR"]])
print("--------")

# 평균기온보다 낮은거 언제, 몇시, 날씨
print(df[df["KW_TEMP"] < df["KW_TEMP"].mean()][["KW_DATE", "KW_HOUR", "KW_WEATHER"]])
print("--------")
print("========")

con = connect("noej/j2527303@195.168.9.61:1521/xe")

# 최고기온
sql = "select max(KW_TEMP) from kma_weather"
df = pd.read_sql(sql, con)
print(df)

# 평균기온
sql = "select avg(KW_TEMP) from kma_weather"
df = pd.read_sql(sql, con)
print(df)

# 최고기온 언제, 몇시
sql = "select KW_DATE, KW_HOUR from kma_weather where KW_TEMP = (select max(KW_TEMP) from kma_weather)"
df = pd.read_sql(sql, con)
print(df)

# 평균기온보다 낮은거 언제, 몇시, 날씨
sql = "select KW_DATE, KW_HOUR, KW_WEATHER from kma_weather where KW_TEMP < (select avg(KW_TEMP) from kma_weather)"
df = pd.read_sql(sql, con)
print(df)

con.close()