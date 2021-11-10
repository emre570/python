class Vehicle:
    color = "White"

    def __init__(self, name, maxSpeed, mileage):
        self.name = name
        self.maxSpeed = maxSpeed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

SchoolBus = Bus("School Volvo", 180, 12)
print(SchoolBus.color, SchoolBus.name,
"Speed:", SchoolBus.maxSpeed,
"Mileage", SchoolBus.mileage)

car = Car("Audi Q5", 240, 18)
print(car.color, car.name,
"Speed:", car.maxSpeed,
"Mileage:", car.mileage)