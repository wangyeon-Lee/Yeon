import requests
from bs4 import BeautifulSoup

url = "https://bp.eosgo.io/"

result = requests.get(url =url)
bs_obj = BeautifulSoup(result.content, "html.parser")
#print(bs_obj)  # html 가져오기



# profile_name = bs_obj.find("div", {"class":"profile-name"})
#
# h1_bp_name = profile_name.find("h1")
# bp_name = h1_bp_name.text
# print(bp_name)
#
# # cover_buttons = bs_obj.find("div", {"class":"cover-buttons"})
# # li_bp_name = cover_buttons.find("li")
# # bp_name = li_bp_name.text
# # print(bp_name) # Calgary text
#
# cover_buttons = bs_obj.find("div", {"class":"cover-buttons"})
# button_label = bs_obj.find("span", {"class":"button-label"})
# location = button_label.text
# print(location) # Calgary text

# cover_buttons = bs_obj.find("div", {"class":"cover-buttons"})
# a_bp_name = cover_buttons.find("a")
# bp_name = a_bp_name.text
# print(bp_name)# Website text

# cover_buttons = bs_obj.find("div", {"class":"cover-buttons"})
# button_label = bs_obj.find("span", {"class":"button-label"})
# location = button_label.text
# lis = cover_buttons.findAll("li")
# li_tag = lis[1]
#
# a_tag = li_tag.find("a")
# link = a_tag['href']
# print(link)# 주소


def get_bp_info(url):  # 딕셔너리에 저장
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")

    profile_name = bs_obj.find("div", {"class":"profile-name"})
    h1_bp_name = profile_name.find("h1")

    bp_name = h1_bp_name.text

    cover_buttons = bs_obj.find("div", {"class": "buttons medium button-plain"})
    button_label = cover_buttons.find("span")
    location = button_label.text

    cover_buttons = bs_obj.find("div", {"class": "buttons medium button-outlined"})
    lis = cover_buttons.find("span")
    a_tag = lis.find("a")
    link = a_tag['href']

    dictionary1 = {}
    dictionary1['name'] = bp_name
    dictionary1['location'] = location
    dictionary1['link'] = link

    return dictionary1

# dic_result = get_bp_info(url)
#
# print(dic_result)

lf_items = bs_obj.findAll("div", {"class":"lf-item"}) # 링크작업

hrefs = [div.find("a")['href'] for div in lf_items] # 링크작업

for number in range(0, 5):
    dic_result = get_bp_info(hrefs[number])  # 리스트로 보냄
    print(dic_result)




