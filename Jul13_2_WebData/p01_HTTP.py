# -*- coding:utf-8 -*-
from http.client import HTTPSConnection

# https://www.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=가나다라마바사

# http or https
# huc = HTTPConnection("주소:포트")
# 연결
huc = HTTPSConnection("www.kma.go.kr") # 서버
# 요청
huc.request("GET", "/wid/queryDFSRSS.jsp?zone=1111061500") # 폴더/파일/파라메터/...
# 응답
res = huc.getresponse()
# 응답내용
resBody = res.read()
# 응답내용 한글처리해서
print(resBody.decode())

huc.close()