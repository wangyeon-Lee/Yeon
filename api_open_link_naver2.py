# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import urllib.request
import requests
from urllib.parse import urlparse

keyword = "광운대"

# client_id = "oAUslLX5Dmtc70_hlzi5"
# client_secret = "z_GRGNO4ep"
# encText = urllib.parse.quote("광운대")
# url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
url = "https://openapi.naver.com/v1/search/blog?query=" + keyword # json 결과
result = requests.get(urlparse(url).geturl(),
                      headers={"X-Naver-Client-Id":"oAUslLX5Dmtc70_hlzi5", "X-Naver-Client-Secret":"z_GRGNO4ep"})
print(result.json())  # 광운대 키워드 있는 블로그보여줌
json = {'name':'WangYeon', 'age':'23', 'where':'서울', 'phone_number':'010-5555-3333',
        'friends':[{'name':'GiHo', 'age':'23'},{'name':'yeongjae', 'age':'23'}]}
friends = json['friends']
for friends in friends:
    print(friends['name'])

# print(json['name'])
# print(json['phone_number'])
# print(json['age'])
# print(json['where'])