# -*- coding:utf-8 -*-

# 콘솔출력 : 중간 확인용 -> 줄 바뀌는게 보기 편함

# System.out.println("ㅋ");
print("ㅋ")

# 줄 안바뀌는거
# System.out.print("ㅋ");
print("안", end="")
print("녕")

# System.out.printf("%d", 10); - x
# System.out.println(String.format("%d", 10));
print("%d" % 10)
print("%.2f" % 1.23456)
print("키 : %.1fcm\n몸무게 : %.1fkg" % (158.4, 48.6))

# % : %d, %02d, %f, %.2f, %s
# \ : \t, \n, \r, \\, \"

# 명함
print("*****************")
print("*이름:\t%s\t*\n*나이:\t%d\t*\n*집:\t%s\t*" % ("정윤호", 25, "서울"))
print("*****************")

# { "name" : "홍길동", "age" : 30 }

print("{ \"name\" : \"홍길동\", \"age\" : 30 }")