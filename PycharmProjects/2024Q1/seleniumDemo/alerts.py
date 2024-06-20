from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
sleep(5)
driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']").click()
sleep(2)
alert = driver.switch_to.alert
sleep(2)
alert.accept()
sleep(5)
driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']").click()
sleep(2)
alert.dismiss()
sleep(2)
text_of_the_alert = driver.find_element(By.CSS_SELECTOR, "#result").text
print(text_of_the_alert)
sleep(2)
driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']").click()
sleep(2)
alert.send_keys("Tojtech Q1 2024 is almost done with courses")
sleep(2)
alert.accept()
sleep(2)
text_of_last_alert = text_of_the_alert = driver.find_element(By.CSS_SELECTOR, "#result").text
print(text_of_last_alert)


