import PySimpleGUI as gui
from zip_creator import make_archive

label1 = gui.Text("Select files to compress:")
input1 = gui.Input()
button1 = gui.FilesBrowse("Choose", key="files")

label2 = gui.Text("Select destination folder:")
input2 = gui.Input()
button2 = gui.FolderBrowse("Choose", key="dirpath")
btnCompress = gui.Button("Compress")
status_label = gui.Text(key="status", text_color="green")

window = gui.Window("File Compressor",
                    layout=[[label1, input1, button1],
                            [label2, input2, button2],
                            [btnCompress,status_label]]
                    )
while True:
    event, values = window.read()
    print(event)
    print(values)
    filepaths = values["files"].split(";")
    dirpath = values["dirpath"]
    match event:
        case "Compress":
            make_archive(filepaths, dirpath)
            print("hello")
    window["status"].update(value="Compression completed")
window.close()