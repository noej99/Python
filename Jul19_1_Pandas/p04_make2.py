# -*- coding:utf-8 -*-

import pandas as pd
from cx_Oracle import connect

# 데이터 없
# kaggle : 분석 경진대회 샘플데이터
# 타이타닉

# csv파일(첫줄에 제목이 있는)로
a = pd.read_csv("C:/noej/sourceFile/data/csv/titanic.csv")
print(a)
print("-------------")

# csv파일(첫줄에 제목이 없는)    names=[]로 제목추가
b = pd.read_csv("C:/noej/sourceFile/data/csv/subway.csv", names=["년", "월", "일", "노선", "역", "탑승", "하차"])
print(b)
print("-------------")

# 어쨌든 파일
# .csv, .txt : 확장자 - MS Window에만
c = pd.read_csv("C:/noej/sourceFile/data/csv/kakaoBlog.txt", sep="\t", names=["제목", "내용", "블로그"]) # 구분자 없으면 sep=로
print(c)

# OracleDB에 있는거
con = connect("noej/j2527303@195.168.9.61:1521/xe")
sql = "select * from owm_weather"
d = pd.read_sql(sql, con)
print(d)

sql = " select sd_MSRRGN_NM, avg(sd_pm10) from seoul_dust group by sd_MSRRGN_NM"
e = pd.read_sql(sql, con)
print(e)
con.close()

# 정형데이터
#    OracleDB에 : DB에서 SQL로 처리
#    csv파일 : Hadoop으로 처리
# 비정형데이터
#    데이터프레임은 좀 아니고
# -> Pandas?
