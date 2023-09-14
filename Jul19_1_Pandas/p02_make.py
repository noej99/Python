# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

# Python list
a = pd.DataFrame() # DataFrame
a["이름"] = ["홍길동", "고길동"] # 변수명["필드명"] = Python list 
a["나이"] = [45, 36]
print(a)
print("------")

# np.array
b = pd.DataFrame()
b["이름"] = np.array(["홍길동", "고길동"]) # 변수명["필드명"] = np.array
b["나이"] = np.array([45, 36]) 
print(b)
print("------")

# 2차원 list/np.array
# c = [["홍길동", 45], ["고길동", 36]]
c = np.array([["홍길동", 45], ["고길동", 36]])
c = pd.DataFrame(c, columns=["이름", "나이"])
print(c)
print("------")

# dict + List
d = {"이름": ["홍길동", "고길동"], "나이": [45, 36]}
d = pd.DataFrame(d)
print(d)
print("------")

# list + dict
e = [{"이름": "홍길동", "나이": 45}, {"이름": "고길동", "나이": 36}]
e = pd.DataFrame(e)
print(e)




