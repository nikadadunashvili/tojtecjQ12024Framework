from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#driver.maximize_window()
# driver.get("https://the-internet.herokuapp.com/dynamic_loading")
# sleep(2)
# driver.find_element(By.CSS_SELECTOR, "a[href='/dynamic_loading/1']").click()
# sleep(2)
# driver.find_element(By.XPATH, "//button[text()='Start']").click()
# wait = WebDriverWait(driver, 10)
# wait.until(expected_conditions.text_to_be_present_in_element((By.ID, "finish"), "Hello World!"))
# text_of_new_element = driver.find_element(By.ID, "finish").text
# print(text_of_new_element)

driver.find_element(By.CSS_SELECTOR, "a[href='/dynamic_loading/2']").click()
sleep(2)
driver.find_element(By.XPATH, "//button[text()='Start']").click()
wait = WebDriverWait(driver, 10)
text_of_element_located = wait.until(expected_conditions.presence_of_element_located((By.ID, "finish")))
print(text_of_element_located)
