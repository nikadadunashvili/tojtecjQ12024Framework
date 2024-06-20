from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("http://staging.shopping.beeyor.com/")
sleep(2)
driver.find_element(By.XPATH, "//span[text()='Login']").click()
sleep(2)
driver.find_element(By.ID, "username").send_keys("regular")
sleep(2)
driver.find_element(By.ID, "password").send_keys("Default1!")
sleep(2)
driver.find_element(By.NAME, "rememberme").click()
sleep(2)
driver.find_element(By.CLASS_NAME, "woocommerce-button").click()
sleep(2)
actual_user = driver.find_element(By.XPATH, "(//strong[text()='Regular User'])[1]")
expected_user = "Darina"
print(actual_user.text)
print(expected_user)
assert expected_user == actual_user, "The users don't match. Expected user is Darina, but returned Regular User"


