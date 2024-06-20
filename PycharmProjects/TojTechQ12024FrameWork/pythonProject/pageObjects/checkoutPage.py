from selenium.webdriver.common.by import By


class CheckoutPage:
    def init(self, driver):
        self.driver = driver

    country_field= (By.CSS_SELECTOR, "#components-form-token-input-0")
    list_of_countries = (By.CSS_SELECTOR,".components-form-token-field__suggestion")

    def get_country_field(self):
        return self.driver.find_element(*CheckoutPage.country_field)

    def get_list_of_countries(self):
        return self.driver.find_elements(*CheckoutPage.list_of_countries)