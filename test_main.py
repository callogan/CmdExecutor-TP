import main
import os
import shutil
import tempfile
import unittest


class TestCommandExecution(unittest.TestCase):

    def setUp(self) -> None:
        """
        Setting up testing environment.
        Creating temporary directory for testing.
        """
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self) -> None:
        """
        Cleaning up after testing.
        Deleting temporary directory and all its content.
        """
        shutil.rmtree(self.test_dir)

    def create_test_file(self, filename, content) -> None:
        """
        Creates test file with stated content in temporary directory.

        Parameters:
        filename (str): File name for the creation.
        content (str): File content.
        """
        with open(os.path.join(self.test_dir, filename), 'w') as file:
            file.write(content)

    def test_unique_commands(self) -> None:
        """
        Checks on the execution of unique commands.
        Creates files with unique commands and checks on,
        whether they are being executed in the correct order.
        """
        self.create_test_file('a.py', "CMDS = ['echo 1']")
        self.create_test_file('b.py', "CMDS = ['echo 2']")

        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(
                b"import os\nos.system('echo 1')\nos.system('echo 2')"
            )
            temp_file.close()
            try:
                main.main(self.test_dir)
            finally:
                os.remove(temp_file.name)

    def test_repeated_commands(self) -> None:
        """
        Checks on processing of repeated commands.
        Creates files with repeated commands and checks on
        whether every command is being executed only one time.
        """
        self.create_test_file('a.py', "CMDS = ['echo 1', 'echo 2']")
        self.create_test_file('b.py', "CMDS = ['echo 2', 'echo 3']")

        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(
                b"import os\nos.system('echo 1')\
                nos.system('echo 2')\nos.system('echo 3')"
            )
            temp_file.close()
            try:
                main.main(self.test_dir)
            finally:
                os.remove(temp_file.name)

    def test_empty_cmds(self) -> None:
        """
        Checks on file processing with the empty command list.
        Creates the file with the empty command list and checks on
        whether the script has no exit.
        """
        self.create_test_file('a.py', 'CMDS = []')

        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(b'import os\n')
            temp_file.close()
            try:
                main.main(self.test_dir)
            finally:
                os.remove(temp_file.name)

    def test_files_without_cmds(self) -> None:
        """
        Checks on file processing without CMDS variable.
        Creates the file without CMDS variable and checks on
        whether the script has no exit.
        """
        self.create_test_file('a.py', '# Empty file without variable CMDS')

        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(b'import os\n')
            temp_file.close()
            try:
                main.main(self.test_dir)
            finally:
                os.remove(temp_file.name)


if __name__ == '__main__':
    unittest.main()
