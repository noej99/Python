# -*- coding:utf-8 -*-
from pymongo.mongo_client import MongoClient
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from http.client import HTTPSConnection, HTTPConnection
from bs4 import BeautifulSoup

# 카카오블로그 글 출력
con = MongoClient("195.168.9.61")
db = con.xe
trainData =[]
label = []
for b in db.kakao_blog.find():
    trainData.append(b["blogname"] + " " + b["title"] + " "  + b["contents"])
    label.append(b["what"])
con.close()

cv = CountVectorizer()
cvResult = cv.fit_transform(trainData).toarray() # 전처리
print(cvResult)
mnb = MultinomialNB().fit(cvResult, label) # 학습

# https://freshsky.tistory.com/116
u = input("블로그 주소 : ")
u = u.split("/")
if u[0] == "https":
    huc = HTTPSConnection(u[2])
else:
    huc = HTTPConnection(u[2])
addr = "/"
for i in range(3, len(u)):
    addr += u[i] + "/"
huc.request("GET", addr)
rb = huc.getresponse().read()
huc.close()

blog = BeautifulSoup(rb, "html.parser", from_encoding="utf-8")
blogResult = cv.transform([blog.text]).toarray()
result = mnb.predict(blogResult)[0]
print(result)