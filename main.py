from selenium import webdriver
from selenium.webdriver.common.by import By
#Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/Megalast-Liquid-Catsuit-Lipstick-Mocha/dp/B01N5G2TYO/?_encoding=UTF8&pd_rd_w=ki3Yf&content-id=amzn1.sym.255b3518-6e7f-495c-8611-30a58648072e%3Aamzn1.symc.a68f4ca3-28dc-4388-a2cf-24672c480d8f&pf_rd_p=255b3518-6e7f-495c-8611-30a58648072e&pf_rd_r=1NE7ZTF1TW178HTHH68E&pd_rd_wg=2cTpS&pd_rd_r=1b6ff91f-fa34-45e2-a0f7-59c009d8ec4f&ref_=pd_hp_d_atf_ci_mcx_mr_ca_hp_atf_d")

price_dollar = driver.find_element(By.CLASS_NAME, value= "a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value= "a-price-fraction")

print(f"The price is {price_dollar.text}.{price_cents.text}")





driver.quit()