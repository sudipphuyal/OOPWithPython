class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        return f"{self.name} says something"
my_dog = Dog("Laika",5)
# print(my_dog.bark())

anotherDog = Dog("Kalo Kukur",4)
# print(anotherDog.bark())


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def description(self):
        return f"{self.year} {self.make} {self.model}"
    
my_car = Car("Toyota", "Corolla", 2020)
# print(my_car.description())


