from bs4 import BeautifulSoup
import requests
import time
import datetime
import smtplib

#asks user for amazon listing
URL = input("Enter URL of Amazon Listing")

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
page = requests.get(URL, headers=headers)
soup1 = BeautifulSoup(page.content, "html.parser")
soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

#finds the title and price from website
title = soup2.find(id='productTitle').get_text()
price = soup2.find(id='priceblock_ourprice').get_text()

#makes pricing neater
price = "$" + price.strip()[1:]
title = title.strip()

print(title)
print(price)

