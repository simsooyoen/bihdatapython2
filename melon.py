import requests
from bs4 import BeautifulSoup

# 멜론 주간 차트 URL
url = 'https://www.melon.com/chart/week/index.htm'

# User-Agent 설정하여 요청
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)

# HTML 소스 가져오기
html = response.text

# BeautifulSoup을 통한 HTML 파싱
soup = BeautifulSoup(html, 'html.parser')

# 음악 정보 추출
songs = soup.select('tr[data-song-no]')
for song in songs:
    rank = song.select_one('span.rank').text.strip()  # 순위
    title = song.select_one('div.ellipsis.rank01 a').text.strip()  # 곡 제목
    artist = song.select_one('div.ellipsis.rank02 a').text.strip()  # 가수
    album = song.select_one('div.ellipsis.rank03 a').text.strip()  # 앨범

    print(f'순위: {rank}, 곡 제목: {title}, 아티스트: {artist}, 앨범: {album}')