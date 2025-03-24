import requests
from bs4 import BeautifulSoup

# 뮤지컬 작품 인기 순위를 조사할 URL
url = 'https://example.com/musical-ranking'

# HTTP 요청 보내기
response = requests.get(url)

# 응답이 정상인지 확인
if response.status_code == 200:
    # HTML 문서 파싱
    soup = BeautifulSoup(response.text, 'html.parser')

    # 인기 순위 정보가 담긴 태그 선택 (예: 'h2' 태그의 'ranking-title' 클래스)
    titles = soup.select('h2.ranking-title')
    ranks = soup.select('span.rank')

    # 데이터 출력
    for rank, title in zip(ranks, titles):
        print(f"{rank.text}: {title.text}")
else:
    print('웹 페이지를 가져오는 데 실패했습니다.')