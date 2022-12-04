import time

from selenium.webdriver.common.by import By

from EnterSite import SelectItem

class DataFromCart(SelectItem):

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
#Common for ALL
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
# TOTAL COST
    def item_sum_from_cart(self, item_sum):
        item_sum_fc = self.driver.find_element(By.XPATH, item_sum)
        item_sum_fc = item_sum_fc.text
        item_sum_final = float(item_sum_fc.replace('$', " "))
        print(item_sum_final)

    def total_sum_from_cart(self, total_sum):
        total_sum_fc = self.driver.find_element(By.XPATH, total_sum)
        total_sum_fc = total_sum_fc.text
        total_sum_final = float(total_sum_fc.replace("Item total: $", " "))


