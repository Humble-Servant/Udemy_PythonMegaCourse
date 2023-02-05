from modules import functions
import PySimpleGUI as sg
import time

sg.theme("Topanga")

clock = sg.Text("", key="clock")
label = sg.Text("Type a task")
input_box = sg.InputText(tooltip="Enter task", key='task')
add_button = sg.Button(key="Add", image_source="add.png", size=10, mouseover_colors="DarkBlue", tooltip="Add new task")
list_box = sg.Listbox(values=functions.get_tasks(), key='tasks', enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button(key="Complete", image_source="complete.png", tooltip="Complete a task")
exit_button = sg.Button("Exit")

window = sg.Window("My Task List App",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 12))

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    # print("Event:", event)
    # print("Values:", values)

    match event:
        case "Add":
            tasks = functions.get_tasks()
            new_task = values["task"] + "\n"
            tasks.append(new_task)
            functions.write_tasks(tasks)
            window['tasks'].update(values=tasks)
            window['task'].update(value="")
        case "Edit":
            try:
                task_to_edit = values['tasks'][0]
                new_task = values['task'] + "\n"
                tasks = functions.get_tasks()
                index = tasks.index(task_to_edit)
                tasks[index] = new_task
                functions.write_tasks(tasks)
                window['tasks'].update(values=tasks)
                window['task'].update(value="")
            except IndexError:
                sg.popup("Please select an item first", font=('Helvetica', 12))
        case "Complete":
            try:
                task_to_complete = values['tasks'][0]
                tasks = functions.get_tasks()
                tasks.remove(task_to_complete)
                functions.write_tasks(tasks)
                window['tasks'].update(values=tasks)
                window['task'].update(value="")
            except IndexError:
                sg.popup("Please select an item first", font=('Helvetica', 12))
        case "Exit":
            break
        case "tasks":
            selection = values['tasks'][0].strip("\n")
            window['task'].update(value=selection)
        case sg.WIN_CLOSED:
            break
        
window.close()
