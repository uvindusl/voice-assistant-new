import speech_recognition as sr
import pyttsx3
import contentGenaration

# Initialize the recognizer
r = sr.Recognizer()

# Initialize the engine
engine = pyttsx3.init()


# Adjust volume
volume = engine.getProperty('volume')
print(f'Current volume level: {volume}')
engine.setProperty('volume', 1.0)

# Change voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Selecting a female voice

# The function to convert text to speech now uses the pre-initialized engine
def speak_text(command):
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
                    speak_text('Goodbye')
                    break
                speak_text(contentGenaration.generate_content(MyText))


        except sr.RequestError as e:
            speak_text('Could not request results')
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            speak_text('Could not recognize your voice')
            print("Could not understand audio")


if __name__ == '__main__':
    speech_recognizing()