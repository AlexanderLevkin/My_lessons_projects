class Cars:
    def __init__(self, model, age, volume, price, mileage):
        self.model = model
        self.age = age
        self.volume = volume
        self.price = price
        self.mileage = mileage
        self.wheels = 4

    def description_car(self):
        description = f"This is a {self.model} car, year of " \
                      f"manufacture this car is {self.age} , it volume is {self.volume}, " \
                      f"price of this car is {self.price}$, mileage is {self.mileage}km, and " \
                      f"this model has {self.wheels} wheels"
        return description


volovo = Cars("Volvo XC90", 2020, 2.8, 45000, 35000)
print(volovo.description_car())


class Trucks(Cars):
    def __init__(self, model, age, volume, price, mileage):
        super().__init__(model, age, volume, price, mileage)
        self.wheels = 8

    def description_car(self):
        description = f"This is a {self.model} car, year of " \
                      f"manufacture this car is {self.age} , it volume is {self.volume}, " \
                      f"price of this car is {self.price}$, mileage is {self.mileage}km, and " \
                      f"this model has {self.wheels} wheels"
        return description


lorry = Trucks("MAN", 2010, 3.5, 400000, 250000)
print(lorry.description_car())


