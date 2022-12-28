import functions
import PySimpleGUI as gui

label = gui.Text("Type in a to-do")
input_box = gui.InputText(tooltip="Enter a todo", key="todo")
add_button = gui.Button("Add")

window = gui.Window("My Todo App",
                    layout=[[label], [input_box, add_button]],
                    font=('Helvetica', 18))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values['todo']+"\n")
            functions.write_todos(todos)
        case gui.WINDOW_CLOSED:
            break;

window.close()

