# -*- coding:utf-8 -*-

class WordCount:
    def __init__(self, w, c):
        self.word = w
        self.count = c
    
    def show(self):
        print(self.word, self.count)
############################
# 결과파일 읽어와서 출력
f = open("C:/noej/sourceFile/wcResult.txt", "r", encoding="utf-8")
wcs = []
for l in f.readlines():
    l = l.replace("\n", "").split("\t")
    wc = WordCount(l[0], int(l[1]))
    wcs.append(wc)

# (lambda p1, p2, ...:리턴)(값,값,...)
# python이 알아서 객체 하나씩
wcs.sort(key=(lambda wcwc:wcwc.count), reverse=True)
# wcs.sort(key=(lambda wcwc:wcwc.word))
for v in wcs:
    v.show()
f.close()