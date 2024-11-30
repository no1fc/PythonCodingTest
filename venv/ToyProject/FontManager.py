import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# platform.system() == 'Windows' #윈도우
# plt.rc('font', family='Malgun Gothic')
#!wget "https://www.wfonts.com/download/data/2016/06/13/malgun-gothic/malgun.ttf"
#!mv malgun.ttf /usr/share/fonts/truetype/
#import matplotlib.font_manager as fm
#fm._rebuild()
# plt.rc('font', family='Malgun Gothic')
#한글 폰트 사용시 마이너스 폰트 깨짐 해결
plt.rcParams['axes.unicode_minus'] = False
#font 이름을 받아오기 위해, matplotlib에 있는 font_manager를 사용
# font_manager에서 받아온 폰트이름으로
# plot 표에 있는 폰트를 변경
fontName = fm.FontProperties(fname="font/Freesentation-9Black.ttf").get_name()
plt.rc('font', family=fontName)
#matplotlib 패키지 한글 깨짐 처리 끝

##########데이터 로드

df = pd.DataFrame([
    ['A01', 2, 1, 60, 139, 'country', 0, 3],
    ['A02', 3, 2, 80, 148, 'country', 0, 5],
    ['A03', 3, 4, 50, 149, 'country', 0, 7],
    ['A04', 5, 5, 40, 151, 'country', 0, 10],
    ['A05', 7, 5, 35, 154, 'city', 0, 12],
    ['A06', 2, 5, 45, 149, 'country', 0, 7],
    ['A07',8, 9, 40, 155, 'city', 1, 13],
    ['A08', 9, 10, 70, 155, 'city', 3, 13],
    ['A09', 6, 12, 55, 154, 'city', 0, 12],
    ['A10', 9, 2, 40, 156, 'city', 1, 13],
    ['A11', 6, 10, 60, 153, 'city', 0, 12],
    ['A12', 2, 4, 75, 151, 'country', 0, 6]
], columns=['ID', 'hour', 'attendance', 'weight', 'iq', 'region', 'library', 'score'])

##########데이터 분석

plt.plot(df['ID'], df['score']) #x축, y축
plt.title('선 그래프')
plt.xlabel('아이디')
plt.ylabel('점수')
plt.show()