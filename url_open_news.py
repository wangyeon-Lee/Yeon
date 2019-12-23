import urllib.request
import bs4

url = "https://news.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")

newslist = bs_obj.find("ul", {"class":"mlist2 no_bg"})
lis = newslist.findAll("li")

for li in lis:
    strong = li.find("strong")
    print(strong.text)
