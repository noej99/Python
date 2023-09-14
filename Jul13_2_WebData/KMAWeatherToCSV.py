# -*- coding:utf-8 -*-
from cx_Oracle import connect
from _datetime import datetime

# DB에 저장된 기상청 날씨예보데이터
# csv로 저장하는 프로그램

# 년,월,일,시,기온,날씨
# 2023,7,13,21,20.0,비


f = open("C:/noej/sourceFile/data/csv/kmaWeather.csv", "a", encoding="utf-8")

con = connect("noej/j2527303@195.168.9.61:1521/xe")
cur = con.cursor()

sql = "select * from kma_weather order by kw_date, kw_hour"

cur.execute(sql)

for d, h, t, w in cur:
    f.write(datetime.strftime(d, "%Y,%m,%d,"))
    f.write("%d,%.1f,%s\n"% (h, t, w))
f.close()
cur.close()
con.close()