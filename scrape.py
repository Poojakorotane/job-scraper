import requests
from bs4 import BeautifulSoup
import math
import pandas as pd

job_ids = []
job_details = {}
job_list = []
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
job_search_url = 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=Graduate%20%28Programming%20Language%29&location=Las%20Vegas%2C%20Nevada%2C%20United%20States&geoId=100293800&currentJobId=3415227738&start={}'

for page_index in range(0, math.ceil(117 / 25)):
    response = requests.get(job_search_url.format(page_index))
    soup = BeautifulSoup(response.text, 'html.parser')
    jobs_on_page = soup.find_all("li")
    print(len(jobs_on_page))
    for job_index in range(0, len(jobs_on_page)):
        job_id = jobs_on_page[job_index].find(
            "div", {"class": "base-card"}).get('data-entity-urn').split(":")[3]
        job_ids.append(job_id)

job_details_url = 'https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{}'
for job_id in job_ids:
    response = requests.get(job_details_url.format(job_id))
    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        job_details["company"] = soup.find(
            "div", {"class": "top-card-layout__card"}).find("a").find("img").get('alt')
    except:
        job_details["company"] = None

    try:
        job_details["job_title"] = soup.find(
            "div", {"class": "top-card-layout__entity-info"}).find("a").text.strip()
    except:
        job_details["job_title"] = None

    try:
        job_details["seniority_level"] = soup.find("ul", {"class": "description__job-criteria-list"}).find(
            "li").text.replace("Seniority level", "").strip()
    except:
        job_details["seniority_level"] = None

    job_list.append(job_details)
    job_details = {}

job_dataframe = pd.DataFrame(job_list)
job_dataframe.to_csv('linkedinjobs.csv', index=False, encoding='utf-8')
print(job_list)
