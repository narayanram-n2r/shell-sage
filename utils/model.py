import os
import json

from typing import Dict


class ModelConfig:
    """
    Class to load the model configuration from a json file.

    Args:
    config_path (str, optional): Path to the model configuration file. Defaults to None.
    """

    def __init__(self, config_path: str = None):
        self.config = self.load_config(config_path)

    def load_config(self, config_path: str = None) -> Dict:
        """
        Load the model configuration from a json file.

        Args:
        config_path (str, optional): Path to the model configuration file. Defaults to None.

        Returns:
        dict: Model configuration
        """
        if config_path is None:
            config_path = os.path.join(
                os.path.dirname(__file__), "../config/model.json"
            )

        with open(config_path, "r") as f:
            config = json.load(f)
        return config

    def __str__(self) -> str:
        """
        Return the model configuration as a string.

        Returns:
        str: Model configuration as a string
        """
        return json.dumps(self.config, indent=4)

    def __getitem__(self, key: str) -> any:
        """
        Get a specific configuration value.

        Args:
        key (str): Key to retrieve from the configuration

        Returns:
        any: Value of the key in the configuration
        """
        return self.config[key]
