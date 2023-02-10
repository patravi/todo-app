# from functions import get_todos, write_todos
import functions
import time
now = time.strftime("%b %d, %Y %H:%M:%S")
print(now)
while True:
    user_action = input("Type add, show, edit, delete or exit: ") + "\n"
    user_action = user_action.strip() # to clear any tailing white  spaces while entering the string

    if user_action.startswith("add"):
        todo = user_action[4:]  # slicing the string

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos)


    elif user_action.startswith("show"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = get_todos()

            new_todo = input("Enter a new todo")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid")

            continue

    #elif 'delete' in user_action:
    elif user_action.startswith("delete"):
        try:
            number = int(user_action[7:])

            todos = functions.get_todos()
            index = number-1
            todo_to_remove = todos [index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number")
    #elif  'exit' in user_action:
    elif user_action.startswith("exit"):
        break
    else:
        print("command is not valid")
print("Bye")
