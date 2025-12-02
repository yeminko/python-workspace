# *args will create a tuple
def order_pizza(size, *toppings):
    print(f'You ordered {size} pizza with following toppings: ')
    for topping in toppings:
        print(f'- {topping}')


order_pizza('large', 'Pineapple', 'Cheese', 'Hams')
