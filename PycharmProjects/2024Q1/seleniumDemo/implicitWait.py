from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(5)
#driver.maximize_window()
driver.get("http://staging.shopping.beeyor.com/shop/")
driver.find_element(By.XPATH, "(//span[text()='Add to cart'])[1]").click()
driver.find_element(By.CLASS_NAME, "wc-block-mini-cart__button").click()
driver.find_element(By.XPATH, "//span[text()='View my cart']").click()
