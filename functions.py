
FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


# Non-default parameters must stand before default parameters, otherwise you get an error message
def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


# The following if condition has the effect that the code under it is only executed when the file
# is executed directly and not e.g. via import
if __name__ == "__main__":
     print("Hello")
     print(get_todos())
