import PySimpleGUI as gui

input1 = gui.InputText(key="feet")
input2 = gui.InputText(key="inches")
button = gui.Button("Convert")
status_label = gui.Text(key="status")
window = gui.Window("Converter",
                    layout=[[gui.Text("Enter Feet:"), input1],
                            [gui.Text("Enter inches"), input2],
                            [button, status_label]])

while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case "Convert":
            feet = float(values["feet"])
            inches = float(values["inches"])
            total_inches = (feet * 12) + inches
            meter = total_inches * 0.0254
            window["status"].update(value=f"{meter} m")
        case gui.WIN_CLOSED:
            break
window.close()