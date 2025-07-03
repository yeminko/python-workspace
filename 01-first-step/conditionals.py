cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


# Checking value exist
print("bmw" in cars)
print("toyota" not in cars)
