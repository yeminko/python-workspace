cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


# Checking value exist
print("bmw" in cars)
print("toyota" not in cars)


# If-elseIf-else
score = 45

if score < 40:
    print("Fail")
elif score > 40 and score < 80:
    print("Pass")
else:
    print("High Score")


# Empty Check
topping = []

if topping:
    print("topping exist")
else:
    print("topping doesn't exist")
