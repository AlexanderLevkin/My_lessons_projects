class Character:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.weight = 100

    def description_character(self):
        description = "The name of new hero is " + str(self.name) + " and his age is " + str(self.age) + " and his " \
                                                                                                         "weight is " \
                      + str(self.weight)
        return description

    def update_weight(self, kg):
        self.weight = kg


class Human(Character):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.humanity = 100

    def description_character(self):
        description = f"The name of new hero is {self.name} his age is {self.age} his weight is {self.weight} " \
                      f"He is humanity {self.humanity}"
        return description

    def update_humanity(self, h):
        self.humanity = h


man = Human("Nick", 34)
man.update_weight(70)
print(man.description_character())
man_2 = Human("Boris", 28)
man_2.update_humanity(85)
print(man_2.description_character())


class Warrior(Character):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.rage = 200

    def description_character(self):
        description = f"The name of new hero is {self.name} his age is {self.age} his weight is {self.weight} " \
                      f"He is rage {self.rage}"
        return description

    def update_rage(self, r):
        self.rage = r


warrior_1 = Warrior("Conan", 32)
warrior_1.update_weight(200)
print(warrior_1.description_character())
warrior_2 = Warrior("Jax", 28)
warrior_2.update_weight(230)
warrior_2.update_rage(178.2)
print(warrior_2.description_character())


class Archer(Character):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.accuracy = 100

    def description_character(self):
        description = f"The name of new hero is {self.name} his age is {self.age} his weight is {self.weight} " \
                      f"He is accuracy {self.accuracy}"
        return description

    def update_accuracy(self, a):
        self.accuracy = a


archer_1 = Archer("Mark", 20)
archer_1.update_weight(60)
print(archer_1.description_character())
archer_2 = Archer("Sam", 21)
archer_2.update_weight(80)
archer_2.update_accuracy(40)
print(archer_2.description_character())
