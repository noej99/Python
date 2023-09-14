# -*- coding:utf-8 -*-
from cx_Oracle import connect

# OracleDB서버
#    사양좋음
# PC
#    사양안좋음
    
# OracleDB서버에 있는 100TB 데이터
# 인터넷으로 받아와서??
# PC에 CSV파일로??    (현실적으로 불가능)

# PC에 100TB짜리 CSV파일이 있다 해도
# list에??? (RAM에다가?)
# PC의 CPU로 계산??

# OracleDB서버에 100TB 데이터
# OracleDB서버의 좋은 cpu로 계산
# 4687.5 가져옴 

# 1) 평균가
con = connect("noej/j2527303@195.168.9.61:1521/xe")
sql = "select avg(c_price) from jul13_coffee"
cur = con.cursor()
cur.execute(sql)
for p in cur:
    print(p[0])
cur.close()

# 2) 메뉴 총 몇 종류
sql = "select count(*) from jul13_coffee"
cur = con.cursor()
cur.execute(sql)
for p in cur:
    print(p[0])
cur.close()

# 3) 최고가 메뉴 / 최저가 메뉴
sql = "select * from jul13_coffee where c_price = (select max(c_price) from jul13_coffee)"
cur = con.cursor()
cur.execute(sql)
for name, cate, price in cur:
    print(name, cate, price)
cur.close()

# 4) 최저가 메뉴 ?
sql = "select * from jul13_coffee where c_price = (select min(c_price) from jul13_coffee)"
cur = con.cursor()
cur.execute(sql)
for name, cate, price in cur:
    print(name, cate, price)
cur.close()

# 5) 카테고리별 평균가
sql = "select c_cate, avg(c_price) from jul13_coffee group by c_cate"
cur = con.cursor()
cur.execute(sql)
for cate, price in cur:
    print(cate, price)
cur.close()
con.close()