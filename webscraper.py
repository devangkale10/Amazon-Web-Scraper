import datetime
import smtplib
import time

import requests
from bs4 import BeautifulSoup

# Connect to the website
URL = "https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_1?keywords=funny+got+data+mis+data+systems+business+analyst+t-shirt&qid=1680320819&sr=8-1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}

page = requests.get(URL, headers=headers)

Soup1 = BeautifulSoup(page.content, "lxml")

Soup2 = BeautifulSoup(Soup1.prettify(), "lxml")

title = Soup2.find(id="productTitle").get_text()
print(title)
