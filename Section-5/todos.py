
todos = []
while True:

        user_action = input("Type add, show, edit, complete or exit: ")
        user_action = user_action.strip() # to clear any tailing white  spaces while entering the string
        match user_action:
            case 'add':
                todo = input("Enter a todo: ")
                todos.append(todo)

            case 'show':
                #print(todos) # this shows the items in a list
                #for item in todos:
                    #print(item) # this prints out items without  a list
                for index, item in enumerate(todos) :
                    #print(index, '-', item) # this will print a space beween the index and the - and another space between - and item
                    print(f"{index + 1}-{item}")

            case 'edit':
                 number = int(input("Number of the todo to edit: "))
                 #print(number)
                 number = number - 1
                 #present_todo = todos[number]
                 new_todo = input("Enter a new todo")
                 todos[number] = new_todo
                 #print(present_todo)

            case 'complete':
                number = int(input("Number of tod to complete: "))
                todos.pop(number -1)
            case 'exit':
                break

print("Bye")