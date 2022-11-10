pin = 1234
user_pin = int(input("Enter the pin code: "))
if pin == user_pin:
    print("How much money do you want to cash")
else:
    print("Enter the correct pin you have 2 chances")
    user_pin = int(input("Enter the pin code: "))
    if pin == user_pin:
        print("How much money do you want to cash")
    else:
        print("Enter the correct pin you have 1 chances")
        user_pin = int(input("Enter the pin code: "))
        if pin == user_pin:
            print("How much money do you want to cash")
        else:
            print("You card has been blocking")