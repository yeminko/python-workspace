from utility import printTodos, addTodo, markAsDone, deleteTodo

todos: list[str] = []
done_todos: list[str] = []

print('Welcome from My Todo App. Type \'q\' to quit.')

while True:
    print('Select an option')
    print('1. Add todo')
    print('2. Mark as done')
    print('3. Delete a todo')
    print('4. Delete all todos')

    option = input('Enter an option: ')

    if option == '1':
        addTodo(todos)
        printTodos(todos, done_todos)
    elif option == '2':
        markAsDone(todos, done_todos)
        printTodos(todos, done_todos)
    elif option == '3':
        deleteTodo(todos)
    elif option == 'q':
        break
