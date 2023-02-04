from modules import functions
import PySimpleGUI as sg

label = sg.Text("Type a task")
input_box = sg.InputText(tooltip="Enter task")
add_button = sg.Button("Add")

window = sg.Window('My Task List App', layout=[[label], [input_box, add_button]])
window.read()
window.close()
