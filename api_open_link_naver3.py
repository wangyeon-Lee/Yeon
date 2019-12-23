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
url = "https://openapi.naver.com/v1/search/blog?query=" + keyword + '&display=100' # json 결과 [display 보여주는 개수 100개]
result = requests.get(urlparse(url).geturl(),
                      headers={"X-Naver-Client-Id":"oAUslLX5Dmtc70_hlzi5", "X-Naver-Client-Secret":"z_GRGNO4ep"})


#####json_obj = result.json()# 타이틀만 보여줌
#####for item in json_obj['items']:
#####    print('Title : ' + item['title'])


#####json_obj = result.json()# 타이틀, 링크만 보여줌
#####for item in json_obj['items']:
#####    print('Title : ' + item['title'].replace("<b>","").replace("</b>",""), 'Link : ' + item['link'])# b태그가있으면 공백으로 수정해라

json_obj = result.json()
#print('display : ' + str(json_obj['display']))
#print('start : ' + str(json_obj['start']))
#print('items : ' + str(len(json_obj['items'])))
print(json_obj)
#print(json_obj['lastBuildDate'])
#print(json_obj['total'])
#print(json_obj['title'])
#print(json_obj['link'])
#print(json_obj['start'])
#print(json_obj['display'])
#for item in json_obj['items']:
#print(item)