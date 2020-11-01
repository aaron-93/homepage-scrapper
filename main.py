from indeed import extract_indeed_pages, extract_indeed_notices

# 목표 URL에서 가장 마지막 페이지 찾기
last_indeed_page = extract_indeed_pages()


# 목표 페이지에서 notice 추출하기
indeed_notices = extract_indeed_notices(last_indeed_page)


print(indeed_notices)