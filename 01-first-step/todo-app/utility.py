def addTodo(todos):
    while True:
        todo = input('Add Todo: ')
        if todo == 'done':
            break
        todos.append(todo)


def printTodos(todos):
    print('Your todos are: ')
    for index, todo in enumerate(todos):
        print(f'{index+1}. {todo}')
    print('\n')
