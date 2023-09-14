# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
from json import loads
from cx_Oracle import connect

huc = HTTPSConnection("api.openweathermap.org")

# GET방식 요청
huc.request("GET", "/data/2.5/weather?q=seoul&appid=baff8f3c6cbc28a4024e336599de28c4&units=metric&lang=kr")

# 응답받고 -> 내용 읽어와서
resBody = huc.getresponse().read()
##########################################
# JSON -> Python dict + list
weatherData = loads(resBody)
# list : 변수명[인덱스]
# dict : 변수명[키]

#            sqlplus 아이디/비번@주소:포트/디비이름
con = connect("noej/j2527303@195.168.9.61:1521/xe")

# DB작업 총괄객체 겸 결과객체
cur = con.cursor()

desc = weatherData["weather"][0]["description"]
temp = weatherData["main"]["temp"]
humi = weatherData["main"]["humidity"]
sql = "insert into owm_weather values(sysdate, '%s', %.2f, %d)" % (desc, temp, humi)

# 실행
cur.execute(sql)

# 반영
con.commit()

cur.close()
con.close()
huc.close()