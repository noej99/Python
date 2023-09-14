# -*- coding:utf-8 -*-
from cx_Oracle import connect

con = connect("noej/j2527303@195.168.9.61:1521/xe")

sql = "select * from jul13_coffee"

cur = con.cursor()

cur.execute(sql)

f = open("C:/noej/sourceFile/coffeeTest.csv", "a", encoding="utf-8")
for name, cate, price in cur:
    f.write("%s,%s,%d\n" % (name, cate, price))
f.close()
cur.close()
con.close()
