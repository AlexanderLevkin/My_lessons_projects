import time
import datetime
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome, Firefox, Remote, ActionChains, Keys

driver = Chrome(executable_path=ChromeDriverManager().install())

base_url = 'https://demoqa.com/date-picker'
driver.get(base_url)
driver.maximize_window()

# new_date = driver.find_element(By.XPATH, '//input[@id="datePickerMonthYearInput"]')
# new_date.send_keys(Keys.BACKSPACE)
# new_date.send_keys(Keys.BACKSPACE)
# new_date.send_keys(Keys.BACKSPACE)
# new_date.send_keys(Keys.BACKSPACE)
# new_date.send_keys(Keys.BACKSPACE)
# new_date.send_keys(Keys.BACKSPACE)
# new_date.send_keys(Keys.BACKSPACE)
# new_date.send_keys(Keys.BACKSPACE)
# new_date.send_keys(Keys.BACKSPACE)
# new_date.send_keys(Keys.BACKSPACE)
# new_date.send_keys(Keys.BACKSPACE)
# time.sleep(3)
new_date = driver.find_element(By.XPATH, '//input[@id="datePickerMonthYearInput"]')
new_date.click()
time.sleep(3)
now_date = datetime.datetime.utcnow().strftime("%d")
print(now_date)
date = int(now_date) + 1
locator = "//div[@aria-label='Choose Thursday," + str(date) + "th, 2022']"
# aria-label="Choose Wednesday, November 23rd, 2022"
print(locator)
# new_date_17 = driver.find_element(By.XPATH, locator)
# new_date_17.click()
# time.sleep(3)

