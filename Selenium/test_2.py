from selenium import webdriver
import time
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
button_login = driver.find_element(By.XPATH, '//input[@id="login-button"]')
button_login.click()
print("Click login button")

warring_text = driver.find_element(By.XPATH, '//h3[@data-test="error"]')
value_warring_text = warring_text.text
assert value_warring_text == "Epic sadface: Username and password do not match any user in this service"
print("Good test!!!")

