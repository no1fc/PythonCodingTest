#=============== import 시작 =================
import ToyProject1
import matplotlib.pyplot as plt
import pandas as pd
#=============== import 끝 =================

#================= csv 데이터 -> 배열 변환 시작 ===================
def csvFile(file_path):
    ################### 검색량 csv 파일 주소 ##################
    return [file_path+"2021_부침개_네이버_일간검색트렌드.csv",file_path+"2022_부침개_네이버_일간검색트렌드.csv"
        ,file_path+"2023_부침개_네이버_일간검색트렌드.csv",file_path+"2024_부침개_네이버_일간검색트렌드.csv"]

################### 기상청 dataFrame 데이터 생성 ###################
def pandasDataFrame(file_path):
    ################### 기상청 csv 파일 주소 ###################
    return pd.DataFrame(pd.read_csv(file_path+"기상청_강수량.csv",encoding="cp949"))

#월별 폴더 주소
file_path = ToyProject1.resource_path("csvFile/07/")
koreanPancakeCSVArr07 = csvFile(file_path)
weatherArr07 = pandasDataFrame(file_path)
#월별 폴더 주소
file_path = ToyProject1.resource_path("csvFile/09/")
koreanPancakeCSVArr09 = csvFile(file_path)
weatherArr09 = pandasDataFrame(file_path)

#================= csv 데이터 -> 배열 변환 끝 ===================

#================= 날짜 배열 생성 시작 =================
yearDate = [2021,2022,2023,2024]
#================= 날짜 배열 생성 끝 ===================
print(yearDate)
print(koreanPancakeCSVArr07)
print(koreanPancakeCSVArr09)
ToyProject1.plotKoreanPancake(koreanPancakeCSVArr07,weatherArr07,yearDate)
ToyProject1.plotKoreanPancake(koreanPancakeCSVArr09,weatherArr09,yearDate)
print(weatherArr07)
print(weatherArr09)
# 그래프 출력
plt.show()