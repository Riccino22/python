def get_todos():
    with open("web_todoapp/todos.txt", "r") as file:
        todos = file.readlines()
    todos_list = []
    for todo in todos:
        todos_list.append(todo.strip())
    return todos_list

def create_todo(todo):
    todos = get_todos()
    todos.append(todo)
    with open("web_todoapp/todos.txt", "w") as file:
        for todo in todos:
            file.write(todo + "\n")
    print(todos)


def delete_todo(todo_index):
    todos = get_todos()
    del todos[todo_index]
    with open("web_todoapp/todos.txt", "w") as file:
        for todo in todos:
            file.write(todo + "\n")
    print(todos)

delete_todo(1)
    
