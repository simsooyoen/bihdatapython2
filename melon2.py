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
# 1. 멜론 100곡 출력
# 2. 멜론 50곡 출력
# 3. 멜론 10곡 출력
# 4. AI 추천곡 출력
# 5. 가수 이름 검색
print("===================")
print("1. 멜론 100곡 출력")
print("2. 멜론 50곡 출력")
print("3. 멜론 10곡 출력")
print("4. AI 추천곡 출력")
print("5. 가수 이름 검색")
print("===================")
# 메뉴선택(숫자입력): 1
n = input("메뉴선택(숫자입력):")
print(f"당신이 입력한 값은? {n}")
# 만약에 1을 입력하면
# 멜론 100 출력
if n == "1":
    print("멜론 100")
    # 수집한 데이터를 출력합니다.
    for i in range(100):
        print(f"{songs[i][0]}. {songs[i][1]} - {songs[i][2]}")
# else:
#    print("1이 아닙니다.")
# 만약에 2를 입력하면
# 멜론 50 출력
elif n == "2":
    print("멜론 50")

elif n == "3":
    print("멜론 10")

elif n == "4":
    print("AI 추천곡")
    # 멜론 차트 100 중에서 노래 한곡 추천 해주는 서비스 만들기
    ai_song = random.choice(songs)
    print(f"추천곡은 {ai_song[1]} - {ai_song[2]} 입니다.") 

elif n == "5":
    print("가수 이름 검색")
# ...
# 5를 입력하면 가수 이름 검색할 수 있게 입력창이 또 나와야함
# 이름을 입력하면 해당 가수 이름의 노래 리스트가 출력
else:
    print("1~5까지 입력하세요")
