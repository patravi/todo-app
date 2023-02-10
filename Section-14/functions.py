def get_todos(filepath = "todos-14.txt"):
    """ Read a text file and return
    the list of to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath = "todos-14.txt" ):
    """ write the to-do items in the text file."""
    with open('todos-14.txt', 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print ("Hi Hi")
    print (get_todos())