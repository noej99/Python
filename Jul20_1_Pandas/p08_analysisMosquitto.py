# -*- encoding:utf-8 -*-

import pandas as pd
import numpy as np

df = pd.read_csv("C:/noej/sourceFile/data/csv/mosquitto.csv", names=["날짜", "물가", "집", "공원"])
print(df)
print("----")
print(df["물가"].isnull())
print("----")
print(df[df["물가"].isnull()])
print("----")


# None이라는 글자가 있음(xml파싱, 입력하는 과정에서 발생)
# 123, "None" -> object
print(df[df["물가"] == "None"])
print("----")

# "None" -> 없게
df["물가"] = df["물가"].replace("None", np.nan)
df["집"] = df["집"].replace("None", np.nan)
df["공원"] = df["공원"].replace("None", np.nan)

# 필드 형변환 -> int
df["물가"] = pd.to_numeric(df["물가"])
df["집"] = pd.to_numeric(df["집"])
df["공원"] = pd.to_numeric(df["공원"])

# 필드 형변환(글자로)
# df["물가"] =  df["물가"].astype(str) 

# 없는거는 평균치로 채워서
df["물가"] = df["물가"].fillna(df["물가"].mean())
df["집"] = df["집"].fillna(df["집"].mean())
df["공원"] = df["공원"].fillna(df["공원"].mean())

# 물가/집/공원 평균치
df["평균"] = (df["물가"] + df["집"] + df["공원"]) / 3
print(df)
print("----")

# 모기가 가장 심했던 날 언제
print(df[df["평균"] == df["평균"].max()]["날짜"])


