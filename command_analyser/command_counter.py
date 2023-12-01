from collections import Counter


class CommandCounter:
    def __init__(self, commands):
        self.commands = commands

    def count_command_frequency(self):
        command_count = Counter(self.commands)
        return command_count
