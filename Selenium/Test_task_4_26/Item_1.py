import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome, Firefox, Remote

from Selenium.Test_task_4_26.Credentials import Main

print("Приветствую тебя в нашем интернет магазине")
print("Выбери один из следующих товаров и укажи его номер: 1 - Sauce Labs Backpack, 2 - Sauce Labs Bike Light,"
      "3 - Sauce Labs Bolt T-Shirt, 4 - Sauce Labs Fleece Jacket, 5 - Sauce Labs Onesie, "
      "6 - Test.allTheThings() T-Shirt (Red)")
product = input()

if product == "1":
    print("sauce_labs_backpack")
elif product == "2":
    print('sauce_labs_bike_light')
elif product == "3":
    print('sauce_labs_bolt_t_shirt')
elif product == "4":
    print('sauce_labs_fleece_jacket')
elif product == "5":
    print('sauce_labs_onesie')
elif product == "6":
    print('t_shirt_red')
else:
    print("This good is not avaliable")


class Product_1():
    driver = Chrome(executable_path=ChromeDriverManager().install())
    base_url = 'https://www.saucedemo.com'
    driver.get(base_url)
    driver.maximize_window()
    login_name = 'standard_user'
    password = 'secret_sauce'

    # Authorization on site
    login = Main(driver)
    login.login(login=login_name, password=password)

    # Selecting 2 goods
    driver.execute_script("window.scrollTo(0, 500)")
    time.sleep(1)

    red_kids_tshirt = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-onesie"]')
    red_kids_tshirt.click()
    time.sleep(1)
    red_adult_tshirt = driver.find_element(By.XPATH, '//button[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]')
    red_adult_tshirt.click()
    time.sleep(1)
    print("Select 2 goods: ")
    # Creating name and worth in variables
    # kids t-shirt
    red_kids_tshirt_name = driver.find_element(By.XPATH, '//*[@id="item_2_title_link"]/div')
    red_kids_tshirt_name = red_kids_tshirt_name.text
    print("-Name of first good is: " + red_kids_tshirt_name)
    red_kids_tshirt_cost = driver.find_element(By.XPATH,
                                               '//*[@id="inventory_container"]/div/div[5]/div[2]/div[2]/div')
    red_kids_tshirt_cost = red_kids_tshirt_cost.text
    print("It costs: " + red_kids_tshirt_cost)
    # adult t-shirt
    red_adult_tshirt_name = driver.find_element(By.XPATH, '//*[@id="item_3_title_link"]/div')
    red_adult_tshirt_name = red_adult_tshirt_name.text
    print("-Name of second good is: " + red_adult_tshirt_name)
    red_adult_tshirt_cost = driver.find_element(By.XPATH,
                                                '//*[@id="inventory_container"]/div/div[6]/div[2]/div[2]/div')
    red_adult_tshirt_cost = red_adult_tshirt_cost.text
    print("It costs: " + red_adult_tshirt_cost + "\n")
    time.sleep(1)

    # Transition to the cart
    driver.execute_script("window.scrollTo(0, 0)")
    time.sleep(1)
    cart_button = driver.find_element(By.XPATH, '//span[@class="shopping_cart_badge"]')
    cart_button.click()
    time.sleep(1)

    # Check the name and cost from cart with catalog data. Asserts
    cart_red_adult_tshirt_name = driver.find_element(By.XPATH, '//*[@id="item_3_title_link"]/div')
    cart_red_adult_tshirt_name = cart_red_adult_tshirt_name.text
    assert cart_red_adult_tshirt_name == red_adult_tshirt_name
    print("Name of adult t-shirt match with cart")

    cart_red_adult_tshirt_cost = driver.find_element(By.XPATH, '//*[@id="cart_contents_container"]'
                                                               '/div/div[1]/div[4]/div[2]/div[2]/div')
    cart_red_adult_tshirt_cost = cart_red_adult_tshirt_cost.text
    assert cart_red_adult_tshirt_cost == red_adult_tshirt_cost
    print("Cost of adult t-shirt match with cart\n")

    cart_red_kids_tshirt_name = driver.find_element(By.XPATH, '//*[@id="item_2_title_link"]/div')
    cart_red_kids_tshirt_name = cart_red_kids_tshirt_name.text
    assert cart_red_kids_tshirt_name == red_kids_tshirt_name
    print("Name of kids t-shirt match with cart")

    cart_red_kids_tshirt_cost = driver.find_element(By.XPATH, '//*[@id="cart_contents_container"]'
                                                              '/div/div[1]/div[3]/div[2]/div[2]/div')
    cart_red_kids_tshirt_cost = cart_red_kids_tshirt_cost.text
    assert cart_red_kids_tshirt_cost == red_kids_tshirt_cost
    print("Cost of kids t-shirt match with cart\n")
    # Click on checkout button

    checkout_button = driver.find_element(By.XPATH, '//button[@id="checkout"]')
    checkout_button.click()

    # Fill in the information about customer
    first_name_field = driver.find_element(By.XPATH, '//input[@id="first-name"]')
    first_name_field.send_keys("Alexander")
    last_name_field = driver.find_element(By.XPATH, '//input[@id="last-name"]')
    last_name_field.send_keys("Levkin")
    zip_code_field = driver.find_element(By.XPATH, '//input[@id="postal-code"]')
    zip_code_field.send_keys("777")

    continue_button = driver.find_element(By.XPATH, '//input[@id="continue"]')
    continue_button.click()
    time.sleep(1)

    # Calculate the total sum of goods from cart
    good_1 = float(red_adult_tshirt_cost.replace('$', " "))
    good_2 = float(red_kids_tshirt_cost.replace('$', " "))
    cart_sum = good_1 + good_2
    print(f"The total cost is: {cart_sum} $\n")

    # Comparing the sums
    items_total = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[5]')
    items_total = items_total.text
    items_sum = float(items_total.replace("Item total: $", " "))

    assert items_sum == cart_sum
    print(f"The sum from cart: {cart_sum} $ corresponds total sum: {items_sum} $!!!")
    time.sleep(5)
