from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(5)
driver.get("http://staging.shopping.beeyor.com/shop/")
sleep(2)
driver.find_element(By.CSS_SELECTOR, "#wp-block-search__input-3").send_keys("Beanie")
sleep(2)
driver.find_element(By.CSS_SELECTOR, "button[aria-label='Search']").click()
sleep(2)
element = driver.find_element(By.XPATH, "(//a[text()='Add to cart'])[1]")
sleep(2)
action = ActionChains(driver)
sleep(2)
#action.move_to_element(element).click().perform()
action.move_to_element(element).context_click().perform()
sleep(5)