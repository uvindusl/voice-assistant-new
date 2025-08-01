# Voice Assistant with Gemini AI

This is a personal voice assistant built with Python. It leverages Google's Gemini AI for content generation and a variety of libraries to handle speech recognition, text-to-speech, and web Browse commands.

## Features

* **Voice Recognition:** Understands and processes spoken commands.
* **AI-powered Content Generation:** Utilizes the Gemini API to generate creative and informative text.
* **Text-to-Speech:** Responds to your commands with a voice.
* **Time & Date:** Provides the current time and date upon request.
* **Web Browser Integration:** Opens specified websites like YouTube and GitHub with simple voice commands.

---

## Prerequisites

Before you run the assistant, you need to have **Python** installed on your system. This project was developed and tested on Python 3.x.

All required libraries are listed in the `requirements.txt` file. You can install them all with a single command.

```bash
pip install -r requirements.txt
````

**Note:** For the `PyAudio` library, you might need to install additional system-level dependencies depending on your operating system. For more information, please refer to the official PyAudio documentation.

-----

## Gemini API Key

This project requires a Google Gemini API key to generate AI content.

1.  Go to the [Google AI Studio](https://aistudio.google.com/) website.
2.  Follow the instructions to get an API key.
3.  Store your API key securely. You can create a file (e.g., `.env`) to hold it:

<!-- end list -->

```python
# .env
API_KEY = "YOUR_GEMINI_API_KEY"
```
-----

## Usage

1.  Clone this repository or download the project files.
2.  Install the required dependencies using the `requirements.txt` file (see the "Prerequisites" section).
3.  Open the main Python file (`main.py` or similar).
4.  Run the file from your terminal:

<!-- end list -->

```bash
python main.py
```

The assistant will start and wait for your command. You can then speak to it using the specified wake word or command structure (e.g., "Hello assistant...", "Hey there...").

-----

## Commands

Here are some example commands you can use with the assistant:

  * **"Open YouTube"**: Opens the YouTube website in your default browser.
  * **"Open GitHub"**: Opens the GitHub website in your default browser.
  * **"Generate some content about [topic]"**: Uses the Gemini AI to generate a response about the given topic.

-----

## Project Structure

  * `main.py`: The main script that initializes the assistant, handles speech recognition, and processes commands.
  * `contentGenaration.py`: A module that interfaces with the Gemini API to generate content.
  * `requirements.txt`: A list of all Python libraries needed for the project.
  * `README.md`: This file.

-----

## Libraries Used

  * **`speech_recognition`**: A library for performing speech recognition with support for various engines and APIs, online and offline.
  * **`pyttsx3`**: A cross-platform text-to-speech conversion library.
  * **`PyAudio`**: Required for `speech_recognition` to handle audio input from the microphone.
  * **`google-generativeai`**: The official Python library for the Google Gemini API.
  * **`datetime`**: A built-in Python module for working with dates and times.
  * **`webbrowser`**: A built-in Python module. I use this to open YouTube and GitHub.
