import functions
import PySimpleGUI as pg
print(pg)

# 1 create layout
label = pg.Text("Enter a todo")
input_box = pg.InputText(tooltip="Enter todo", key="todo")
add_button = pg.Button("Add")
list_box = pg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events= True, size=[45,10])
edit_button = pg.Button("Edit")

layout = [[label], [input_box, add_button],[list_box, edit_button]]

# 2 create a window

window = pg.Window("My todo App", layout, font=("Helvetica", 15))

# 3 Event loop
'''
while True:
    event, values = window.read()
    if event == "Cancel" or event == pg.WIN_CLOSED:
        break
    print(values[0])
    print(values[1])'''
# 4 close window
while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append((new_todo))
            functions.write_todos(todos)
            window["todos"].update(values=todos)

        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"]

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index]= new_todo
            functions.write_todos(todos)
            window["todos"].update(values=todos)

        case "todos":
            window["todo"].update(value=values["todos"][0])
        case pg.WIN_CLOSED:
            break

window.close()