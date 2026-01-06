from utility import print_todos, add_todo, mark_as_done, delete_todo, delete_all_todos
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
            todos += add_todo()
            print_todos(todos)
        elif option == '2':
            todos = mark_as_done(todos)
            print_todos(todos)
        elif option == '3':
            todos = delete_todo(todos)
            print_todos(todos)
        elif option == '4':
            todos = delete_all_todos()
            print_todos(todos)
        elif option == 'q':
            print('Bye Bye!')
            break
    except KeyboardInterrupt:
        print('\nBye Bye!')
        break
