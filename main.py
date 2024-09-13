import importlib.util
import os


executed_cmds = set()


def execute_cmds(module_code):
    global executed_cmds
    module_name = "temp_module"
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


def collect_files(directory):
    py_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                py_files.append(file_path)

    py_files.sort()
    return py_files


def main(directory):
    sorted_files = collect_files(directory)

    for file_path in sorted_files:
        with open(file_path, "r") as file:
            module_code = file.read()
            execute_cmds(module_code)


if __name__ == "__main__":
    main("tests/")
