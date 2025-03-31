from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
import csv

class Job:
    def __init__(self, job):
        self.link = self.get_link(job)
        self.title = self.get_title(job)
        self.compnay_name = self.get_company_name(job)
        self.reward = self.get_reward(job)
    
    def get_link(self, job):
        return f"https://www.wanted.co.kr{job.find('a')['href']}"
    
    def get_title(self, job):
        return job.find("strong", class_="JobCard_title__HBpZf").text
    
    def get_company_name(self, job):
        return job.find("span", class_="JobCard_companyName__N1YrF").text
    
    def get_reward(self, job):
        return job.find("span", class_="JobCard_reward__cNlG5").text
    
class FileWriter:
    def __init__(self, keyword):
        self.file = open(f"{keyword}_jobs.csv", "w")

    def write(self, datas):
        writer = csv.writer(self.file)
        writer.writerow(["Title", "Company", "Reward", "Link"])
        for data in datas:
            writer.writerow([data.title, data.compnay_name, data.reward, data.link])
        self.file.close()

class Scraper:
    def __init__(self,keyword):
        self.content = self.get_content(keyword)
        self.jobs_db = []

    def scrape(self):
        soup = BeautifulSoup(self.content, "html.parser")
        jobs = soup.find_all("div", class_="JobCard_container__REty8")
        for job in jobs:
            job = Job(job)
            self.jobs_db.append(job)
    
    def get_content(self, keyword):
        p = sync_playwright().start()
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(f"https://www.wanted.co.kr/search?query={keyword}&tab=position")
        for i in range(5):
            time.sleep(1)
            page.keyboard.down("End")
        content = page.content()
        browser.close()
        p.stop()
        return content


keywords = ["flutter", "python", "react"]

for keyword in keywords:
    scraper = Scraper(keyword)
    scraper.scrape()
    fw = FileWriter(keyword)
    fw.write(scraper.jobs_db)