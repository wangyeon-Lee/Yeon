from urllib.request import urlopen
import json

from_date = "2019-01-01"
to_date = "2019-12-23"
url = "http://www.krei.re.kr:18181/chart/main_chart/index/kind/W/sdate/1972-01-01/edate/2019-12-23" \
    + from_date + "/edate/" + to_date
text = urlopen(url)
json_objs = json.load(text)

#print(json_objs)
#print(text.read())
for url in json_objs:
    print("url :", url['date'] +"  @  "+ "settlement :", url['settlement']) # url에있는 데이터에서 date , settlement 키값의 데이터를 불러옴
    #print(url['id'] +"@"+ url['date']) # url에있는 데이터에서 date , settlement 키값의 데이터를 불러옴
