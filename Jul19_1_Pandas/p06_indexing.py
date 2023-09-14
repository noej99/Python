# -*- coding:utf-8 -*-
import pandas as pd

titanicDF = pd.read_csv("C:/noej/sourceFile/data/csv/titanic.csv")
print(titanicDF)
print("-----")
print(titanicDF.shape) # 몇행몇열
print("-----")
print(titanicDF.columns) # 필드명들
print("-----")
print(titanicDF.head()) # 앞에서부터 몇개 - 기본값은 5개
print("-----")
print(titanicDF.tail(2)) # 뒤에서부터 몇개 - 기본값은 5개

print("열(필드) 기준=====")
print(titanicDF["Name"]) # 변수명["필드명"]
print("-----")
print(titanicDF.Name) # 변수명.필드명
print("-----")
print(titanicDF[["Name", "Age"]]) # 변수명[list형태로 필드명들]

print("행(데이터) 기준=====")
print(titanicDF.iloc[0])# 번호로 데이터 : 변수명.iloc[번호]
print("-----")
print(titanicDF.iloc[0:3]) # 0 ~ (3-1)번 데이터
print("-----")
titanicDF = titanicDF.set_index(titanicDF["Name"]) # 찾는 기준 설정 변수명.set_index(변수명["설정할 index"])
print(titanicDF.loc["Braund, Mr. Owen Harris"])
print("-----")
print(titanicDF.iloc[1]) # 번호로
print("-----")
print(titanicDF.loc["Braund, Mr. Owen Harris"]) # 설정한 index로
print(titanicDF.loc["Braund, Mr. Owen Harris":"Allen, Mr. William Henry"])

print("열 + 행(데이터의 특정 필드) 조회=====")
print(titanicDF.loc["Braund, Mr. Owen Harris"]["Age"]) # 변수명.loc["?"]["필드명"]
print("-----")
print(titanicDF.loc["Braund, Mr. Owen Harris", "Age"]) # 변수명.loc["?", "필드명"])

print("조건으로 조회=====")
print(titanicDF[titanicDF["Age"] > 30]) # True/False
print("-----")
# 20대
# 20 <= titanicDF["Age"] <= 29
# 20 <= titanicDF["Age"] and titanicDF["Age"] <= 29
#                        && : 중간에 생략되는 버전
# NumPy/Pandas에서는 중간에 생략되는 버전을 쓰면 안되니
# and -> &
# or -> |
print(titanicDF[(titanicDF["Age"] >= 20) & (titanicDF["Age"] <= 29)])
print("-----")