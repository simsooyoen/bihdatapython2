import requests
from bs4 import BeautifulSoup

url = 'https://ticket.melon.com/concert/index.htm?genreType=GENRE_ART'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

rankings = soup.select('.some_css_class')  # 실제 CSS 클래스명으로 변경해야 함

for ranking in rankings:
    title = ranking.select_one('.title_css_class').get_text()  # 제목 CSS 클래스명을 사용
    artist = ranking.select_one('.artist_css_class').get_text()  # 아티스트 CSS 클래스명을 사용
    print(f'제목: {title}, 아티스트: {artist}')