import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

#================= plot 폰트설정 시작 ============================
plt.rcParams['axes.unicode_minus'] = False
fontName = fm.FontProperties(fname="font/Freesentation-9Black.ttf").get_name()
plt.rc('font', family=fontName)
#================== plot 폰트 설정 끝 ============================

#str 타입 날짜 데이터를 date 타입으로 변환하는 함수
def dateType(arr):
    return pd.to_datetime(arr)

file_path = "csvFile/09/"
koreanPancakeCSVArr = [file_path+"2021_부침개_네이버_일간검색트렌드.csv",file_path+"2022_부침개_네이버_일간검색트렌드.csv"
    ,file_path+"2023_부침개_네이버_일간검색트렌드.csv",file_path+"2024_부침개_네이버_일간검색트렌드.csv"]

koreanPancakeArr2021 = []
koreanPancakeArr2022 = []
koreanPancakeArr2023 = []
koreanPancakeArr2024 = []
koreanPancakeArr = [koreanPancakeArr2021,koreanPancakeArr2022,koreanPancakeArr2023,koreanPancakeArr2024]

weatherCSVArr = "csvFile/09/기상청_강수량.csv"
yearArr = ['2021','2022','2023','2024']

#window 공공데이터 csv 파일은 cp949 or enc-kr 이기때문에
# cp949로 변환하여 데이터 저장
weatherArr = pd.DataFrame(pd.read_csv(weatherCSVArr,encoding="cp949"))

#년도만 비교하기 위해 일시 데이터를 년도로 변경
weatherArr['일시'] = dateType(weatherArr['일시']).dt.year
# koreanPancakeArr+yearArr[0].append()
print([data for data in weatherArr])

# print(koreanPancakeArr[0])
# for i in range(len(yearArr)):
#     if yearArr[i] == weatherArr['일시']:
#         print(weatherArr)



# print(koreanPancakeArr)
# for i in range(len(koreanPancakeCSVArr)):
#     with open(koreanPancakeCSVArr[i], mode='r',encoding="UTF-8") as file :
#         reader = csv.reader(file)
#         header = next(reader)
#         for row in reader:
#             koreanPancakeArr[i].append(row)

#아래 for문을 하드코딩한
# koreanPancakeArr[0] = pd.read_csv(koreanPancakeCSVArr[0])
# koreanPancakeArr[1] = pd.read_csv(koreanPancakeCSVArr[1])
# koreanPancakeArr[2] = pd.read_csv(koreanPancakeCSVArr[2])
# koreanPancakeArr[3] = pd.read_csv(koreanPancakeCSVArr[3])

#각 배열열에 csv 데이터를 추출
for i in range(len(koreanPancakeArr)):
    koreanPancakeArr[i] = pd.read_csv(koreanPancakeCSVArr[i])
    koreanPancakeArr[i]['period'] = dateType(koreanPancakeArr[i]['period'])

plt.title('부침개 검색량')
plt.plot(koreanPancakeArr[0]['period'].dt.day.astype(dtype='str'),koreanPancakeArr[0]['searchVolume'])
plt.plot(koreanPancakeArr[1]['period'].dt.day.astype(dtype='str'),koreanPancakeArr[1]['searchVolume'])
plt.plot(koreanPancakeArr[2]['period'].dt.day.astype(dtype='str'),koreanPancakeArr[2]['searchVolume'])
plt.plot(koreanPancakeArr[3]['period'].dt.day.astype(dtype='str'),koreanPancakeArr[3]['searchVolume'])
plt.show()