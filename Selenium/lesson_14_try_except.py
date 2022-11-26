import time
import datetime

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome, Firefox, Remote, ActionChains, Keys

driver = Chrome(executable_path=ChromeDriverManager().install())

base_url = 'https://demoqa.com/radio-button'
driver.get(base_url)
driver.maximize_window()
# try:
#     visible_button = driver.find_element(By.XPATH, '//button[@id="visibleAfter"]')
#     visible_button.click()
# except NoSuchElementException as exception:
#     print("we catch this exception")
#     time.sleep(5)
#     visible_button = driver.find_element(By.XPATH, '//button[@id="visibleAfter"]')
#     visible_button.click()
# time.sleep(3)

check_box_yes = driver.find_element(By.XPATH, '//label[@for="yesRadio"]')
check_box_yes.click()
time.sleep(2)
try:
    message = driver.find_element(By.XPATH, '//span[@class="text-success"]')
    value_message = message.text
    print(value_message)
    assert value_message == "No"
except AssertionError as exception:
    driver.refresh()
    time.sleep(5)
    check_box_yes = driver.find_element(By.XPATH, '//label[@for="yesRadio"]')
    check_box_yes.click()
    message = driver.find_element(By.XPATH, '//span[@class="text-success"]')
    value_message = message.text
    print(value_message)
    assert value_message == "Yes"
print('Test over')