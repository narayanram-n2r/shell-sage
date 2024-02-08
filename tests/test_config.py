import unittest
from utils.model import ModelConfig


class TestModel(unittest.TestCase):
    def test_initialize(self):
        config = ModelConfig("../config/model.json")
        self.assertIsInstance(config, ModelConfig)
        self.assertEqual(config["model"], "gpt-3.5-turbo")
        self.assertEqual(config["api_version"], "2023-05-15")


if __name__ == "__main__":
    unittest.main()
