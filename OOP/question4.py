class Vehicle:
    def __init__(self, name, maxSpeed, mileage):
        self.name = name
        self.maxSpeed = maxSpeed
        self.mileage = mileage
    
    def seatingCapacity(self, capacity):
        return f"The seating capacity of a {self.name} is{capacity} passengers"

class Bus(Vehicle):
    def seatingCapacity(self, capacity=50):
        return super().seatingCapacity(capacity=50)

SchoolBus = Bus("School Volvo", 180, 12)
print("Vehicle Name:", SchoolBus.name, 
    "Speed:", SchoolBus.maxSpeed, 
    "Mileage:", SchoolBus.mileage,)

print(SchoolBus.seatingCapacity())