import csv
import matplotlib.pyplot as plt # pyplt이라 부른다.
#인터프리터 언어에서는 대부분
# as(별칭)을 지원한다.

# matplotlib는 jsoup, ojdbc6.jar 같은 라이브러리라 설치가 필요하다.
#pip install matplotlib

## 3번째 일시
## 4번째 평균기온

## Python에서는 _(언더바)가 더 보편적으로 사용된다.
## Java등의 언어에서는 다양한 함수,메서드를 사용하기 때문에 카멜표기법이 더 유용하다.
file_path = "test.csv"
# Python 파일입출력 기본 코드
# with open(파일명, mode='어떤 모드로 열지', encoding="UTF-8") as 객체명:
dateList = [] #변수명 dates(요즘 사용), data_list(python에서 사용)
tempList = []

with open(file_path, mode='r') as file :
    ##reader 등의 색이 변하지 않는 함수는 내장 함수가 아니기 때문에
    ##import 받아와야한다.
    reader = csv.reader(file) # Java에서는 패키지, 파이썬에서는 모듈이라 부른다.
    #기본 for문
    # for i in range()
    #향상된 for문 -> 이번에 사용할 예정
    # for i in 객체

    # if 첫번째시도면: <- for,while 반복문에 한번만 실행된다면 / 함정 코드, 성능 저하 코드이다.
    # 반복문안에있는 어떤 로직, 조건이 딱 1번 수행되는데
    ## 이는 1번만 진행하면 되기 때문에 성능 저하가 발생할 수 있다.
    #list 한줄을 읽을 때 next()매서드를 활용하면 된다.
    # 보통 불러온 첫줄은 header에 저장한다.
    header = next(reader)

    for row in reader:
        #Python에서는 문자를 보여줄때는 ,(콤마)를 사용하여 보여준다.
        a=row[2]
        b=row[3]
        c=row[-2]
        # if a가 Dec 시작하면 :
        if a.startswith("Nov"):
            print("일시 : ",a," 평균기온 : ",b," 최저기온 : ",c)## print(row) 한번당 List로 확인이 가능하다.
            dateList.append(a)
            tempList.append(float(c))
# -----------------------------------------------------------------------------------------------------
# 2024-11-26 내용
#그래프를 그리고()
# plt.plot(x축데이터, y축데이터)
# plt.plot(dateList, tempList,marker="o",color="r",linestyle=":",linewidth=2,markersize=10)
plt.plot(dateList, tempList,color="#025",linestyle="dashdot")
plt.bar(dateList, tempList,color="#025586")
#그래프 제목달기
plt.title("Temperature in December",fontsize=10)
#그래프 X축 명칭
plt.xlabel("Date",fontsize=10)
#그래프 Y축 명칭
plt.ylabel("Temperature",fontsize=10)
#그린 그래프를 화면에 출력해줘()
plt.show()