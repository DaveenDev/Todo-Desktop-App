import functions
import PySimpleGUI as gui
import time

gui.theme("DarkBlue2")
time_label = gui.Text('Time', key="time_label")
label = gui.Text("Type in a to-do")
input_box = gui.InputText(tooltip="Enter a todo", key="todo")
add_button = gui.Button("Add")

list_box = gui.Listbox(values=functions.get_todos(), key="todos",
                       enable_events=True, size=[45,10])
edit_button = gui.Button("Edit")
complete_btn = gui.Button("Complete")
exit_button = gui.Button("Exit")
window = gui.Window("My Todo App",
                    layout=[[time_label],
                            [label], [input_box, add_button],
                            [list_box, edit_button, complete_btn],
                            [exit_button]],
                    font=('Helvetica', 18))
while True:
    event, values = window.read(timeout=10)
    window['time_label'].update(value=time.strftime("%m.%d.%Y %H:%M:%S"))

    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values['todo']+"\n")
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + "\n"

                todos = functions.get_todos()
                index_to_edit = todos.index(todo_to_edit)
                todos[index_to_edit] = new_todo

                functions.write_todos(todos)

                window['todos'].update(values=todos)
            except IndexError as error:
                gui.popup("Please select an item to edit", font=("Helvetica", 20))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]

                todos = functions.get_todos()
                index_to_edit = todos.index(todo_to_complete)
                todos.remove(todo_to_complete)

                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError as error:
                gui.popup("Please select an item to complete", font=("Helvetica", 20))
        case "todos":
            window['todo'].update(value=values['todos'][0])
        case "Exit":
            break
        case gui.WINDOW_CLOSED:
            break;

window.close()

