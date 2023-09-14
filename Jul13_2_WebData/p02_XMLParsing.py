# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
from xml.etree.ElementTree import fromstring

# http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1111061500

huc = HTTPSConnection("www.kma.go.kr") # 서버
huc.request("GET", "/wid/queryDFSRSS.jsp?zone=1111061500") # 폴더/파일/파라메터/...
resBody = huc.getresponse().read()
##########################################
# XML피싱
kmaData = fromstring(resBody)
weathers = kmaData.getiterator("data")  # <data></data>들
                                        # $(kmaData).find("data")
for w in weathers:
    print(w.find("hour").text) # <hour>18</hour>
    print(w.find("temp").text) 
    print(w.find("wfKor").text)
    
huc.close()