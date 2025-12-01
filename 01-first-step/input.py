flag = True

while flag:
    name = input("Enter your name: ")

    if name == 'quit':
        flag = False
    else:
        print(f'Your name is: {name}')
