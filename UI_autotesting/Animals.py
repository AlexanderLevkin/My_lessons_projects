# class Animals():
#     def __init__(self, name, age, breed):
#         self.name = name
#         self.age = age
#         self.breed = breed
#         print("The Pet was created")
#
#     def move(self):
#         print(self.name + " Move forward")
#
#     def barking(self):
#         print(f"The {self.name} is barking!")
#
#     def breed_2(self):
#         print(f"the {self.name} breed is {self.breed}")
#
#
# dog = Animals("Puppy", 10, "bulldog")
# dog.move()
# dog.barking()
# dog.breed_2()


class Cars():
    def __init__(self, model, comp, year):
        self.model = model
        self.comp = comp
        self.year = year
        self.typ = "car"

    def description_cars(self):
        description = "This is " + str(self.model) + " and complectation this model is " + \
                      str(self.comp) + " it's " + str(self.year) \
                      + " and type of this car is " + str(self.typ)
        print(description)

    def update_cars(self, typ_2):
        self.typ = typ_2


bentley = Cars("Bentley", "Hight", 2022)
bentley.description_cars()
bentley.update_cars("Bentley")
bentley.description_cars()