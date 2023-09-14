# -*- coding:utf-8 -*-
from cx_Oracle import connect

# J : JDBC -> ConnectionPool -> MyBatis

# P 
# 연결
con = connect("noej/j2527303@195.168.9.61:1521/xe")

# 데이터 확보
n = input("이름 : ")
c = input("종류 : ")
p = int(input("가격 : "))

# SQL(완성)
sql = "insert into jul13_coffee values('%s', '%s', %d)" % (n, c, p)

# DB관련 작업 총괄매니저(PreparedStatement)겸 결과
cur = con.cursor()

# SQL을 서버로 전송, 실행 -> 결과가 cur에 저장
cur.execute(sql)

if cur.rowcount == 1:
    print("성공")
    con.commit()

cur.close()
con.close()
