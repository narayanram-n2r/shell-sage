import os
import argparse

from utils.model import ModelConfig
from llm.base_model import OpenAILLM
from utils.logger import Logger

def parse_args():
    parser = argparse.ArgumentParser(description="Shell Sage")
    parser.add_argument(
        "--model_config",
        "-mc",
        type=str,
        default="config/model.json",
        help="Path to model config file",
    )
    parser.add_argument(
        "--prompt_template",
        "-t",
        type=str,
        default="./templates/base_prompt.txt",
        help="Path to template file",
    )
    parser.add_argument(
        "--logger_config",
        "-lc",
        type=str,
        default="config/logger.ini",
        help="Path to logger config file",
    )
    
    os.makedirs("logs", exist_ok=True)

    return parser.parse_args()


def main():
    args = parse_args()
    logger = Logger(args.logger_config).get_logger()

    model_config = ModelConfig(args.model_config)
    logger.info("Model config loaded")
    logger.info(f"Model config: {model_config}")

    llm = OpenAILLM(model_config, args.prompt_template)
    logger.info("Model loaded")

if __name__ == "__main__":
    main()
