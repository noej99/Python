# -*- coding:utf-8 -*-

# 카톡 내보내기
# 채팅내용 txt로

# 대화 내용 내보내기
# 모든 메시지 내부저장소에 저장

# Python이 구려 - x
# 하드웨어쪽 한계
# 1TB짜리 데이터를 RAM이 어떻게 감당을...
# 전처리(1TB짜리 데이터를 서버급 컴 여러대로 병렬처리)
# -> 필요없는 데이터는 제외 -> 50MB
# -> Hadoop(Linux에서만 돌아가는, Java프로그램)

# 파일 읽어서 콘솔에

# 채팅내용부분만 무슨단어가 제일 많이
f = open("C:/noej/sourceFile/KakaoTalkChats.txt", "r", encoding="utf-8")
txt = None
wc = {}
for i, l in enumerate(f.readlines()):
    if i > 6:
        l = l.replace("\n", "")
        if l.startswith("2023년"):
            try:
                txt = l.split(" : ")[1]
            except:
                pass
        else:
            txt = l
        
        if txt != None and txt != "":
            for word in txt.split(" "):
                if word in wc:
                    wc[word] += 1
                else:
                    wc[word] = 1
f2 = open("C:/noej/sourceFile/wcResult.txt","a", encoding="utf-8")
for k, v in wc.items():
    f2.write("%s\t%d\n" % (k, v))
f2.close()

f.close()
