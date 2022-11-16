import datetime
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='//Users/alexanderlevkin/Desktop/My_projects/'
                                          'My_lessons_projects/Selenium/chromedriver')
base_url = 'https://www.saucedemo.com'
driver.get(base_url)
driver.maximize_window()

password = "secret_sauce"
login = "standard_user"
# Authorization on site
username_field = driver.find_element(By.XPATH, '//input[@id="user-name"]')
username_field.send_keys(login)

password_field = driver.find_element(By.XPATH, '//input[@id="password"]')
password_field.send_keys(password)

login_button = driver.find_element(By.XPATH, '//input[@id="login-button"]')
login_button.click()
time.sleep(1)
print("Login into site")
# Selecting 2 goods
driver.execute_script("window.scrollTo(0, 500)")
time.sleep(2)

red_kids_tshirt = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-onesie"]')
red_kids_tshirt.click()
time.sleep(1)
red_adult_tshirt = driver.find_element(By.XPATH, '//button[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]')
red_adult_tshirt.click()
time.sleep(1)
print("Select 2 goods")
# Creating name and worth in variables
# kids t-shirt
red_kids_tshirt_name = driver.find_element(By.XPATH, '//*[@id="item_2_title_link"]/div')
red_kids_tshirt_name = red_kids_tshirt_name.text
print("Name of first good is: " + red_kids_tshirt_name)
red_kids_tshirt_cost = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[5]/div[2]/div[2]/div')
red_kids_tshirt_cost = red_kids_tshirt_cost.text
print("It costs: " + red_kids_tshirt_cost)
# adult t-shirt
red_adult_tshirt_name = driver.find_element(By.XPATH, '//*[@id="item_3_title_link"]/div')
red_adult_tshirt_name = red_adult_tshirt_name.text
print("Name of second good is: " + red_adult_tshirt_name)
red_adult_tshirt_cost = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[6]/div[2]/div[2]/div')
red_adult_tshirt_cost = red_adult_tshirt_cost.text
print("It costs: " + red_adult_tshirt_cost)
time.sleep(1)


