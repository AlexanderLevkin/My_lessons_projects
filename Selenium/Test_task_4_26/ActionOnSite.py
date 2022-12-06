import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome

driver = Chrome(executable_path=ChromeDriverManager().install())
base_url = 'https://www.saucedemo.com'
driver.get(base_url)
driver.maximize_window()
password = "secret_sauce"
login = "standard_user"

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

# Select the item on the main page (after login to site)
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

# Transition to the cart
    def click_on_cart_button(self, cart_but):
        cart_button = self.driver.find_element(By.XPATH, cart_but)
        cart_button.click()
        time.sleep(1)

class DataFromCart(SelectItem):
# Find the piked item in cart
    def cart_check_name(self, cart_name):
        cart_name_v = self.driver.find_element(By.XPATH, cart_name)
        cart_name_v = cart_name_v.text
        print(cart_name_v)

    def cart_check_cost(self, cart_cost):
        cart_cost_v = self.driver.find_element(By.XPATH, cart_cost)
        cart_cost_v = cart_cost_v.text
        cart_cost_v_final = float(cart_cost_v.replace('$', " "))
        print(cart_cost_v_final )

#Click on the checkout button on the cart
    def click_on_the_checkout_button(self):
        checkout_button = self.driver.find_element(By.XPATH, '//button[@id="checkout"]')
        checkout_button.click()
        print('Click on Checkout Button')

#Fill in the user form (Common for ALL)
    def fill_in_the_information_about_customer(self):
        first_name_field = self.driver.find_element(By.XPATH, '//input[@id="first-name"]')
        first_name_field.send_keys("Alexander")
        last_name_field = self.driver.find_element(By.XPATH, '//input[@id="last-name"]')
        last_name_field.send_keys("Levkin")
        zip_code_field = self.driver.find_element(By.XPATH, '//input[@id="postal-code"]')
        zip_code_field.send_keys("777")
        continue_button = self.driver.find_element(By.XPATH, '//input[@id="continue"]')
        continue_button.click()
        time.sleep(1)
        print('Fill in the customer information')

# FIND THE ITEM SUM AND TOTAL COST ON ORDER PAGE
    def item_sum_from_cart(self, item_sum):
        item_sum_fc = self.driver.find_element(By.XPATH, item_sum)
        item_sum_fc = item_sum_fc.text
        item_sum_final = float(item_sum_fc.replace('$', " "))
        print(item_sum_final)

    def total_sum_from_cart(self, total_sum):
        total_sum_fc = self.driver.find_element(By.XPATH, total_sum)
        total_sum_fc = total_sum_fc.text
        total_sum_final = float(total_sum_fc.replace("Item total: $", " "))







