from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import ssl
import pandas as pd
import os

# 만약 data 폴더가 없다면
if not os.path.exists('../data'):
    # 폴더를 만들어 준다
    os.mkdir('../data')

# 보안을 위한 인증서 우회
context = ssl._create_unverified_context()
# 웹 페이지 접속 웹 브라우저로 접속한 척 하는 코드
headers = {'User-Agent': 'Mozilla/5.0'}

# 뉴스에 보내기
# url = input("URL 입력 : ")
url = 'https://news.naver.com/main/clusterArticles.naver?id=c_202204260850_00000001&mode=LSD&mid=shm&sid1=100&oid=056&aid=0011256180'
# 편지지 생성
request = Request(url, headers=headers)
# 편지지 보내기
response = urlopen(request, context=context)
html = response.read()

# html 구조 가져오기
soup = BeautifulSoup(html, 'html.parser')
result = soup.find_all('a', {'class', 'nclicks(cls_pol.clsart1)'})
# 리스트
titles = []

for r in result:
    # r.text = 테그 안에있는 내용물 만 출력하는 함수
    d = r.text
    # len = 문자열 길이를 구하는 함수
    if len(d) > 10:
        print(r.text)
        # 기사 제목들 만 리스트에 모아둠
        titles.append(r.text)

        # 엑셀과 유사하게 되어있음
        data = pd.DataFrame({'title': titles})
        # 한글이 포함되어 있다면 인코딩이 필요.!
        data.to_csv('../data/titles.cvs', encoding='utf-8')


#print(titles)