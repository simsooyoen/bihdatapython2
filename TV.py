import requests
from bs4 import BeautifulSoup

# 방송사별 편성표 URL
schedule_urls = {
    "KBS": "https://schedule.kbs.co.kr/?search_day=20250602",  # KBS 편성표
    "SBS": "https://www.sbs.co.kr/schedule/index.html?div=gnb_pc",  # SBS 편성표
    "MBC": "https://schedule.imbc.com/?NaPm=ct%3Dmbepdc9r%7Cci%3Dcheckout%7Ctr%3Dds%7Ctrx%3Dnull%7Chk%3Db5b747a74fd82dfd99b8b663bd274b8c6ea50939"  # MBC 편성표
}

# 방송사별 편성표에서 시간에 맞는 방송 찾기
def get_schedule(channel, time):
    # 선택한 방송사의 편성표 URL
    url = schedule_urls.get(channel)
    if not url:
        print("지원하지 않는 방송사입니다.")
        return

    # 웹 요청 및 응답 받기
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    
    # 응답 상태 확인
    if response.status_code != 200:
        print(f"{channel} 사이트 접근 실패")
        return
    
    # BeautifulSoup을 사용하여 HTML 파싱
    soup = BeautifulSoup(response.text, 'html.parser')

    programs = []

    # 방송사별로 HTML 구조가 다르기 때문에 태그와 클래스를 다르게 처리해야 함
    if channel == "KBS":
        # KBS의 경우, 프로그램 시간과 제목이 span 태그 내에 포함
        program_elements = soup.find_all('span', {'class': 'program-title'})  # 이건 예시로, 실제 HTML 구조에 맞게 수정 필요
    elif channel == "SBS":
        # SBS의 경우, 시간대별로 td 태그 내에 방송 프로그램 정보가 있음
        program_elements = soup.find_all('td', {'class': 'time-list'})  # 이건 예시로, 실제 HTML 구조에 맞게 수정 필요
    elif channel == "MBC":
        # MBC의 경우, div 또는 span 태그 내에 방송 정보가 있음
        program_elements = soup.find_all('span', {'class': 'program-name'})  # 이건 예시로, 실제 HTML 구조에 맞게 수정 필요

    # 방송 프로그램 정보 추출
    for program in program_elements:
        # 방송 시간과 제목을 가져오는 부분은 HTML 구조에 따라 달라질 수 있음
        program_time = program.find('strong')  # 방송 시간 태그 (예시)
        program_title = program.find('span', {'class': 'title'})  # 방송 제목 태그 (예시)

        if program_time and program_title:
            program_time = program_time.get_text().strip()
            program_title = program_title.get_text().strip()
            
            # 사용자가 입력한 시간과 비교
            if time in program_time:
                programs.append((program_time, program_title))
    
    return programs

# 사용자 입력 처리
def main():
    print("방송사와 시간을 입력하면 해당 시간에 방송 중인 프로그램을 알려드립니다.")
    
    # 방송사 선택 (KBS, SBS, MBC)
    channel = input("방송사 (KBS, SBS, MBC) 입력: ").strip()
    
    # 시간 입력 (예: 13:00)
    time = input("시간 (HH:MM 형식으로 입력): ").strip()
    
    # 해당 시간에 방송되는 프로그램 찾기
    programs = get_schedule(channel, time)
    
    if programs:
        print(f"{channel}에서 {time}에 방송되는 프로그램:")
        for idx, (program_time, program_title) in enumerate(programs, start=1):
            print(f"{idx}. {program_time} - {program_title}")
    else:
        print(f"{time}에 방송되는 프로그램이 없습니다.")

if __name__ == "__main__":
    main()