# -*- encoding:utf-8 -*-
import pandas as pd

df = pd.read_csv("C:/noej/sourceFile/data/csv/lnps.csv", names=["어디", "뭐", "가격", "종류", "구"])
print(df)
print("---------")

print(df["가격"].max())
print(df["가격"].min())
print(df[df["가격"] == df["가격"].min()])
print("---------")
print(df["가격"].mean())
print(df["가격"].median()) # 중앙값
print(df["가격"].sum())
print(df["가격"].count())
print(df["가격"].var()) # 분산
print(df["가격"].std()) # 표준편차
print("---------")
print(df["가격"].mode()) # 최빈값(제일 자주 나오는 값) => Series
print(df["어디"].mode()[0])
print("---------")
print(df["가격"].describe()) # 다
print(df.describe()) # 필드 중에 숫자 있는거 알아서 다
