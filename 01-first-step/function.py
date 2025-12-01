# Simple Function
def greet():
    """Display a simple greeting"""
    print("Hello")


greet()

# Function with args


def favorite_food(name, food):
    """Display user's favorite food"""
    print(f'{name} favorite food is {food}')


favorite_food('Max', 'Fried Rice')  # Positional Args
favorite_food(name='John', food='Papaya Salad')  # Keyword Args
