from rental import Vehicle, Renter, ElectricCar, Motorbike


# Create vehicles
car = Vehicle("Toyota", "Yaris", "1AB234")
electric_car = ElectricCar("Tesla", "Model 3", "2CD567", 60)
motorbike = Motorbike("Honda", "Click", "3EF890", 125)

# Create a renter
renter = Renter("John", 12345)

print("Vehicles before rental:")
print(car)
print(electric_car)
print(motorbike)

# Rent and return a vehicle
print("\nRenting the Toyota Yaris")
car.rent()
print(car)

print("\nReturning the Toyota Yaris")
car.return_vehicle()
print(car)

# Show renter information
print("\nRenter:")
print("Name:", renter.name)
print("License:", renter.license_no)
print("Rented vehicles:", renter.rented)

# Try invalid renter data
print("\nTesting invalid renter data:")

try:
    Renter("", 12345)
except ValueError as error:
    print("Invalid name:", error)

try:
    Renter("John", 0)
except ValueError as error:
    print("Invalid license:", error)

# Polymorphism
print("\nMixed vehicle list:")
vehicles = [car, electric_car, motorbike]

for vehicle in vehicles:
    print(vehicle)
