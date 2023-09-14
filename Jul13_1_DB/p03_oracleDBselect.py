# -*- coding:utf-8 -*-
from cx_Oracle import connect

con = connect("noej/j2527303@195.168.9.61:1521/xe")

sql = "select * from jul13_coffee"

# DB관련 작업 총괄매니저(PreparedStatement)겸 결과(ResultSet)
cur = con.cursor()

# SQL을 서버로 전송, 실행 -> 결과가 cur에 저장
cur.execute(sql)

for name, cate, price in cur:
    print(name)
    print(cate)
    print(price)
    print("------")

# for c in cur:
#     # print(c, type(c))
#     print(c[0])
#     print(c[1])
#     print(c[2])
cur.close()
con.close()
