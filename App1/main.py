# from functions import get_tasks, write_tasks
from modules import functions
import time

prompt = "Enter add, show, edit, complete, or exit:"
tasks = []

now = time.strftime("%b %d, %Y  %H:%M:%S")

print(f"It is {now}.\n")

while True:
    choice = input(prompt)
    choice = choice.strip()

    if choice.startswith('add'):

        task = choice[4:] + '\n'
        tasks = functions.get_tasks()
        tasks.append(task)
        functions.write_tasks(tasks)

    elif choice.startswith('show'):

        print()
        tasks = functions.get_tasks()
        for index, item in enumerate(tasks):
            item = item.strip('\n')
            row = f"{index + 1}. {item}"
            print(row)
        print()

    elif choice.startswith('edit'):

        try:
            number = int(choice[5:]) - 1
            tasks = functions.get_tasks()
            tasks[number] = input("New task:") + "\n"
            functions.write_tasks(tasks)
        except ValueError:
            print("Command not valid.")
            continue

    elif choice.startswith('complete'):

        try:
            number = int(choice[9:]) - 1
            tasks = functions.get_tasks()
            completed = tasks.pop(number).strip('\n')
            print(f"\n{completed} completed.\n")
            functions.write_tasks(tasks)
        except ValueError:
            print("\nCommand not valid.\n")
            continue
        except IndexError:
            print("\nCommand not valid.\n")
            continue


    elif choice.startswith('exit'):
            break

print("Bye!")