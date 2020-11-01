import requests
from bs4 import BeautifulSoup

ssu_notice = requests.get(
    "https://scatch.ssu.ac.kr/%ea%b3%b5%ec%a7%80%ec%82%ac%ed%95%ad/?f&keyword"
)


# beautifulsoup에게 ssu_notice는 html이라고 알려줌
ssu_soup = BeautifulSoup(ssu_notice.text, "html.parser")

# 페이지 컨테이너에서 ul 추출
pagination = ssu_soup.find("ul", {"class": "pagination justify-content-center"})

# 추출된 ul에서 다시 class가 page-numbers 인 anchor 전부 추출
pages = pagination.find_all("a", {"class": "page-numbers"})


# page anchor에서 '페이지번호'만을 추출하여 리스트화
page_list = []
for page in pages:
    # 문자형인 페이지번호를 int형으로 변환
    page_list.append(int(page.string))

print(page_list)