import urllib.request
import bs4

url = "http://www.naver.com"
html = urllib.request.urlopen(url) # 데이터를 받아옴

bs_obj = bs4.BeautifulSoup(html, "html.parser")

# print(bs_obj)     # bs_obj 를 출력해줌

top_right = bs_obj.find("div", {"class":"area_links"})
first_a = top_right.find("a")
print(first_a.text)     # 네이버를 시작페이지로
