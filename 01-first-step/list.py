# For loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f'fruit is {fruit.title()}')
print(f"Thanks for coming. {fruit}")

# range from 1 to 4
for value in range(1, 5):
    print(value)

print(f'\n')

# range from 0 to 4
for value in range(5):
    print(value)

# Step range
numbers = list(range(1, 11, 2))
print(numbers)


# simple statistics
numbers = range(11)
print(max(numbers))
print(min(numbers))
print(sum(numbers))


# list comprehensions
squares = [value ** 2 for value in range(12)]
print(f'Squares Numbers: {squares}')
