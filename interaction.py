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