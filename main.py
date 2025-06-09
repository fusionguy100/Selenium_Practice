from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.keys import Keys
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

appbrewery_URL = "https://appbrewery.github.io/Zillow-Clone/"
google_form_URL = "myformurl"
driver.get(url=google_form_URL)

response = requests.get(url=appbrewery_URL)
response.raise_for_status()
soup =BeautifulSoup(response.text, "html.parser")
addresses = soup.find_all("address", attrs={"data-test": "property-card-addr"})
cost_per_month = soup.find_all("span", class_="PropertyCardWrapper__StyledPriceLine")
links = soup.select(".StyledPropertyCardDataWrapper a")
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

print(f'There are {len(addresses_list)} addresses in the list.')
print(f'There are {len(cost_list)} cost in the list.')
print(f'There are {len(link_list)} links in the list.')



for i in range(0,len(addresses_list)):
    time.sleep(2)
    address_input = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    price_input = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    link_input = driver.find_element(By.XPATH,"/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    submit_button = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div")

    address_input.send_keys(addresses_list[i])
    price_input.send_keys(cost_list[i])
    link_input.send_keys(link_list[i])
    submit_button.click()
    next_link = driver.find_element(By.TAG_NAME, "a")
    next_link.click()



driver.quit()