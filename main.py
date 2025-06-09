from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

appbrewery_URL = "https://appbrewery.github.io/Zillow-Clone/"


response = requests.get(url=appbrewery_URL)
response.raise_for_status()
soup =BeautifulSoup(response.text, "html.parser")
addresses = soup.find_all("address", attrs={"data-test": "property-card-addr"})
cost_per_month = soup.find_all("span", class_="PropertyCardWrapper__StyledPriceLine")
links = soup.find_all('a', attrs={"data-test": "property-card-link"})
addresses_list = []
cost_list = []
link_list = []

for link in links:
    href = link.get("href")
    if href:
        link_list.append(href)

for addr in addresses:
    addresses_list.append(addr.get_text(strip=True))

for cost in cost_per_month:
    cost_list.append(cost.get_text(strip=True).replace("$","").replace('+', '').replace('/mo','').replace('1 bd','').strip().replace('1bd',''))

print(link_list)
