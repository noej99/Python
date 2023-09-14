# -*- coding:utf-8 -*-
from cx_Oracle import connect
from _datetime import datetime



con = connect("noej/j2527303@195.168.9.61:1521/xe")
cur = con.cursor()

sql = "select * from seoul_dust order by sd_date, sd_MSRRGN_NM, sd_MSRSTE_NM"
cur.execute(sql)

f = open("C:/noej/sourceFile/data/csv/seoulDust.csv", "a", encoding="utf-8")

for date, MSRRGN_NM, MSRSTE_NM, pm10, pm25, idex_nm in cur:
    f.write(datetime.strftime(date, "%Y,%m,%d,%H,"))
    f.write("%s,%s,%d,%d,%s\n"% (MSRRGN_NM, MSRSTE_NM, pm10, pm25, idex_nm))
f.close()
cur.close()
con.close()