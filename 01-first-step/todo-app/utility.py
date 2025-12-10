def addTodo(todos: list[str]) -> None:
    while True:
        todo = input('Add Todo: ')
        if todo == 'done':
            break
        todos.append(todo)


def markAsDone(todos: list[str], done_todos: list[str]) -> None:
    todoId = input('Enter todo\'s ID to mark as done: ')
    index = int(todoId) - 1
    done_todo: str = todos.pop(index)
    done_todos.append(done_todo)


def deleteTodo(todos: list[str]):
    todoId = input('Enter todo\'s ID to delete: ')
    index = int(todoId) - 1
    del todos[index]


def deleteAllTodos(todos: list[str]):
    todos.clear()


def printTodos(todos: list[str], done_todos: list[str]) -> None:
    print('\nYour todos are: ')

    if todos:
        for index, todo in enumerate(todos):
            print(f'{index+1}. {todo}')
    else:
        print('No todos for today!')

    if done_todos:
        print('Your done todos are: ')
        for index, done in enumerate(done_todos):
            print(f'{index+1}. {done}')
    print()
