import speech_recognition as sr
import pyttsx3
from google import genai
from google.genai import types
from dotenv import dotenv_values

# Initialize the recognizer
r = sr.Recognizer()
config = dotenv_values(".env")

# Initialize the engine
engine = pyttsx3.init()


# Adjust volume
volume = engine.getProperty('volume')
print(f'Current volume level: {volume}')
engine.setProperty('volume', 1.0)

# Change voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Selecting a female voice


key = config['API_KEY']

try:
    client =genai.Client(api_key=key)
except Exception as e:
    print('gemini not connected')
    client = None

# The function to convert text to speech now uses the pre-initialized engine
def Speak_text(command):
    engine.say(command)
    engine.runAndWait()

def speech_recognizing():
    while (1):
        try:
            # use the microphone as source for input.
            with sr.Microphone() as source2:
                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level
                r.adjust_for_ambient_noise(source2, duration=0.2)

                # listens for the user's input
                audio2 = r.listen(source2)

                # Using google to recognize audio
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()
                if (MyText == 'stop'):
                    Speak_text('Goodbye')
                    break
                Speak_text(generate_content(MyText))


        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("Could not understand audio")

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


if __name__ == '__main__':
    speech_recognizing()