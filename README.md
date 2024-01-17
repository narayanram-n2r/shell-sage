# shell-sage

Shell Sage is a Proof-of-Concept (POC) project aimed at enhancing Linux command usage by leveraging `bash_history` logs. This project utilizes Python and implements reinforcement learning techniques specifically the human-intervened Proximal Policy Optimization (PPO) algorithm, to fine-tune a comprehensive list of useful Linux commands.

## Overview

The primary goal of Shell Sage is to analyze user `bash_history` logs and identify frequently used Linux commands and employ reinforcement learning to refine and expand this list. By using human-intervened PPO. The project aims to enhance command suggestions and streamline Linux command-line operations.

## Project Structure

### Project Components

- [Command Analysis](command_analysis.md) - Details on analyzing `bash_history` logs.
- [Reinforcement Learning](reinforcement_learning.md) - Explanation of the PPO algorithm implementation.
- [Dataset](useful_commands_list.md) - Compilation of refined and expanded Linux command suggestions.

## Usage

### Installation

To run this project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/narayanram-n2r/shell-sage.git
    cd shell-sage
    ```

2. Install project dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Execute specific scripts or components using Python.

## Contributing

Contributions to Shell Sage are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create your feature branch: `git checkout -b feature/new-feature`.
3. Commit your changes: `git commit -am 'Add new feature'`.
4. Push to the branch: `git push origin feature/new-feature`.
5. Open a pull request.

## Contributors

This project is contributed to by:

- [n2r](https://github.com/narayanram-n2r)
- [sumanthsec](https://github.com/sumanthsec)
