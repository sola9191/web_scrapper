import requests
from bs4 import BeautifulSoup

url = "https://www.jobkorea.co.kr/Search/?stext=sqa&tabType=recruit&Page_No=1"
all_jobs = []

def scrape_page(url):
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"}
    response = requests.get(url, headers=headers)
    response.encoding = response.apparent_encoding 
    soup = BeautifulSoup(response.content, "html.parser")
    jobs = soup.find("article", class_="list").find_all("div", class_="list-section-information")

    for job in jobs:
        title = job.find("a").text.strip()
        region = job.find_all("li")[3].text
        # company = 
        url = job.find("a")["href"]
        job_data ={
            "title" : title,
            "region" : region,
            "url" : f"https://www.jobkorea.co.kr/{url}"
        }
        all_jobs.append(job_data)

def get_pages(url):
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    return len(soup.find("article", class_="tplPagination pagenation").find_all("button", class_="button-pagenation"))

total_pages = get_pages(url)

for x in range(total_pages):
    url=f"https://www.jobkorea.co.kr/Search/?stext=sqa&tabType=recruit&Page_No={x+1}"
    scrape_page(url)
    
for job in all_jobs:
    print(f"title: {job['title']} / region: {job['region']} / url: {job['url']}")
