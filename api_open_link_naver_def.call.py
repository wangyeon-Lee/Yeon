# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색

import requests
from urllib.parse import urlparse

# client_id = "oAUslLX5Dmtc70_hlzi5"
# client_secret = "z_GRGNO4ep"
# encText = urllib.parse.quote("광운대")
# url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과


def get_api_result(keyword, display, start):
    url = "https://openapi.naver.com/v1/search/blog?query=" + keyword + "&display=" + str(display) + '&start=' + str(start)
    result = requests.get(urlparse(url).geturl(),
                          headers={"X-Naver-Client-Id":"oAUslLX5Dmtc70_hlzi5", "X-Naver-Client-Secret":"z_GRGNO4ep"})
    return result.json()


def call_and_print(keyword, page):
    json_obj = get_api_result(keyword, 100, page)
    for item in json_obj['items']:
        title = item['title'].replace("<b>", "").replace("</b>", "")
        print(title + "@" + item['bloggername'] + "@" + item['link'])

keyword = "광운대학교"
call_and_print(keyword, 1)
call_and_print(keyword, 101)
call_and_print(keyword, 201)
call_and_print(keyword, 301)
call_and_print(keyword, 401)




