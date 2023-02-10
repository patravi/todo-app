while True:
        # Get user input and strip space chars from it
        user_action = input("Type add, show, edit, complete or exit: ")
        user_action = user_action.strip() # to clear any tailing white  spaces while entering the string

        #match user_action:
        if 'add' in user_action:
            todo = user_action[4:]
            with open("todos.txt", "r") as file:
                todos = file.readlines()
            todos.append(todo)
            with open("todos.txt", "w") as file:
                file.writelines(todos)


        elif 'show' in user_action:
            with open("todos.txt" ,"r") as file:
                todos = file.readlines()



            for index, item in enumerate(todos) :
            #for index, item in enumerate(new_todos):
                item = item.strip('\n')
                #print(index, '-', item) # this will print a space beween the index and the - and another space between - and item
                row = f"{index + 1}-{item}"
                print(row)

       #case 'edit':
        elif 'edit' in user_action:
             number = int(user_action[5:])
             print(number)
             number = number - 1

             with open("todos.txt", "r") as file:
                 todos = file.readlines()

             #present_todo = todos[number]
             new_todo = input("Enter a new todo")
             todos[number] = new_todo + '\n'
            # print("Existing todos, todos ", todos)

             with open("todos.txt", "w") as file:
                 file.writelines(todos)

        #case 'complete':
        elif 'complete' in user_action:
            number = int(user_action[9:])
            with open("todos.txt", "r") as file:
                todos = file.readlines()
            index = number -1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open("todos.txt", "w") as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list. "
            print(message)

        #case 'exit':
        elif 'exit' in user_action:
            break
        else:
            print("Command is not valid")

print("Bye")