from selenium import webdriver
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path='/Users/alexanderlevkin/Desktop/My_projects/'
                                           'My_lessons_projects/Selenium/geckodriver')
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
password.send_keys(Keys.RETURN)


filter = driver.find_element(By.XPATH, '//select[@class="product_sort_container"]')
time.sleep(0.5)
filter.send_keys(Keys.PAGE_DOWN)
