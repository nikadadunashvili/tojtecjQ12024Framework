from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("http://staging.shopping.beeyor.com/my-account/")
sleep(2)

driver.find_element(By.CLASS_NAME, "wc-block-button__link").click()
sleep(6)