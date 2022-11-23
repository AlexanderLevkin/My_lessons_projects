import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome, Firefox, Remote, ActionChains

driver = Chrome(executable_path=ChromeDriverManager().install())

base_url = 'https://demoqa.com/buttons'
driver.get(base_url)
driver.maximize_window()
time.sleep(1)
action = ActionChains(driver)
double = driver.find_element(By.XPATH, '//button[@id="doubleClickBtn"]')
action.double_click(double).perform()
assert_double_click = driver.find_element(By.XPATH, '//p[@id="doubleClickMessage"]')
assert_double_click = assert_double_click.text
assert assert_double_click == "You have done a double click"
print("Well done")
time.sleep(2)
right_click = driver.find_element(By.XPATH, '//button[@id="rightClickBtn"]')
action.context_click(right_click).perform()
assert_right_click = driver.find_element(By.XPATH, '//p[@id="rightClickMessage"]')
assert_right_click = assert_right_click.text
assert assert_right_click == "You have done a right click"
print("Well done")
time.sleep(2)
