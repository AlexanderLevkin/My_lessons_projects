import time
import datetime
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome, Firefox, Remote, ActionChains, Keys
driver = Chrome(executable_path=ChromeDriverManager().install())

base_url = 'https://html5css.ru/howto/howto_js_rangeslider.php'
driver.get(base_url)
driver.maximize_window()

action = ActionChains(driver)

price = driver.find_element(By.XPATH, '//*[@id="slidecontainer"]/input')
action.move_to_element(price).perform()
action.click_and_hold(price).move_by_offset(20, 0).release().perform()
print('Price +')
time.sleep(5)