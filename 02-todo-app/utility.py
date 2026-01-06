from models.todo import Todo


def add_todo() -> list[Todo]:
    todos: list[Todo] = []

    while True:
        title = input('Add Todo: ')
        if title == 'done':
            break

        todo = Todo(title)
        todos.append(todo)

    return todos


def mark_as_done(todos: list[Todo]) -> list[Todo]:
    todoId = input('Enter todo\'s ID to mark as done: ')
    index = int(todoId) - 1

    return list(map(lambda todo: Todo(todo.title, True) if todos.index(todo) == index else todo, todos))


def delete_todo(todos: list[Todo]) -> list[Todo]:
    todoId = input('Enter todo\'s ID to delete: ')
    index = int(todoId) - 1

    return list(filter(lambda todo: todos.index(todo) != index, todos))


def delete_all_todos() -> list[Todo]:
    return []


def print_todos(todos: list[Todo]) -> None:

    undone_todos = list(filter(lambda todo: not todo.isDone, todos))
    done_todos = list(filter(lambda todo: todo.isDone, todos))

    print('\nYour todos are: ')

    if not undone_todos:
        print('No todos for today!')

    for index, todo in enumerate(undone_todos):
        print(f'{index+1}. {todo.title}')

    if done_todos:
        print('Your done todos are: ')
        for index, todo in enumerate(done_todos):
            print(f'{index+1}. {todo.title}')
    print()
