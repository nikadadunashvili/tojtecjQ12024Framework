from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

option = Options()
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
driver.maximize_window()
driver.get("http://staging.shopping.beeyor.com/shop/")
sleep(4)
#driver.execute_script("window.scrollTo(0, 2000)")
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
sleep(3)
driver.execute_script()