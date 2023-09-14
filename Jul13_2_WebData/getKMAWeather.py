# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
from xml.etree.ElementTree import fromstring
from cx_Oracle import connect

# BD/AI 1단계 : 분석용 데이터 구축
#    OracleDB
#        날짜    시간    기온    날씨

huc = HTTPSConnection("www.kma.go.kr")
huc.request("GET", "/wid/queryDFSRSS.jsp?zone=1111061500")
resBody = huc.getresponse().read()
# XML피싱
con = connect("noej/j2527303@195.168.9.61:1521/xe")
# pstmt : 자동commit -> 1회용
# cur : 수동commit -> 여러번 사용가능
cur = con.cursor()
for w in fromstring(resBody).getiterator("data"):
    if w.find("day").text == "1":
        break
    sql = "insert into kma_weather values(sysdate, "
    sql += "%s, " % w.find("hour").text
    sql += "%s, " % w.find("temp").text 
    sql += "'%s')" % w.find("wfKor").text
    cur.execute(sql)

con.commit()
cur.close()
con.close()
huc.close()