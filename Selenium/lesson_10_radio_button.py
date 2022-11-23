import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome, Firefox, Remote

driver = Chrome(executable_path=ChromeDriverManager().install())

base_url = 'https://demoqa.com/radio-button'
driver.get(base_url)
driver.maximize_window()
time.sleep(2)

radio_button = driver.find_element(By.XPATH, '//label[@class="custom-control-label"]')
radio_button.click()
time.sleep(2)
