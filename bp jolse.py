import requests
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0'}
url = "http://jolse.com/category/toners-mists/1019/?page=1"

#result = requests.get(url =url) # 크롤링 거부반응일어남
result = requests.get(url, headers=headers) # 허가받지않고 사이트 접속가능

bs_obj = BeautifulSoup(result.text)
# print(bs_obj)

ul = bs_obj.find("ul", {"class":"prdList grid4"})

boxes = ul.findAll("div", {"class":"box"})

for box in boxes:
    # print(box)
    ptag = box.find("p", {"class":"name"})
    span = ptag.find("span")
    print(span.text)
