a = int(input("Привет, это простой калькулятор\nВведите первое число: "))
b = int(input("Введите второе число: "))
c = input("Введите арифметический знак из предложенных +, -, *, /: ")
if c == "+":
    print(f"Результат: {a + b}")
elif c == "-":
    print(f"Результат: {a - b}")
elif c == "*":
    print(f"Результат: {a * b}")
elif c == "/":
    try:
        c = int(a / b)
        print(f"Результат: {a / b}")
    except ZeroDivisionError:
        print("Ошибка: На ноль делить нельзя!")
else:
    print("Вы ввели неверный знак !!! Повторите еще раз, используя предложенные арифметические знаки +, -, *, /")
