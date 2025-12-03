from utility import printTodos, addTodo

todos = []
done_todos = []

print('Welcome from My Todo App. Select an option to start! Type \'q\' to quit.')

while True:
    print('1. Add todo')
    print('2. Mark as done')
    print('3. Delete a todo')
    print('4. Delete all todos')

    option = input('Enter an option: ')

    if option == '1':
        addTodo(todos)
        printTodos(todos)
    elif option == 'q':
        break
