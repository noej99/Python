# -*- encoding:utf-8 -*-

import pandas as pd

df = pd.read_csv("C:/noej/sourceFile/data/csv/rjResult.txt", sep="\t", names=["단어", "횟수"])

print(df)
print("---------")
df = df.sort_values(by="횟수", ascending=False)
print(df)
print("---------")
print(df.head(10))