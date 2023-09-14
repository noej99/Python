# -*- coding:utf-8 -*-
from cx_Oracle import connect
from datetime import datetime


con = connect("noej/j2527303@195.168.9.61:1521/xe")

cur = con.cursor()

sql = "select * from owm_weather order by ow_date"

cur.execute(sql)

# append모드로, utf-8인코딩방식(excel은 원래 utf-8을 감당x)
f = open("C:/noej/sourceFile/data/csv/weather.csv", "a", encoding="utf-8")

for date, desc, temp, humi in cur:
    # f.write("%d,%d,%d,%d," % (date.year, date.month, date.day, date.hour)
    # Python은 접근제어자가 없어서 캡슐화가 없고 멤버변수에 직접 접근
    f.write(datetime.strftime(date, "%Y,%m,%d,%H,"))
    f.write("%s," % desc)
    f.write("%.2f," % temp)
    f.write("%d\n" % humi)
    
cur.close()
con.close()
f.close()