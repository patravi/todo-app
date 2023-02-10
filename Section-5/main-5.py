# to SHOW NUMBERS BEFORE each TODO "enumerate"
# USE OF f string

todos = []
while True:
        # Get user input and strip space chars from it
        user_action = input("Type add, show, edit, or exit: ")
        user_action = user_action.strip() # to clear any tailing white  spaces while entering the string

        match user_action:
            case 'add':
                todo = input("Enter a todo: ")
                todos.append(todo)
            case 'show':
                for index,item in enumerate(todos):
                    row = f"{index}-{item}"
                    print(row)

            case 'edit':
                 number = int(input("Number of the todo to edit: "))
                 number = number - 1
                 new_todo = input("Enter a new todo")
                 todos[number] = new_todo

            case 'exit':
                break

print("Bye")
