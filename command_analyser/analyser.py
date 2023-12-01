from bash_history_parser import BashHistoryParser
from command_counter import CommandCounter


class Analyzer:
    def __init__(self, file_path):
        self.file_path = file_path

    def analyze_commands(self):
        parser = BashHistoryParser(self.file_path)
        parsed_commands = parser.parse_bash_history()

        command_counter = CommandCounter(parsed_commands)
        command_count = command_counter.count_command_frequency()

        sorted_commands = sorted(command_count.items(), key=lambda x: x[1], reverse=True)
        commands_dictionary = {cmd: freq for cmd, freq in sorted_commands}

        return commands_dictionary


def main():
    bash_history_path = "~./bash_history"  # path/to/bash_history_file

    analyzer = Analyzer(bash_history_path)
    commands_dictionary = analyzer.analyze_commands()

    print("\nCommands sorted by usage frequency:")
    for command, frequency in commands_dictionary.items():
        print(f"{command}: {frequency} times used")


if __name__ == "__main__":
    main()
