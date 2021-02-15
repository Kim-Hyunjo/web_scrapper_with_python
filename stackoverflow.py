from bs4 import BeautifulSoup
import requests
import scrapper

url = "https://stackoverflow.com/jobs"
LIMIT = 100
params = {"q":"python", "I":"경기도+성남","limit":LIMIT,"start":"0"}
response = requests.get(url,params=params)
soup = BeautifulSoup(response.text,'html.parser')

scrapper.getJobs.extractJobs(url, params, LIMIT)