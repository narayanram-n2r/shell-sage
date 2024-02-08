import openai
import os

from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI

from typing import Dict, List, Any


class OpenAILLM:
    """
    Wrapper for the OpenAI language model

    Args:
        config (Dict[str, Any]): Configuration for the model
        prompt_file (str): File containing the prompt to be used
    """
    def __init__(self, config: Dict[str, Any], prompt_file : str = None):
        self.api_key = config["api_key"]
        self.api_version = config["api_version"]
        self.model = config["model"]
        self.temperature = config["temperature"]

        self.model = OpenAI(openai_api_key=self.api_key, openai_api_version=self.api_version, openai_model=self.model)

        if prompt_file is None:
            ValueError("Prompt file is required")

        with open(prompt_file, "r") as f:
            file_contents = f.read()
            self.prompt = PromptTemplate.from_template(file_contents)
        
        self.chain = self.prompt | self.model
        
    def generate(self, prompt_vars : Dict[str, Any]) -> str:
        """
        Generate a response from the model

        Args:
            prompt_vars (Dict[str, Any]): Variables to be used in the prompt

        Returns:
            str: The generated response
        """
        if not prompt_vars:
            ValueError("Prompt variables are required")

        return self.chain.invoke(prompt_vars)


            
    