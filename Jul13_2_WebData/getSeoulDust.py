# -*- coding:utf-8 -*-
from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring
from cx_Oracle import connect

# http://openapi.seoul.go.kr:8088/575a4655496b636839386f58586542/xml/RealtimeCityAir/1/25/

huc = HTTPConnection("openapi.seoul.go.kr:8088")
huc.request("GET", "/575a4655496b636839386f58586542/xml/RealtimeCityAir/1/25/")
resBody = huc.getresponse().read()

con = connect("noej/j2527303@195.168.9.61:1521/xe")
cur = con.cursor()
for d in fromstring(resBody).getiterator("row"):
    sql = "insert into seoul_dust values(sysdate, "
    sql += "'%s', " % d.find("MSRRGN_NM").text
    sql += "'%s', " % d.find("MSRSTE_NM").text 
    sql += "%s, " % d.find("PM10").text 
    sql += "%s, " % d.find("PM25").text 
    sql += "'%s')" % d.find("IDEX_NM").text
    cur.execute(sql)

con.commit()
cur.close()
con.close()
huc.close()