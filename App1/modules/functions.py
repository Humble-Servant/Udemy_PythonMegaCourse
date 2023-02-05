FILEPATH = "tasks.txt"


def get_tasks(filepath=FILEPATH):
    """
    Read and return a list of tasks from a text file. 
    """
    try:
        with open(filepath, 'r') as file:
            local_tasks = file.readlines()
        return local_tasks
    except FileNotFoundError:
        local_tasks = []
        return local_tasks


def write_tasks(local_tasks, filepath=FILEPATH):
    """
    Write To-Do task list to a text file.
    """
    with open(filepath, 'w') as file:
        file.writelines(local_tasks)


if __name__ == "__main__":
    print(get_tasks())
