from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import datetime

driver = webdriver.Chrome(executable_path='//Users/alexanderlevkin/Desktop/My_projects/'
                                          'My_lessons_projects/Selenium/chromedriver')
# driver = webdriver.Safari()
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

time.sleep(2)

# driver.execute_script("window.scrollTo(0, 500)")  # scroll
action = ActionChains(driver)  # создали переменную что бы указать каким драйвером будет управлять ActionChains
red_t_shirt = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-onesie"]')  # создаем переменную в
# которой будем хранить наш локатор
action.move_to_element(red_t_shirt).perform()  # через метод move_to_element мы указываем куда мы должны двигаться

time.sleep(5)

now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
name_screenshot = 'screenshot ' + now_date + '.png'
driver.save_screenshot('./Screenshots/' + name_screenshot)

