import time
from selenium.webdriver.common.by import By

class Login:
    def __init__(self,driver):
        self.driver = driver

    def enter_to_the_site(self,login_name,password_name):
        username_field = self.driver.find_element(By.XPATH, '//input[@id="user-name"]')
        username_field.send_keys(login_name)
        password_field = self.driver.find_element(By.XPATH, '//input[@id="password"]')
        password_field.send_keys(password_name)
        time.sleep(1)
        login_button = self.driver.find_element(By.XPATH, '//input[@id="login-button"]')
        login_button.click()
        time.sleep(1)
        print("Login into site\n")

class SelectItem(Login):

    def __init__(self,driver):
        super().__init__(driver)

    def selecting_item(self, pick_item):
        item = self.driver.find_element(By.XPATH, pick_item)
        item.click()
        time.sleep(1)

    def selecting_name_item(self, name_item):
        item_name_onsite = self.driver.find_element(By.XPATH, name_item)
        item_name_onsite = item_name_onsite.text
        print(item_name_onsite)

    def selecting_cost_item(self, cost_item):
        item_cost_onsite = self.driver.find_element(By.XPATH, cost_item)
        item_cost_onsite = item_cost_onsite.text
        item_cost_onsite_final = float(item_cost_onsite.replace('$', " "))
        print(item_cost_onsite_final)
        time.sleep(1)

    def click_on_cart_button(self):
#Transition to the cart
        cart_button = self.driver.find_element(By.XPATH, '//span[@class="shopping_cart_badge"]')
        cart_button.click()
        time.sleep(1)






