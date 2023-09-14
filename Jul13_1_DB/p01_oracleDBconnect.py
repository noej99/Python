# -*- coding:utf-8 -*-

###########################################################
# SQLPlus : OracleDB서버에 접속해서 제어하는 프로그램(정품)
#           -> 근데 cmd기반이라 불편
#           -> EclipseIDE로 OracleDB를 제어하자
# https://dbeaver.io/ - download - 
###########################################################

# J
#    DB메이커가 다양한데 그걸 Java에서 어찌 다 감당을
#    각 DB마다 연결할때 쓰는 driver가 필요
#    ojdbc??.jar

# P
#    DB메이커가 다양한데 그걸 Java에서 어찌 다 감당을
#    각 DB마다 연결할때 쓰는 driver가 필요
#    cx_Oracle.py(ojdbc??.jar을 사용) -> pip
#    cmd -> pip install cx_Oracle

# cmd
#    pip install 이름

#    cx_Oracle.py가 ojdbc??.jar가 어디에 있는지 모르니까 찾을 수 있게
#        instantclient폴더 경로 복사해놓고
#            C:\noej\clientDB\instantclient_21_9
#        PATH
#            내 PC - 속성 - 고급 시스템 설정
#            고급 - 환경 변수 
#            Path에 instantclient폴더 경로 새로만들기 
#            (위에는 로그인한 계정만 아래는 모든 계정 적용)

#    Eclipse 자동완성(아나콘다로 인한 충돌 때문에 설정)
#        Window - Preferences
#        PyDev - Interpreters - Python Interpreter
#        - Forced Builtins - New - cx_Oracle추가

###########################################################
from cx_Oracle import connect
try:
    # sqlplus에서 연결할때 쓰는 양식
    #               아이디/비번@주소:포트/SID
    con = connect("noej/j2527303@195.168.9.61:1521/xe")
    print("성공")
    con.close()
except Exception as e:
    print(e)
###########################################################