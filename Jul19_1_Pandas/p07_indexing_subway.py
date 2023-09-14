# -*- coding:utf-8 -*-
import pandas as pd

subwayDF = pd.read_csv("C:/noej/sourceFile/data/csv/subway.csv", names=["년", "월", "일", "노선", "역", "탑승", "하차"])
print(subwayDF)
print("-----")
print(subwayDF.tail(3)) # 마지막 3개
print("-----")
print(subwayDF.head()[["년", "월", "일"]]) # 첫 5개 날짜
print("-----")
print(subwayDF.iloc[10:16]) # 10 ~ 15번 데이터
print("-----")
print(subwayDF.iloc[20][["노선", "역"]]) # 20번데이터 노선, 역이름
print("-----")
subwayDF = subwayDF.set_index(subwayDF["노선"]) # 노선번호로 찾을 수있게 세팅
print(subwayDF.loc["2호선"]) # 2호선만
print("-----")

# 3호선 역명 탑승 하차 수
print(subwayDF.loc["3호선"][["역", "탑승", "하차"]])
print(subwayDF.loc["3호선",["역", "탑승", "하차"]])
print("-----")

# 탄 사람 수가 5만 넘는거
print(subwayDF[subwayDF["탑승"] > 50000])
print("-----")

# 내린 사람수가 100명 안되는거 년,월,일,노선,역
print(subwayDF[subwayDF["하차"] < 100][["년", "월", "일", "노선", "역"]])
print("-----")

# 서울역
# subwayDF = subwayDF.set_index(subwayDF["역"])
# print(subwayDF.loc["서울역"])
print(subwayDF[subwayDF["역"] == "서울역"])
print("-----")

# 역이름에 '서울'이 들어가는거
#                                startswith
#                                endswith
#                                contains
print(subwayDF[subwayDF["역"].str.contains("서울")])
print("-----")

# 역이름에 '입구'들어가는 노선, 역명
print(subwayDF[subwayDF["역"].str.contains("입구")][["노선", "역"]])
print("-----")

print(subwayDF.shape[0])

# for문으로 하나하나 나오게
for i in range(subwayDF.shape[0]):
    print(subwayDF.iloc[i])
    print("-----------")


