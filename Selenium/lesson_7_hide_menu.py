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

menu = driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]')
menu.click()
print("click menu button")
time.sleep(4)
link_about = driver.find_element(By.XPATH, '//a[@id="about_sidebar_link"]')
link_about.click()
print('click link button')
time.sleep(4)
