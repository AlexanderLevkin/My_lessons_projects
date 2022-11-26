import time
import datetime
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome, Firefox, Remote, ActionChains, Keys
driver = Chrome(executable_path=ChromeDriverManager().install())
# Используя библиотеку datetime получаем текущее время
now_date = datetime.datetime.now()
# К текущей дате прибавляем 10 дней с помощью объекта timedelta
time_delta = datetime.timedelta(days=10)
new_date = now_date + time_delta
# Расставляем в нужной последовательности месяц, день, год
new_new_date = new_date.month, new_date.day, new_date.year
# Так как new_new_date это tuple т.е кортеж, преобразуем его к str
str_date = str(new_new_date)
# Используем цепочку string методов replace что бы убрать лишние символы и добавить необходимые
new_str_date = str_date.replace('(', ' ').replace(', ', '/').replace(')', '/')
print(new_str_date)
# Заходим на сайт
base_url = 'https://demoqa.com/date-picker'
driver.get(base_url)
driver.maximize_window()
# находим необходимое поле и очищаем его
new_date = driver.find_element(By.XPATH, '//input[@id="datePickerMonthYearInput"]')
new_date.send_keys(Keys.BACKSPACE)
new_date.send_keys(Keys.BACKSPACE)
new_date.send_keys(Keys.BACKSPACE)
new_date.send_keys(Keys.BACKSPACE)
new_date.send_keys(Keys.BACKSPACE)
new_date.send_keys(Keys.BACKSPACE)
new_date.send_keys(Keys.BACKSPACE)
new_date.send_keys(Keys.BACKSPACE)
new_date.send_keys(Keys.BACKSPACE)
new_date.send_keys(Keys.BACKSPACE)
new_date.send_keys(Keys.BACKSPACE)
time.sleep(3)
# Отправляем дату
new_date.send_keys(new_str_date)
time.sleep(3)

