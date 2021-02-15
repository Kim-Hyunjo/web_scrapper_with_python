from bs4 import BeautifulSoup
import requests

class Job:
    def __init__(self, title=None, company=None, location=None, link=None):
        self.title = title
        self.company = company
        self.location = location
        self.link = link

    def __str__(self):
        return "["+self.company+"]"+self.title+" in "+self.location

class GetJobs:
    def getPageList(self, url, params):
        response = requests.get(url,params=params)
        soup = BeautifulSoup(response.text,'html.parser')
        pages = pages = soup.find("ul",{"class":"pagination-list"}).find_all("li")
        pageLS = [int(page.string) for page in pages[:-1]]
        return pageLS

    def extractJobs(self, url, params, LIMIT):
        pageLS = getPageList()
        jobs = []
        for page in pageLS:
            if "start" in params.key():
                params["start"] = (page-1) * LIMIT
                response = requests.get(url,params=params)
            elif "pg" in params.key():
                params["pg"] = page
                soup = BeautifulSoup(response.text,'html.parser')
                contents = soup.find_all("div", {"class":"jobsearch-SerpJobCard"})
                for c in contents:
                    job = Job()
                    title = c.find("h2",{"class":"title"}).find("a")
                    job.title = title["title"]
                    job.link = "kr.indeed.com"+title["href"]
                    company = c.find("span",{"class":"company"})
                    if company.string is not None:
                        job.company = company.string.lstrip('\n')
                    else:
                        job.company = company.find("a").string.lstrip('\n')
                    location = c.find("span",{"class":"location"})
                    job.location = location.string
                    jobs.append(job)

        return jobs

        
