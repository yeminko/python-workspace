from models.todo import Todo


def handleAddTodo() -> list[Todo]:
    todos: list[Todo] = []

    while True:
        title = input('Add Todo: ')
        if title == 'done':
            break

        todo = Todo(title)
        todos.append(todo)

    return todos


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


def printTodos(todos: list[Todo]) -> None:

    undone_todos = list(filter(lambda todo: not todo.isDone, todos))

    print('\nYour todos are: ')

    if not todos:
        print('No todos for today!')

    for index, todo in enumerate(todos):
        if not todo.isDone:
            print(f'{index+1}. {todo.title}')

    if done_todos:
        print('Your done todos are: ')
        for index, done in enumerate(done_todos):
            print(f'{index+1}. {done}')
    print()
