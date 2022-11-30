import time
import datetime

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome, Firefox, Remote, ActionChains, Keys
from selenium.webdriver.support import expected_conditions

driver = Chrome(executable_path=ChromeDriverManager().install())

base_url = 'https://demoqa.com/dynamic-properties'
driver.get(base_url)
# driver.maximize_window()
# driver.implicitly_wait(10)

# print("Start test")
# visible_button = driver.find_element(By.CSS_SELECTOR, '#visibleAfter')
# visible_button.click()
# print("Finish test")

print("Start test")
visible_button = WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#visibleAfter')))
visible_button.click()
print("Finish test")