import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome
from Selenium.Test_task_4_26.Selectors import *


class Item:
    def __init__(self, login_name, password_name, pick_item, name_item):
        self.login_name = login_name
        self.password_name = password_name
        self.pick_item = pick_item
        self.name_item = name_item

    def enter_to_the_site(self):
        driver = Chrome(executable_path=ChromeDriverManager().install())
        base_url = 'https://www.saucedemo.com'
        driver.get(base_url)
        driver.maximize_window()
        username_field = driver.find_element(By.XPATH, '//input[@id="user-name"]')
        username_field.send_keys(self.login_name)
        password_field = driver.find_element(By.XPATH, '//input[@id="password"]')
        password_field.send_keys(self.password_name)
        time.sleep(1)
        login_button = driver.find_element(By.XPATH, '//input[@id="login-button"]')
        login_button.click()
        time.sleep(1)
        print("Login into site\n")

# Select the item on the main page (after login to site)
        item = driver.find_element(By.XPATH, self.pick_item)
        item.click()
        time.sleep(1)

        item_name_onsite = driver.find_element(By.XPATH, self.name_item)
        item_name_onsite = item_name_onsite.text
        print(item_name_onsite)


        item_cost_onsite = driver.find_element(By.XPATH, item_cost_comm)
        item_cost_onsite = item_cost_onsite.text
        item_cost_onsite_final = float(item_cost_onsite.replace('$', " "))
        print(item_cost_onsite_final)
        time.sleep(1)

# Transition to the cart
        cart_button = driver.find_element(By.XPATH, cart_button_comm)
        cart_button.click()
        time.sleep(1)

# Find the piked item in cart

        cart_name_v = driver.find_element(By.XPATH, cart_name_comm)
        cart_name_v = cart_name_v.text
        print(cart_name_v)
        assert item_name_onsite == cart_name_v
        print("Name of item match with cart")
        time.sleep(1)


        cart_cost_v = driver.find_element(By.XPATH, cart_cost_comm)
        cart_cost_v = cart_cost_v.text
        cart_cost_v_final = float(cart_cost_v.replace('$', " "))
        print(cart_cost_v_final )

#Click on the checkout button on the cart

        checkout_button = driver.find_element(By.XPATH, '//button[@id="checkout"]')
        checkout_button.click()
        print('Click on Checkout Button')

#Fill in the user form (Common for ALL)

        first_name_field = driver.find_element(By.XPATH, '//input[@id="first-name"]')
        first_name_field.send_keys("Alexander")
        last_name_field = driver.find_element(By.XPATH, '//input[@id="last-name"]')
        last_name_field.send_keys("Levkin")
        zip_code_field = driver.find_element(By.XPATH, '//input[@id="postal-code"]')
        zip_code_field.send_keys("777")
        continue_button = driver.find_element(By.XPATH, '//input[@id="continue"]')
        continue_button.click()
        time.sleep(1)
        print('Fill in the customer information')

# FIND THE ITEM SUM AND TOTAL COST ON ORDER PAGE

        item_sum_fc = driver.find_element(By.XPATH, item_sum_comm)
        item_sum_fc = item_sum_fc.text
        item_sum_final = float(item_sum_fc.replace('$', " "))
        print(item_sum_final)

        total_sum_fc = driver.find_element(By.XPATH, total_sum_comm)
        total_sum_fc = total_sum_fc.text
        total_sum_final = float(total_sum_fc.replace("Item total: $", " "))
        assert item_sum_final == total_sum_final
        print('The sum from cart corresponds total sum !!!')






