class Person():
    """Создаём человека"""

    def __init__(self, name, age, height):
        """Инициализируем атрибуты человека"""
        self.name = name
        self.age = age
        self.height = height
        self.weight = 100

    def description_person(self):
        """Получение описания человека"""
        description = self.name + ", ему " + str(self.age) + " лет, его рост " + str(self.height) + " и вес " + str(self.weight)
        print("Нового человека зовут " + description)

    def get_weight(self):
        print("Вес нашего человека: " + str(self.weight))

    def update_weight(self, kg):
        """изменение веса человека"""
        self.weight = kg


class Warrior(Person):
    """Создаем класс война"""
    def __init__(self, name, age, height):
        """Инициализируем атрибуты родителя"""
        super().__init__(name, age, height)
        self.rage = 100

    def get_rage(self):
        print("Заряд ярости равен: " + str(self.rage))

    def description_person(self):
        """Переопределение метода родителя"""
        description = self.name + ", ему " + str(self.age) + " лет, его рост " + str(self.height) + " и его заряд " \
                                                                                                    "ярости " + str(
            self.rage)
        # print("Нового человека зовут " + description)
        return description


warrior = Warrior("Conan", 32, 200)
# warrior.description_person()
print("Нового человека зовут " + warrior.description_person())




