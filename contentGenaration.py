from google import genai
from google.genai import types
from dotenv import dotenv_values

config = dotenv_values(".env")

# get gemini API key from .env file
key = config['API_KEY']

try:
    # connecting with gemini
    client =genai.Client(api_key=key)
except Exception as e:
    print('gemini not connected')
    client = None

# this function will get text as parameter and according to parameter generate output
def generate_content(paragraph):
    if not client:
        return "Error there is No API KEY initialized."

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=paragraph,
            config=types.GenerateContentConfig(
                system_instruction="You are a Human. Your name is Harry.",
                max_output_tokens=400,
                temperature=0.3
            )
        )
        if hasattr(response, 'text'):
            return response.text
        else:
            print(f"Unexpected response: {response}")
            return "Error: couldn't get expected response"

    except Exception as e:
        print(f"Error generating output: {e}")
        return f"Failed to generate output ({e})"
