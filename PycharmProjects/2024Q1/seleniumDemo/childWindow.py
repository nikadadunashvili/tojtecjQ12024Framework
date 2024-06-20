from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")
sleep(2)
driver.find_element(By.XPATH, "//a[text()='Click Here']").click()
sleep(2)

window = driver.window_handles
driver.switch_to.window(window[1])
sleep(2)
text_of_element = driver.find_element(By.XPATH, "//h3[text()='New Window']").text
print(text_of_element)
driver.quit()
sleep(2)
driver.switch_to.window(window[0])
sleep(2)
text_parent_window_element = driver.find_element(By.TAG_NAME, "h3").text
print(text_parent_window_element)
