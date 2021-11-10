class Vehicle:
    def __init__(self, name, capacity, mileage):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity*100

class Bus(Vehicle):
    def fare(self):
        amount = super().fare()
        amount += amount*(10/100)
        return amount

SchoolBus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", SchoolBus.fare())