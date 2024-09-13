import os
import importlib.util

executed_cmds = set()


def execute_cmds(file_path):
    global executed_cmds
    spec = importlib.util.spec_from_file_location("module.name", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    if hasattr(module, 'CMDS'):
        for cmd in module.CMDS:
            if cmd not in executed_cmds:
                print(cmd.split()[-1])
                os.system(cmd)
                executed_cmds.add(cmd)
            else:
                print(f"The command '{cmd}' have already been executed")


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
        execute_cmds(file_path)


if __name__ == "__main__":
    main("tests/")
