import unittest
import os
import shutil
import tempfile
import main


class TestCommandExecution(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def create_test_file(self, filename, content):
        with open(os.path.join(self.test_dir, filename), 'w') as file:
            file.write(content)

    def test_unique_commands(self):
        self.create_test_file('a.py', "CMDS = ['echo 1']")
        self.create_test_file('b.py', "CMDS = ['echo 2']")

        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(b"import os\nos.system('echo 1')\nos.system('echo 2')")
            temp_file.close()
            try:
                main.main(self.test_dir)
            finally:
                os.remove(temp_file.name)

    def test_repeated_commands(self):
        self.create_test_file('a.py', "CMDS = ['echo 1', 'echo 2']")
        self.create_test_file('b.py', "CMDS = ['echo 2', 'echo 3']")

        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(b"import os\nos.system('echo 1')\nos.system('echo 2')\nos.system('echo 3')")
            temp_file.close()
            try:
                main.main(self.test_dir)
            finally:
                os.remove(temp_file.name)

    def test_empty_cmds(self):
        self.create_test_file('a.py', "CMDS = []")

        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(b"import os\n")
            temp_file.close()
            try:
                main.main(self.test_dir)
            finally:
                os.remove(temp_file.name)

    def test_files_without_cmds(self):
        self.create_test_file('a.py', "# Empty file without variable CMDS")

        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(b"import os\n")
            temp_file.close()
            try:
                main.main(self.test_dir)
            finally:
                os.remove(temp_file.name)


if __name__ == "__main__":
    unittest.main()
