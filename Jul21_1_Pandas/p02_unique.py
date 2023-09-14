# -*- encoding:utf-8 -*-

import pandas as pd
from cx_Oracle import connect

df = pd.read_csv("C:/noej/sourceFile/data/csv/titanic.csv")
print(df.columns)
print("-----")

# 객실 클래스별 요금 평균가
print(df.groupby("Pclass")["Fare"].mean())
print("-----")

# 객실 클래스별 죽은사람수/산사람수
print(df.groupby(["Pclass", "Survived"])["PassengerId"].count())
print("-----")

# 성별 별로 죽은사람수/산사람수
print(df.groupby(["Sex", "Survived"])["PassengerId"].count())
print("-----")

# 객실명이 뭐뭐있나(중복제거)
print(df["Cabin"].unique())
print("-----")

# 객실이 몇개 있었나
print(df["Cabin"].nunique())
print("-----")

# 객실별로 몇명씩
print(df["Cabin"].value_counts())
print("-----")

# OracleDB기상청
con = connect("noej/j2527303@195.168.9.61:1521/xe")
sql = "select * from kma_weather"
df2 = pd.read_sql(sql, con)
con.close()
# 어떤 날씨들이 있었나
print(df2["KW_WEATHER"].unique())

# 각 날씨별 맑음은 몇번
print(df2["KW_WEATHER"].value_counts())

