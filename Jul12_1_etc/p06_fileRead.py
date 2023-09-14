# -*- coding:utf-8 -*-

# open(경로, 모드, ..)
#                        r
#                        w
#                        a
ff = open("C:/noej/sourceFile/1.txt", "r", encoding="utf-8")

# a = ff.read() # 전체 다 읽어서, str하나로
# print(a)
# print(type(a))

# b = ff.readline() # 다음 한 줄 읽어서, str하나로
# print(b)
# b = ff.readline() 
# print(b)
# print(type(b))

# 전체 다 읽어서, 엔터키 기준으로 나눠서 list
c = ff.readlines() 
print(c)
print(type(c))

lines = ff.readlines()
for l in lines:
    l = l.replace("\n", "")
    print(l)

ff.close
# J
#   통일된 시스템
#   무슨 입/출력 장치든간에(파일, Socket, HttpRes, ...)
#   InputStream -> InputStreamReader -> BufferReader
#   OutputStream
#   어디다 입/출력을 하든지 소스가 다 똑같
#   소스가 길다

# P
#   다 다름
