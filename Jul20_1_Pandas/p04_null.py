# -*- encoding:utf-8 -*-
import pandas as pd

df = pd.read_csv("C:/noej/sourceFile/data/csv/lnps.csv", names=["어디", "뭐", "가격", "종류", "구"])
print(df)
print("---------")

print(df["뭐"].isnull()) # 값이 없나?(T/F)
print(df[df["뭐"].isnull()])
print("---------")

# 결측값(없는거) -> '없음
df["뭐"] = df["뭐"].fillna("없음")

# 상품명에 사과 포함된거 조회
print(df[df["뭐"].str.contains("사과")])
print("---------")

# '없음' -> 결측값
# Pandas로 결측값이 표현 불가 -> numpy로
import numpy as np
df["뭐"] = df["뭐"].replace("없음", np.nan)
print(df[df["뭐"].isnull()])
# print(df[df["뭐"].str.contains("사과")])
