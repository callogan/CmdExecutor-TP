import importlib.util
import os


executed_cmds = set()


def execute_cmds(module_code) -> None:
    """
    Loads the module from code string and executes commands
    contained in CMDS variable.

    Parameters:
    module_code (str): The string with the Python module code,
    containing CMDS variable.

    Effects:
    Executes commands from variable CMDS, passing already executed commands
    and them to the list of executed commands.
    Outputs commands and notification about repetition.
    """
    module_name = 'temp_module'
    spec = importlib.util.spec_from_loader(module_name, loader=None)
    module = importlib.util.module_from_spec(spec)
    exec(module_code, module.__dict__)

    if hasattr(module, 'CMDS'):
        for cmd in module.CMDS:
            if cmd not in executed_cmds:
                print(cmd.split()[-1])
                os.system(cmd)
                executed_cmds.add(cmd)
            else:
                print(f"The command '{cmd}' has already been executed")


def collect_files(directory) -> list:
    """
    Collects all the Python files (.py) from the directory tree
    and sorts them in the alphabetical order.

    Parameters:
    directory (str): The path to the directory from which collecting
    files is required.

    Returns:
    list: The list of paths to Python files, sorted in the alphabetical order.

    Description:
    The function iterates through all the directories and files,
    contained in given directory, and collects all the files
    with .py extension. Received paths to files subsequently are sorted
    in the alphabetical order for the further processing.
    """
    py_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                py_files.append(file_path)

    py_files.sort()
    return py_files


def main(directory) -> None:
    """
    Main function for collecting, processing and executing commands
    from Python files in given directory.

    Parameters:
    directory (str): The path to the directory
    which contains the Python files with commands.

    Description:
    The function initially collects all the Python files
    from the given directory, sorts them in the alphabetical order,
    and then consecutively opens every file, reads the code and executes
    commands from CMDS variable, in the case it is present in the file.
    All the commands are being executed only one time, repeated commands
    are being passed.
    """
    sorted_files = collect_files(directory)

    for file_path in sorted_files:
        with open(file_path, 'r') as file:
            module_code = file.read()
            execute_cmds(module_code)


if __name__ == '__main__':
    main('tests/')
