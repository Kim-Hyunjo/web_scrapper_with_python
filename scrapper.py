from bs4 import BeautifulSoup
import requests

url = "https://kr.indeed.com/jobs"
LIMIT = 100
params = {"q":"python", "I":"경기도+성남","limit":LIMIT,"start":"0"}
response = requests.get(url,params=params)
soup = BeautifulSoup(response.text,'html.parser')
pagination = soup.find("div",{"class":"pagination"})
pages = pagination.select("a > span")
pageLS = [int(page.string) for page in pages[:-1]]
contents = []
for page in pageLS:
    params["start"] = (page-1) * LIMIT
    res = requests.get(url,params=params)
    soup = BeautifulSoup(response.text,'html.parser')
    content = soup.find_all("div", {"class":"jobsearch-SerpJobCard"})
    titles = []
    for c in content:
        title = c.find("h2",{"class":"title"}).find("a")["title"]
        titles.append(title)
print(titles)
    #contents.append(content)
    