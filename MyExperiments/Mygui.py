# import functions
# import PySimpleGUI as pg
# print(pg)
"""
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


import PySimpleGUI as pg
button_labels = ("Add", "Edit", "Apply", "End",
                 "Cancel", "Undo", "Redo")
layout = []
for label in button_labels:
    layout.append([pg.Button(label)])

window = pg.Window("My to-do App", layout=layout)
window.read()
window.close()
"""
import PySimpleGUI as pg
from converters import convert

feet_label = pg.Text("Enter feet: ")
input_box1 = pg.InputText(key="feet")

inches_label = pg.Text("Enter inches: ")
input_box2 = pg.InputText(key="inches")

convert_btn = pg.Button("Convert")
output_label = pg.Text("", key="output")

layout = [[feet_label, input_box1],
          [inches_label, input_box2],
          [convert_btn, output_label]]
window = pg.Window("Convertor", layout)

while True:
    event, values = window.read()
    print(event, values)
    feet = float(values["feet"])
    inches = float(values["inches"])

    result = convert(feet, inches)
    window["output"].update(value=f"{result}, meters", text_color="white")
window.close()
