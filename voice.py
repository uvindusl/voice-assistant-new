import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()

# Initialize the engine ONCE at the top level of the script
engine = pyttsx3.init()

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
                Speak_text(MyText)


        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("Could not understand audio")


if __name__ == '__main__':
    speech_recognizing()