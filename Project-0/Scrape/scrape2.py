import requests
from bs4 import BeautifulSoup
import pprint


page1= input("Enter the page number  1 :  ")
page2 = input("Enter the page number  2 :  ")

res = requests.get("https://news.ycombinator.com/news?p ={page1}")
res2 = requests.get("https://news.ycombinator.com/news?p={page2}")


soup =BeautifulSoup(res.text,"html.parser")
soup2 = BeautifulSoup(res2.text,"html.parser")


link = soup.select(".titlelink")
link2 = soup.select(".titlelink")

subtext = soup.select(".subtext")
subtext2 = soup.select(".subtext")

mega_link = link + link2
mega_subtext =subtext + subtext2


def sorted_hn(x):
    return sorted(x, key=lambda k: k["vote"])

def hn_creator(link,subtext):
    hn = []
    for idx, item in enumerate(link):
        result = link[idx].getText()
        href = link[idx].get("href", None)
        vote =subtext[idx].select(".score")
        if len(vote):
            point = int(vote[0].getText().replace("points",""))
            if point > 99:
                hn.append({'title': result, "links": href,"vote": point})
    return sorted_hn(hn)


pprint.pprint(hn_creator(mega_link, mega_subtext))
#print(soup.find("div"))
# # return sorted(hn, key=lambda k: k["vote"])