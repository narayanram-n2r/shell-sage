import os


class BashHistoryParser:
    def __init__(self, file_path):
        self.file_path = file_path

    def parse_bash_history(self):
        if not os.path.exists(self.file_path):
            print(f"File {self.file_path} does not exist.")
            return []

        with open(self.file_path, 'r') as history_file:
            commands = history_file.readlines()

        return [cmd.strip() for cmd in commands]
