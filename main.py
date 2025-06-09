import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# === Configuration ===
ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"
GOOGLE_FORM_URL = "https://forms.gle/kdNyrUGsee52UZaMA"


def setup_driver():
    options = Options()
    options.add_experimental_option("detach", True)
    return webdriver.Chrome(options=options)


def scrape_zillow():
    response = requests.get(ZILLOW_URL)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    addresses = [a.get_text(strip=True) for a in soup.find_all("address", attrs={"data-test": "property-card-addr"})]
    prices = [p.get_text(strip=True)
              .replace("$", "")
              .replace("+", "")
              .replace("/mo", "")
              .replace("1 bd", "")
              .replace("1bd", "")
              .strip()
              for p in soup.find_all("span", class_="PropertyCardWrapper__StyledPriceLine")]
    links = [l.get("href") for l in soup.select(".StyledPropertyCardDataWrapper a") if l.get("href")]

    return list(zip(addresses, prices, links))


def fill_form(driver, address, price, link):
    try:
        address_input = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
        price_input = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
        link_input = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
        submit_button = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div")

        address_input.send_keys(address)
        price_input.send_keys(price)
        link_input.send_keys(link)
        submit_button.click()

        time.sleep(1)
        next_link = driver.find_element(By.TAG_NAME, "a")
        next_link.click()

    except Exception as e:
        print(f"❌ Error on entry: {e}")


def main():
    driver = setup_driver()
    driver.get(GOOGLE_FORM_URL)

    data = scrape_zillow()

    print(f"🔍 Scraped {len(data)} properties. Submitting...")
    for address, price, link in data:
        time.sleep(2)
        fill_form(driver, address, price, link)

    print("✅ All submissions complete.")
    driver.quit()


if __name__ == "__main__":
    main()
