# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
from json import loads

############################################################
# JSON : 데이터를 JavaScript에서 객체+배열 표현하는 방식으로
# [] : JS의 배열/Python list
# {} : JS의 객체/Python dict
############################################################
# l = ["a", "b", "c"]
# l[0]
# for v in l:
#    v사용
#################################
# d = {"a" : 1, "b" : 2}
# v["a"]

huc = HTTPSConnection("api.openweathermap.org")
huc.request("GET", "/data/2.5/weather?q=seoul&appid=baff8f3c6cbc28a4024e336599de28c4&units=metric&lang=kr")
resBody = huc.getresponse().read()
weatherData = loads(resBody) # JSON -> Python 컬렉션

print(weatherData["weather"][0]["description"])
print(weatherData["main"]["temp"])
print(weatherData["main"]["humidity"])

huc.close()