# -*- coding:utf-8 -*-
from cx_Oracle import connect

con = connect("noej/j2527303@195.168.9.61:1521/xe")
cur = con.cursor()

sql = "select sd_MSRRGN_NM, avg(sd_PM10 + sd_pm25) from seoul_dust group by sd_MSRRGN_NM order by sd_MSRRGN_NM"
cur.execute(sql)

for sd_MSRRGN_NM, dust in cur:
    print(sd_MSRRGN_NM, dust)
    
cur.close()
con.close()
