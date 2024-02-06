import openai
from openai import OpenAI

# Set your OpenAI API key, then uncomment the line.
# openai.api_key = '<api-key>'
# OR
# gpt = OpenAI(
#     api_key = '<api-key>'
# )

def query_gpt(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",  # Update with the appropriate engine for GPT-4 or different model after checking. td002=>14%.
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {e}"


def ask_gpt_3(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",  # This is for testing.
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {e}"

def ask_gpt_4(prompt, bash_commamd):
    try:
        response = gpt.chat.completion.create(
            model="gpt-4",  # This is for testing.
            messages=[
                {
                    "role": "user",
                    "command": bash_command
                }
            ]
        )
        ## response.choices[0].message.content
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {e}"

