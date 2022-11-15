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

time.sleep(5)
user_name.clear()
time.sleep(2)
# text_products = driver.find_element(By.XPATH, '//span[@class="title"]')
# value_text_products = text_products.text
# print(value_text_products)
# assert value_text_products == "PRODUCTS"
# print("Good!")
#
# url = "https://www.saucedemo.com/inventory.html"
# get_url = driver.current_url
# print(get_url)
# assert url == get_url
# print("GOOD URL")
# time.sleep(10)