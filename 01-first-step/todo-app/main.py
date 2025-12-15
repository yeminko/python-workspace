from utility import printTodos, handleAddTodo, markAsDone, deleteTodo, deleteAllTodos
from models.todo import Todo

todos: list[Todo] = []
done_todos: list[str] = []

print('Welcome from My Todo App. Type \'q\' to quit.')

while True:
    print('Select an option')
    print('(1) Add (2) Mark as done (3) Delete (4) Delete All')

    try:
        option = input('Enter an option: ')
        print()

        if option == '1':
            todos += handleAddTodo()
            printTodos(todos, done_todos)
        elif option == '2':
            markAsDone(todos, done_todos)
            printTodos(todos, done_todos)
        elif option == '3':
            deleteTodo(todos)
            printTodos(todos, done_todos)
        elif option == '4':
            deleteAllTodos(todos)
            printTodos(todos, done_todos)
        elif option == 'q':
            break
    except KeyboardInterrupt:
        print('\nBye Bye!')
        break
