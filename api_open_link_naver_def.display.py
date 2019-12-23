# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import urllib.request
import requests
from urllib.parse import urlparse

keyword = "광운대학교"

# client_id = "oAUslLX5Dmtc70_hlzi5"
# client_secret = "z_GRGNO4ep"
# encText = urllib.parse.quote("광운대")
# url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
def get_api_result(keyword, display):
    url = "https://openapi.naver.com/v1/search/blog?query=" + keyword + str(display)
    result = requests.get(urlparse(url).geturl(),
                          headers={"X-Naver-Client-Id":"oAUslLX5Dmtc70_hlzi5", "X-Naver-Client-Secret":"z_GRGNO4ep"})
    return result.json()

json_obj = get_api_result('광운대학교', 100)
print(json_obj)
