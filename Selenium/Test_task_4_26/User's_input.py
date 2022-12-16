from Excutable_file import purchase_1, purchase_2, purchase_3, purchase_4, purchase_5, purchase_6

print("Приветствую тебя в нашем магазине")
print("Выберите один из следующих товаров и укажи его номер 1 - Sauce labs backpack, 2 - Sauce labs bike light"
      "3 - Labs bolt t shirt, 4 - Sauce labs fleece jacket, 5 - Test.allthethings()-t-shirt-(red), 6 -"
      "Sauce-labs-onesie")

while True:
      try:
            a = int(input())
            if a == 1:
                  print("Вы выбрали Sauce labs backpack")
                  purchase_1()
                  print("Спасибо за ваш выбор!")
                  break
            elif a == 2:
                  print("Вы выбрали Sauce labs bike light")
                  purchase_2()
                  print("Спасибо за ваш выбор!")
                  break
            elif a == 3:
                  print("Вы выбрали Labs bolt t shirt")
                  purchase_3()
                  print("Спасибо за ваш выбор!")
                  break
            elif a == 4:
                  print("Вы выбрали Sauce labs fleece jacket")
                  purchase_4()
                  print("Спасибо за ваш выбор!")
                  break
            elif a == 5:
                  print("Вы выбрали Test.allthethings()-t-shirt-(red)")
                  purchase_5()
                  print("Спасибо за ваш выбор!")
                  break
            elif a == 6:
                  print("Вы выбрали Sauce-labs-onesie")
                  purchase_6()
                  print("Спасибо за ваш выбор!")
                  break
            else:
                  print("Вы выбрали несуществующий товар. Пожалуйста выберите товар в диапазоне от 1 до 6: ")
                  print("1 - Sauce labs backpack, 2 - Sauce labs bike light"
                        "3 - Labs bolt t shirt, 4 - Sauce labs fleece jacket, 5 - Test.allthethings()-t-shirt-(red), 6 -"
                        "Sauce-labs-onesie")
      except ValueError as exception:
            print("Вы ввели недопустимый символ! Введите пожалуйста число от 1 до 6")


