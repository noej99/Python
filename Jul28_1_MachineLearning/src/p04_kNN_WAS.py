# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
from cx_Oracle import connect
from sklearn.preprocessing._data import MinMaxScaler
from sklearn.neighbors._classification import KNeighborsClassifier
from http.client import HTTPSConnection
from json import loads
from flask.app import Flask
from flask.helpers import make_response
from flask.json import jsonify
from datetime import datetime

# 학습데이터는 게시판에 글 쓸떼마다 늘고있고
# 요청할때마다
# 오라클DB에서 다 가져와서?

# 업데이트를 하기는 해야 요청 받을때마다 하기는...

# 새벽에 해놓기

# Spring웹사이트
# 게시판에 글 쓸때마다 OracleDB에 날씨, 색깔

app = Flask(__name__)
mms = MinMaxScaler()
knc = KNeighborsClassifier(7)
weathers = None
day = -1

def trainAI():
    global weathers
    con = connect("noej/j2527303@195.168.9.61:1521/xe")
    sql = "select * from sp_weather_color"
    df = pd.read_sql(sql, con)
    print(df)
    con.close()
    
    # 날씨를 숫자로 인코딩
    weathers =list(df["SWC_DESCRIPTION"].unique())
    df["SWC_DESCRIPTION"] = df["SWC_DESCRIPTION"].apply(lambda d : weathers.index(d))
    
    trainData = df[["SWC_TEMP", "SWC_HUMIDITY", "SWC_DESCRIPTION"]].to_numpy()
    label = df["SWC_COLOR"].to_numpy()
    trainData = mms.fit_transform(trainData)
    knc.fit(trainData, label)

def getWeather():
    huc = HTTPSConnection("api.openweathermap.org")
    huc.request("GET", "/data/2.5/weather?appid=baff8f3c6cbc28a4024e336599de28c4&q=seoul&units=metrics&lang=kr")
    rb = huc.getresponse().read()
    weatherData = loads(rb)
    temp = weatherData['main']['temp']
    humi = weatherData['main']['humidity']
    desc = weatherData['weather'][0]['description']
# 인코딩(처음 나오는 날씨면 -1로)
    try:
        desc = weathers.index(desc)
    except:
        desc = -1
    huc.close()
    return temp, humi, desc
# temp = float(input("기온 : "))
# humi = float(input("습도 : "))
# desc = input("날씨 : ") # 인코딩
    
@app.route("/color.get")
def colorGet():
    global day
    # 새벽시간이면
    # 날짜 바뀌고 첫 호출
    todayDay = datetime.today().day
    if day != todayDay:
        trainAI()
        print("학습")
        day = todayDay
        
    temp, humi, desc = getWeather()
    predictData = np.array([[temp, humi, desc]])
    predictData = mms.transform(predictData)
    result = knc.predict(predictData)[0]
    return make_response(jsonify({"color":"#"+ result})), {"Access-Control-Allow-Origin" : "*"}

if __name__=="__main__":
    app.run("0.0.0.0", 1234, debug=True)