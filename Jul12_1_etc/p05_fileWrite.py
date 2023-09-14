# -*- coding:utf-8 -*-

# open(경로, 모드, ..)
#                        r
#                        w
#                        a
ff = open("C:/noej/sourceFile/1.txt", "a", encoding="utf-8")
ff.write("ㅋㅋㅋ\n")
ff.write("ㅇㅇㅇ\n") # \n만 써도
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