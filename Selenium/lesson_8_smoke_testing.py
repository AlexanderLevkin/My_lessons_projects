import datetime
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='//Users/alexanderlevkin/Desktop/My_projects/'
                                          'My_lessons_projects/Selenium/chromedriver')
base_url = 'https://www.saucedemo.com'
driver.get(base_url)
driver.maximize_window()

login_standart_user = 'standard_user'
password_all = 'secret_sauce'

user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
user_name.send_keys(login_standart_user)
print("Input Login")
password = driver.find_element(By.XPATH, '//input[@id="password"]')
password.send_keys(password_all)
print("Input Password")
button_login = driver.find_element(By.XPATH, '//input[@id="login-button"]')
button_login.click()
print("Click login button")

"""INFO PRODUCT 1"""
product_1 = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]')
value_product_1 = product_1.text
print(value_product_1)

price_product_1 = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div')
value_price_product_1 = price_product_1.text
print(value_price_product_1)

select_product_1 = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')
select_product_1.click()
print("Add to cart")
time.sleep(1)

select_the_cart = driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
select_the_cart.click()
print("Click on cart")
time.sleep(2)

"""INFO CART PRODUCT 1"""
cart_product_1 = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]')
cart_value_product_1 = cart_product_1.text
print(cart_value_product_1)
assert value_product_1 == cart_value_product_1
print("INFO CART PRODUCT 1 GOOD")

cart_price_product_1 = driver.find_element(By.XPATH, '//*[@id="cart_contents_container"]/'
                                                     'div/div[1]/div[3]/div[2]/div[2]/div')
cart_value_price_product_1 = cart_price_product_1.text
print(cart_value_price_product_1)
assert value_price_product_1 == cart_value_price_product_1
print("INFO CART PRODUCT 1 GOOD")

checkout = driver.find_element(By.XPATH, '//button[@id="checkout"]')
checkout.click()
time.sleep(2)

"""SELECT USER INFO"""

first_name_field = driver.find_element(By.XPATH, '//input[@id="first-name"]')
first_name_field.send_keys("Alex")
print("Input First Name")

last_name_field = driver.find_element(By.XPATH, '//input[@id="last-name"]')
last_name_field.send_keys("Levkin")
print("Input Last Name")

zip_code_field = driver.find_element(By.XPATH, '//input[@id="postal-code"]')
zip_code_field.send_keys("211400")
print("Input ZIP/POSTAL code")
time.sleep(1)

continue_button = driver.find_element(By.XPATH, '//input[@id="continue"]')
continue_button.click()
print("Click on continue button")
time.sleep(1)

"""FINISH"""
finish_product_1 = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]')
finish_value_product_1 = finish_product_1.text
print(finish_value_product_1)
assert value_product_1 == finish_value_product_1
print("INFO FINISH PRODUCT 1 GOOD")

finish_price_product_1 = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/'
                                                       'div/div[1]/div[3]/div[2]/div[2]/div')
finish_value_price_product_1 = finish_price_product_1.text
print(finish_value_price_product_1)
assert value_price_product_1 == finish_value_price_product_1
print("INFO FINISH PRODUCT 1 GOOD")

summary_price = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[5]')
summary_price = summary_price.text
print(summary_price)
item_total = "Item total: " + finish_value_price_product_1
assert summary_price == item_total
print("Total summary price good")
