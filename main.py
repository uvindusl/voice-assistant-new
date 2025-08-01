import datetime
import webbrowser

def wish_user():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        return "Good morning"
    elif hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"

def run_assistant(query):
    while True:
        if 'open youtube' in query:
            return "Opening YouTube..."
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            return "Opening Google..."
            webbrowser.open("https://www.google.com/")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            return f"The current time is {strTime}"

        elif 'exit' in query or 'bye' in query:
            return "Goodbye! Have a nice day!"
            break

        else:
            return "Sorry, I didn't understand that. Try again."