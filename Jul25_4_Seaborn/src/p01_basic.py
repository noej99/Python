# -*- coding:utf-8 -*-

# pip install seaborn
import pandas as pd
import seaborn as sns
from cx_Oracle import connect
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# FontFile = "C:/Windows/Fonts/malgun.ttf"
# fontName = fm.FontProperties(fname=FontFile, size=10).get_name()
# plt.rc("font", family=fontName)

con = connect("noej/j2527303@195.168.9.61:1521/xe")
sql = "select * from owm_weather order by ow_date"

df = pd.read_sql(sql, con)
con.close()
print(df)

# 알아서
# sns.lineplot(data=df, palette="summer")

# 필드지정
sns.lineplot(x='OW_DATE', y='OW_TEMP', data=df, palette="summer")
plt.title("날씨")
plt.show()

# Matplotlib : np.array대상, 직접 다 설정
# Seaborn : Matplotlib을 쓰기 편하게 해주는 lib
#       pd.DataFrame대상
#       자동으로 그림
#       부족한거 Matplotlib로
#       테마기능