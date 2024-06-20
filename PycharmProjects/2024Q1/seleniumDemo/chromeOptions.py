from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

option = Options()
#option.add_argument("window-size=")  #w-945 h-1020
option.add_experimental_option("detach", True)
option.add_argument("--start-maximized")
#option.add_argument("headless")
option.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
#driver.set_window_size(800, 500)
driver.get("https://self-signed.badssl.com")
sleep(3)
print(driver.get_window_size())
driver.quit()
