import json
import requests
from bs4 import BeautifulSoup


num, limit =1000, 100
titles, links = [], []

URL = "https://www.dcard.tw/f/funny?latest=true"
response = requests.get(URL)
html = BeautifulSoup(response.text,"html.parser")

a = html.find("h2").find("a")
last = int(a["href"].split('/')[-1]) + 1

for _ in range(0, int(num/limit)):
    post_data={
        "before": str(last),
        "limit": str(limit),
        "popular": "false"
    }
    response = requests.get("https://www.dcard.tw/service/api/v2/forums/funny/posts",
                     params=post_data, headers={"Referer": "https://www.dcard.tw/", "User-Agent": "Mozilla/5.0"})
    data = json.loads(response.text)

    for i in range(len(data)):
        title = str(data[i]["title"])
        print('標題: ', title)
        titles.append(title)
        link = "https://www.dcard.tw/f/funny/p/" + str(data[i]["id"])
        print('網址: ', link)
        links.append(link)
        last = data[i]["id"]
print('--------------------------------------------------------------------')
print('第 1 篇標題: {}\n第 1 篇網址: {}\n第 1000 篇標題: {}\n第 1000 篇網址: {}\n'
      .format(titles[0], links[0], titles[1000 - 1], links[1000 - 1]))