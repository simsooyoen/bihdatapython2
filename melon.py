import requests
from bs4 import BeautifulSoup

# User-Agent 설정
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# 멜론 차트 TOP100 URL
url = 'https://www.melon.com/chart/index.htm'

# HTTP 요청
response = requests.get(url, headers=headers)

# HTML 소스 코드 파싱
soup = BeautifulSoup(response.text, 'html.parser')

# 곡 정보 가져오기
songs = soup.select('.lst50, .lst100')  # lst50과 lst100 클래스를 가진 요소 선택

# 결과 출력
for song in songs:
    title = song.select_one('.ellipsis.rank01 a').text  # 곡 제목
    artist = song.select_one('.ellipsis.rank02 a').text  # 아티스트 이름
    album = song.select_one('.ellipsis.rank03 a').text  # 앨범 이름
    print(f'곡명: {title}, 아티스트: {artist}, 앨범: {album}')