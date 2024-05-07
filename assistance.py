


import wikipedia
import speech_recognition as sr
import pyttsx3

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source, timeout=5)
    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return None
    except sr.RequestError as e:
        print("Sorry, there was an error recognizing your speech. {0}".format(e))
        return None

def search_wikipedia(query):
    try:
        result = wikipedia.summary(query, sentences=20)
        return result
    except wikipedia.exceptions.DisambiguationError as e:
        options = e.options[:5]  # Limiting options to 5 for simplicity
        return f"Can you please specify? I found multiple options: {', '.join(options)}"
    except wikipedia.exceptions.PageError:
        return "Sorry, I couldn't find any information on that topic."
    except Exception as e:
        return f"Sorry, an error occurred: {str(e)}"

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def main():
    while True:
        command = listen()
        if command:
            if "exit" in command:
                print("Goodbye!")
                speak("Goodbye!")
                break
            else:
                print("Searching Wikipedia...")
                result = search_wikipedia(command)
                print("Wikipedia:", result)
                speak(result)

if __name__ == "__main__":
    main()

