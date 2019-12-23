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

# for box in boxes:
#     # print(box)
#     ptag = box.find("p", {"class":"name"})
#     span = ptag.find("span")
#     print(span.text)


def get_product_info(box):
    ptag = box.find("p", {"class":"name"})
    spans_name = ptag.findAll("span")
    ul = box.find("ul")
    spans_price = ul.findAll("span")

    name = spans_name[0].text
    price = spans_price[1].text
    print(" Price : ", price)

    atag = box.find("a")
    link = atag['href']
    print("  Link : ", link)
    return {"name":name, "price":price, "link":link}

for box in boxes:
    ptag = box.find("p", {"class": "name"})
    span = ptag.find("span")
    print("  Name : ", span.text)
    product_info = get_product_info(box)
    print(product_info)
    print()


