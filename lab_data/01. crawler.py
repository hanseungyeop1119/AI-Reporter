from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import ssl

# 보안을 위한 인증서 우회
context = ssl._create_unverified_context()
# 웹 페이지 접속 web browser 로 접속한 척 하는 코드
headers = {'User-Agent': 'Mozilla/5.0'}

# 뉴스에 보내기
url = 'https://news.naver.com/'
# url = 'https://news.naver.com/main/clusterArticles.naver?id=c_202204260850_00000001&mode=LSD&mid=shm&sid1=100&oid=056&aid=0011256180'

# 편지지 생성
request = Request(url, headers=headers)

# 편지지 보내기
response = urlopen(request, context=context)
html = response.read()

# html 구조 가져오기
soup = BeautifulSoup(html, 'html.parser')

result = soup.find_all('div', {'class', 'cjs_t'})

# 리스트
titles = []

for r in result:
    # r.text = 테그 안에 있는 내용물 만 출력 하는 함수
    print(r.text)
    # 기사 제목들 만 리스트 에 모아둠
    titles.append(r.text)
print(titles)
