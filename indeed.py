import requests
from bs4 import BeautifulSoup

URL = "https://scatch.ssu.ac.kr/%ea%b3%b5%ec%a7%80%ec%82%ac%ed%95%ad/?f&keyword"

# 목표 URL에서 가장 마지막 페이지 찾기 함수
def extract_indeed_pages():

    # 가져올 URL 설정
    ssu_notice = requests.get(URL)

    # beautifulsoup에게 ssu_notice는 html이라고 알려줌
    soup = BeautifulSoup(ssu_notice.text, "html.parser")

    # 페이지 컨테이너에서 가장 마지막 페이지의 href 추출
    end_page = soup.find("a", {"class": "page-link next-btn-last"}).attrs["href"]

    # 가장 마지막 페이지번호 추출
    last_page_number = int(end_page.split("/")[-2])

    return last_page_number


# 목표 페이지에서 tag와 notice 제목, 날짜 추출하는 함수
def extract_notice(html):
    tag = html.find(
        "span", {"class": "label d-inline-blcok border pl-3 pr-3 mr-2"}
    ).string
    title = html.find("span", {"class": "d-inline-blcok m-pt-5"}).string
    date = html.find("div", {"class": "h2 text-info font-weight-bold"})
    if date is not None:
        date = date.string
    else:
        # date의 경우 비어있는 칸은 ~d-xl-none으로 class가 설정되어 있어서 if문으로 구분
        date = html.find(
            "div", {"class": "h2 text-info font-weight-bold d-xl-none"}
        ).string
    link = html.find("a", {"class": "text-decoration-none d-block text-truncate"})[
        "href"
    ]

    return {"date": date, "tag": tag, "title": title, "link": link}


# 목표 페이지에서 tag, notice, 날짜를 추출한 후 Dictionary 형식으로 출력하는 함수
def extract_indeed_notices(last_page):
    notices = []
    # for page in range(5):
    target_page = requests.get(
        "https://scatch.ssu.ac.kr/%ea%b3%b5%ec%a7%80%ec%82%ac%ed%95%ad/page/1/"
    )
    soup = BeautifulSoup(target_page.text, "html.parser")

    # div class notice_col3 로 할 경우 None이 발생하여서 div로 변경
    # Notice 컨테이너 불러오기
    results = soup.find_all("div", {"class": "row no-gutters align-items-center"})
    # Notice tag, title 가져오기
    for result in results:
        notice = extract_notice(result)
        notices.append(notice)
    return notices
