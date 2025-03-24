import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# ✅ 웹 드라이버 설정 (User-Agent 추가)
options = Options()
options.add_argument("--headless")  # 브라우저 창을 띄우지 않음
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

# ✅ 크롬 드라이버 실행
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# ✅ 멜론 차트 페이지 접속
url = "https://www.melon.com/chart/index.htm"
driver.get(url)

# 페이지가 완전히 로딩될 때까지 기다림
time.sleep(5)

# ✅ 페이지 소스 가져오기
soup = BeautifulSoup(driver.page_source, "html.parser")

# ✅ 데이터 추출
songs = soup.select("tr.lst50, tr.lst100")  # 1~100위 리스트 선택
melon_chart = []

for song in songs:
    rank = song.select_one("span.rank").text.strip()  # 순위
    title = song.select_one("div.ellipsis.rank01 > span > a").text.strip()  # 곡명
    artist = song.select_one("div.ellipsis.rank02 > a").text.strip()  # 아티스트
    
    melon_chart.append(f"{rank}위 - {title} ({artist})")

# ✅ 출력
for item in melon_chart:
    print(item)

# ✅ 드라이버 종료
driver.quit()
