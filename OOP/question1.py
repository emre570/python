class Vehicle:
    def __init__(self, maxSpeed, mileage):
        self.maxSpeed = maxSpeed
        self.mileage = mileage

modelX = Vehicle(240, 18)
print(modelX.maxSpeed, modelX.mileage)