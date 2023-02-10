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





"""while True:
        # Get user input and strip space chars from it
        user_action = input("Type add, show, edit, complete or exit: ")
        user_action = user_action.strip() # to clear any tailing white  spaces while entering the string

        match user_action:
            case 'add':
                todo = input("Enter a todo: ") + "\n"

                with open("todos.txt", "r") as file:
                    todos = file.readlines()

                todos.append(todo)

                with open("todos.txt", "w") as file:
                    file.writelines(todos)

            case 'show':

                with open("todos.txt" ,"r") as file:
                    todos = file.readlines()

                for index, item in enumerate(todos) :
                    item = item.strip('\n')
                    row = f"{index + 1}-{item}"
                    print(row)
"""
           """ case 'edit':
                 number = int(input("Number of the todo to edit: "))
                 number = number - 1

                 with open("todos.txt", "r") as file:
                     todos = file.readlines()

                 #present_todo = todos[number]
                 new_todo = input("Enter a new todo")
                 todos[number] = new_todo + 
                # print("Existing todos, todos ", todos)

                 with open("todos.txt", "w") as file:
                     file.writelines(todos)

            case 'complete':
                number = int(input("Number of tod to complete: "))
                with open("todos.txt", "r") as file:
                    todos = file.readlines()
                index = number -1
                todo_to_remove = todos[index].strip()
                todos.pop(index)

                with open("todos.txt", "w") as file:
                    file.writelines(todos)

                message = f"Todo {todo_to_remove} was removed from the list. "
                print(message)

            case 'exit':
                break

print("Bye")
"""