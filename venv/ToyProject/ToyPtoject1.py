#=============== import 시작 =================
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
import matplotlib.font_manager as fm
#=============== import 끝 =================

#================= plot 폰트설정 시작 ============================
# 그래프 마이너스 기호 깨짐을 방지하기 위해 설정
# matplotlib에 - 기호는 유니코드로 되어 있기에 깨짐이 발생할 수 있어 false로 지정
plt.rcParams['axes.unicode_minus'] = False
# 원하는 font 파일 위치를 지정
fontPath = "font/Freesentation-9Black.ttf"
# font를 참조하기 위해 이름을 추출
fontName = fm.FontProperties(fname=fontPath).get_name()
# pyplot rc 설정으로 추출한 font를 적용
plt.rc('font', family=fontName)
#================== plot 폰트 설정 끝 ============================

#===================== 날짜 변환 함수 시작 ========================
#str 타입 날짜 데이터를 date 타입으로 변환하는 함수
def dateType(arr):
    return pd.to_datetime(arr)
#===================== 날짜 변환 함수 끝 =========================

#================= csv 데이터 -> 배열 변환 시작 ===================
################### 검색량 csv 파일 주소 ##################
file_path = "csvFile/"
koreanPancakeCSVArr = [file_path+"2021_부침개_네이버_일간검색트렌드.csv",file_path+"2022_부침개_네이버_일간검색트렌드.csv"
        ,file_path+"2023_부침개_네이버_일간검색트렌드.csv",file_path+"2024_부침개_네이버_일간검색트렌드.csv"]

################### 검색량 배열 생성 ###################
koreanPancakeArr2021 = []
koreanPancakeArr2022 = []
koreanPancakeArr2023 = []
koreanPancakeArr2024 = []
koreanPancakeArr = [koreanPancakeArr2021,koreanPancakeArr2022,koreanPancakeArr2023,koreanPancakeArr2024]

################### 기상청 csv 파일 주소 ###################
file_path_rain = "csvFile/기상청_강수량.csv"

################### 기상청 dataFrame 데이터 생성 ###################
weatherArr = pd.DataFrame(pd.read_csv(file_path_rain,encoding="cp949"))

#================= csv 데이터 -> 배열 변환 끝 ===================

#================= 날짜 배열 생성 시작 =================
yearDate = [2021,2022,2023,2024]
#================= 날짜 배열 생성 끝 ===================

#================ 데이터 타입 날짜로 변경 시작 ===================
################### 기상청 날짜, date Type로 변환 ###################
weatherArr['일시'] = dateType(weatherArr['일시'])
print(weatherArr['일시'])

#searchYear == 년도별 강수량
searchYear = []
# 강수량 출력
for i in range(len(yearDate)):
    #일시 열의 연도가 yearDate에 있는 년도와 같을 때 배열로 저장
    searchYear.append(weatherArr[weatherArr['일시'].dt.year == yearDate[i]])

################### 검색량 날짜 , date Type로 변환 ###################
# 검색량 출력
for i in range(len(koreanPancakeArr)):
    # pd로 csv파일을 읽는다
    koreanPancakeArr[i] = pd.read_csv(koreanPancakeCSVArr[i])
    # period 열 데이터를 날짜 형식으로 변환
    koreanPancakeArr[i]['period'] = dateType(koreanPancakeArr[i]['period'])
#================ 데이터 타입 날짜로 변경 끝 ===================

#======================== 표 설정 및 생성 시작 ==========================
# 그래프 크기를 설정, 가로 15, 세로 10
plt.figure(figsize=(15, 10))

for i in range(len(yearDate)):
    #그래프: 2021-2024년 검색량과 강수량을 함께 표시
    #2*2 플롯 생성 / 위치를 지정
    plt.subplot(2, 2, i+1)
    #각 연도별 검색량 및 강수량 제목을 설정
    plt.title(f'{yearDate[i]} 검색량 및 강수량')
    #검색량 선 그래프를 위한 설정
    plt.plot(
    koreanPancakeArr[i]['period'].dt.day.astype(dtype='str'), # x축 YY-mm-dd 중 d(일자)만 출력
        koreanPancakeArr[i]['searchVolume'], # y축 검색량 출력
        color='#FF0000', # 빨간색으로 선색을 지정
        label=f'{yearDate[i]} 검색량', # 그래프 설명문 지정
        marker='o', # 고점에 마커를 설정
        linestyle='-', # 선 스타일을 실선으로 지정
        alpha=0.7 # 선 투명도를 지정
    )
    plt.ylabel('검색량') # Y축 라벨이름을 지정
    plt.tick_params(axis='y', labelcolor='#FF0000') # Y축 라벨 색을 지정
    plt.legend(loc='upper left') # 검색량 그래프 설명을 왼쪽 위로 지정

    # 강수량 막대그래프
    plt.twinx()  # y축을 공유하는 또 다른 축 생성
    plt.bar(
        searchYear[i]['일시'].dt.day.astype(dtype='str'), # x축 YY-mm-dd 중 d(일자)만 출력
        searchYear[i]['강수량(mm)'], # y 축 강수량으로 출력
        color='#0000D9', # 파란색으로 막대색을 지정
        label=f'{yearDate[i]} 강수량', # 막대 설명문을 지정
        alpha=0.3 # 막대 투명도를 지정
    )
    plt.ylabel('강수량 (mm)') # Y축 라벨이름을 지정
    plt.tick_params(axis='y', labelcolor='#0000D9') # Y축 라벨 색을 지정
    plt.legend(loc='upper right') # 강수량 그래프 설명을 오른쪽 위로 지정

# 전체 제목 설정
plt.suptitle("검색량 및 강수량 (2021-2024)", fontsize=16)
plt.tight_layout() # 플롯 간의 레이아웃을 자동 조정, 겹치지 않도록 지정
plt.subplots_adjust(top=0.9)  # 제목과 서브플롯 간격 조정

# 그래프 출력
plt.show()
#======================== 표 설정 및 생성 끝 ==========================