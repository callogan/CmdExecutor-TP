# CmdExecutor-TP

`CmdExecutor-TP` is a Python project that implements a script to execute shell commands 
contained in the `CMDS` variable from Python files within a directory tree. 
Commands are executed in alphabetical order of file paths, and duplicate commands are skipped.

## Description

The `main.py` script:
- Collects all the Python files from the specified directory.
- Sorts them alphabetically.
- Reads the content of each file and executes commands from the `CMDS` variable.
- Commands are executed only once, and duplicate commands are skipped.

## Project Structure

The project has the following structure:

### Main Script (`main.py`)

This script performs the following functions:
1. Collects all Python files from the directory.
2. Sorts them alphabetically.
3. Reads each file and executes commands from the `CMDS` variable.

### Testing

The project uses `unittest` for testing. The test functions check:
- Execution of unique commands.
- Handling of duplicate commands.
- Processing of files with an empty command list.
- Handling of files without the `CMDS` variable.

### Running Tests

1. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

2. Activate the virtual environment:
    - **Windows**:
        ```bash
        venv\Scripts\activate
        ```
    - **macOS/Linux**:
        ```bash
        source venv/bin/activate
        ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the tests:
    ```bash
    python -m unittest test_main.py
    ```

## Project Information

This project is created as a test assignment to evaluate skills in Python, 
file handling, and command execution.
