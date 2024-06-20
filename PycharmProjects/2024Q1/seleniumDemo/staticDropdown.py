from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

option = Options()
option.add_experimental_option("detach", True)
# service_obj = Service("/opt/homebrew/bin/chromedriver")
# driver = webdriver.Chrome(service=service_obj, options=option)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# driver.maximize_window()
driver.get("http://staging.shopping.beeyor.com/shop/")
sleep(3)
select = Select(driver.find_element(By.CSS_SELECTOR, ".orderby"))
# select.select_by_index(2)
# select.select_by_value("price-desc")
sleep(2)
# select.select_by_visible_text("Sort by latest")
for element in select.options:
    if element.get_attribute("value") == "popularity":
        element.click()
        break

sleep(2)

