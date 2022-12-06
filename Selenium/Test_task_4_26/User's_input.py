print("Приветствую тебя в нашем магазине")
print("Выберите один из следующих товаров и укажи его номер 1 - Sauce labs backpack, 2 - Sauce labs bike light"
      "3 - Labs bolt t shirt, 4 - Sauce labs fleece jacket, 5 - Test.allthethings()-t-shirt-(red), 6 -"
      "Sauce-labs-onesie")
product = input()
from Excutable_file import *

if product == str(1):
      print("Вы выбрали Sauce labs backpack")
      purchase_1()
elif product == str(2):
      print("Вы выбрали Sauce labs bike light")
      purchase_2()
elif product == str(3):
      print("Вы выбрали Labs bolt t shirt")
      purchase_3()
elif product == str(4):
      print("Вы выбрали Sauce labs fleece jacket")
      purchase_4()
elif product == str(5):
      print("Вы выбрали Test.allthethings()-t-shirt-(red)")
      purchase_5()
elif product == str(6):
      print("Вы выбрали Sauce-labs-onesie")
      purchase_6()


