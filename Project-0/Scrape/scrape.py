import requests
from bs4 import BeautifulSoup
import pprint
res = requests.get("https://news.ycombinator.com")
soup =BeautifulSoup(res.text,"html.parser")

link = soup.select(".titlelink")
subtext = soup.select(".subtext")

def sorted_hn(x):
    return sorted(x, key=lambda k: k["vote"],reverse = True)



def hn_creator(link,subtext):
    hn = []
    for idx, item in enumerate(link):
        result = link[idx].getText()
        href = link[idx].get("href", None)
        vote =subtext[idx].select(".score")

        if len(vote):
            point = int(vote[0].getText().replace("points",""))
            if point > 100:
                hn.append({'title': result, "links": href,"vote": point})
    return sorted_hn(hn)
    return sorted(hn, key=lambda k: k["vote"])




pprint.pprint(hn_creator(link, subtext))
# print(soup.find("div"))