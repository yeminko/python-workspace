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
    print('delete todo..')


def printTodos(todos: list[str], done_todos: list[str]) -> None:
    print('Your todos are: ')
    for index, todo in enumerate(todos):
        print(f'{index+1}. {todo}')

    if done_todos:
        print('Your done todos are: ')
        for index, done in enumerate(done_todos):
            print(f'{index+1}. {done}')
    print('============================')
