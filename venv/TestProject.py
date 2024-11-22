import requests
from bs4 import BeautifulSoup

# 크롤링할 링크
url = "https://news.naver.com/section/105"
# 크롤링할 내용(select)를 입력
soupSelect = "li > div > div > div.sa_text > a > strong"

# URL(Naver 뉴스)로 응답을 받기 위해 requests.get() 메서드 사용
response = requests.get(url)

# BeautifulSoup 객체를 생성해 HTML 파싱
soup = BeautifulSoup(response.text, "html.parser")

# 지정한 CSS 셀렉터를 사용해 제목을 추출
headlines = soup.select(soupSelect)

# headlines가 비어있지 않다면
if headlines:
    # 데이터 하나씩 Text 값 추출
    for headline in headlines:
        print(headline.text.strip())
# 만약 없다면
else:
    # 로그를 출력하여 비어있다고 알려줌
    print("비어있는 select 입니다.")
