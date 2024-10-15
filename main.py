from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


job_list = []
for pageNumber in range(1,3):
    url = f'https://www.upwork.com/nx/search/jobs/?ontology_skill_uid=1504884906003529729&proposals=0-4,5-9&q=%28web%20AND%20scraping%29%20AND%20NOT%20%28ChatGPT%20OR%20AI%20OR%20Application%29&page={pageNumber}&per_page=50'
    driver = webdriver.Chrome()
    driver.get(url)
    soup = BeautifulSoup(driver.page_source,"lxml")
    soup = soup.find_all("article",class_ = "job-tile cursor-pointer px-md-4 air3-card air3-card-list px-4x")
    for job in soup:
        job_dict = {
            "Job Title":job.find("h2",class_ ="h5 mb-0 mr-2 job-tile-title").text,
            "Link": "https://www.upwork.com"+job.find("a",class_= "up-n-link")["href"]
        }
        job_list.append(job_dict)

df = pd.DataFrame(job_list)
df.to_csv("jobs.csv")
        
