from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()
driver.get("http://staging.shopping.beeyor.com/shop/")
sleep(3)
driver.find_element(By.XPATH, "//span[text()='Add to cart']").click()
sleep(3)
driver.find_element(By.CLASS_NAME, "wc-block-mini-cart__button ").click()
sleep(3)
driver.find_element(By.XPATH,  "//span[contains(text(),'Go to')]").click()
sleep(3)
driver.find_element(By.CSS_SELECTOR, "#components-form-token-input-0").send_keys("Uni")
sleep(2)
list_of_countries = driver.find_elements(By.CSS_SELECTOR, ".componetns-form-token-field__suggestion")
for country in list_of_countries:
    if country.text == "United Kingdom":
        country.click()
        break
        
sleep(2)