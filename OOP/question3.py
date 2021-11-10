class Vehicle:
    def __init__(self, name, maxSpeed, mileage):
        self.name = name
        self.maxSpeed = maxSpeed
        self.mileage = mileage

class Bus(Vehicle):
    pass

SchoolBus = Bus("School Volvo", 180, 12)
print("Vehicle Name:", SchoolBus.name, 
    "Speed:", SchoolBus.maxSpeed, 
    "Mileage:", SchoolBus.mileage)