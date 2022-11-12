from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path='/Users/alexanderlevkin/Desktop/My_projects/'
                                           'My_lessons_projects/Selenium/geckodriver')
driver.get('https://www.saucedemo.com')
driver.maximize_window()
# user_name = driver.find_element(By.ID, "user-name") #By ID
# user_name = driver.find_element(By.NAME, "user-name")  # By Name
# user_name = driver.find_element(By.XPATH, '//*[@id="user-name"]')  # Full Xpath
user_name = driver.find_element(By.XPATH, '//input[@data-test="username"]')  # DATA-Test XPATH
user_name.send_keys("standard_user")
password = driver.find_element(By.CSS_SELECTOR, "#password")  # CSS Selector
password.send_keys("secret_sauce")
button_login = driver.find_element(By.XPATH, '//input[@value="Login"]')
button_login.click()
# time.sleep(10)
# driver.close()

# driver = webdriver.Safari()
# driver.get('https://www.browserstack.com/automate')
