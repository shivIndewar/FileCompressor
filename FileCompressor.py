import FreeSimpleGUI as fsgui
import zip_creator

label1 = fsgui.Text("Select files to compress:")
input1 = fsgui.Input()
choose_button1 = fsgui.FilesBrowse("Choose", key="files")

label2 = fsgui.Text("Select destination folder:")
input2 = fsgui.Input()
choose_button2 = fsgui.FolderBrowse("Choose", key="folder")

compress_button = fsgui.Button("Compress", key="compress")
output_label = fsgui.Text(key="output")

window = fsgui.Window(title="File Compressor",
                      layout=[[label1, input1, choose_button1],
                              [label2, input2, choose_button2],
                              [compress_button, output_label]])
while True:
    event, values = window.read()
    print(event, values)
    file_paths = values["files"].split(";")
    folder = values["folder"]
    zip_creator.compress_file(file_paths, folder)
    window["output"].update(value="Compression completed!")
window.close()