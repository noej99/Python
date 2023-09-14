# -*- encoding:utf-8 -*-

import pandas as pd

df = pd.read_csv("C:/noej/sourceFile/data/csv/titanic.csv")
print(df)
print("-----")

# 이름, 성별 필드 빼고 다 지우기
df = df[["Name", "Sex"]]

# male -> 남자, female -> 여자
df["Sex"] = df["Sex"].replace({"male":"남자", "female":"여자"})

# 이름에서 Mr ->  미스터
# 함수를 생성하여 .apply(함수명)
def replaceMr(t):
    return t.replace("Mr", "미스터")
df["Name"] = df["Name"].apply(replaceMr)
print(df)
print("-----")

# 이름에서 성떼고 이름만 남기기
# lambda함수로도 가능
# def removeFamilyName(n):
#     return n.split(",")[0]
# df["Name"] = df["Name"].apply(removeFamilyName)
df["Name"] = df["Name"].apply(lambda n:n.split(",")[0])
print(df)
print("-----")

# def getHab(a, b):
#     return a + b
# c = getHab(10, 20)
c = (lambda a, b: a + b)(10, 20)
print(c)
print("-----")

df = pd.read_csv("C:/noej/sourceFile/data/csv/titanic.csv")

# 나이대별로 산사람/죽은사람수
print(df[df["Age"].isnull()])
df["Age"] = df["Age"].fillna(900)

df["대"] = df["Age"].apply(lambda a: "%d0대" % (a//10))
df["대"] = df["대"].replace("900대", "모름")
print(df)

# 10대
print(df.groupby(df[df["대"] == "20대" ]["Survived"])["PassengerId"].count())
# 20대
print(df.groupby(df[df["대"] == "30대" ]["Survived"])["PassengerId"].count())
# 30대
print(df.groupby(df[df["대"] == "40대" ]["Survived"])["PassengerId"].count())
# ...
# 모름
print(df.groupby(df[df["대"] == "모름" ]["Survived"])["PassengerId"].count())





