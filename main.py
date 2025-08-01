import speech_recognition as sr
import pyttsx3
import contentGenaration
import datetime
import webbrowser

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


def greeting():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        return "Good morning"
    elif hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"


def helping(query):
    while True:
        if 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            return f"The current time is {strTime}"

        else:
            return "Sorry, I didn't understand that. Try again."


def main():
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
                my_text = r.recognize_google(audio2)
                my_text = my_text.lower()

                if my_text == 'open youtube':
                    speak_text('opening youtube')
                    # helping('open youtube')
                elif my_text == 'open google':
                    speak_text('opening google')
                    # helping('open google')
                elif my_text == 'time':
                    speak_text(helping('time'))
                elif my_text == 'stop':
                    speak_text(contentGenaration.generate_content('bye'))
                    break
                else:
                    speak_text(contentGenaration.generate_content(my_text))

        except sr.RequestError as e:
            speak_text('Could not request results')
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            speak_text('Can you please say that again')
            print("Could not understand audio")


if __name__ == '__main__':
    main()