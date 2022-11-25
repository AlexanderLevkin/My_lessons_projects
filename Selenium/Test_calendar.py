import time
import datetime
from datetime import date
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome, Firefox, Remote, ActionChains, Keys
driver = Chrome(executable_path=ChromeDriverManager().install())

now_date = datetime.datetime.now()
time_delta = datetime.timedelta(days=10)
new_date = now_date + time_delta
new_new_date = new_date.month, new_date.day, new_date.year
print(new_new_date)

# n = str(new_new_date)
# x = str(n.split(" "))
# y = x[2:12]
# z = str(y)
# z.replace("-", "/")
# print(z)
# base_url = 'https://demoqa.com/date-picker'
# driver.get(base_url)
# driver.maximize_window()
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
# new_date.click()
# new_date.clear()
# new_date.send_keys(z)
# time.sleep(3)

