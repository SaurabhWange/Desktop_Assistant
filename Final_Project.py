import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime
import os

##### setting the voice for the assistant , i am using the microsoft speach api to develop the project
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
# print(voices[1].id)


def speak(audio):
    """ This function is used to speak the audio input  """
    engine.say(audio)
    engine.runAndWait()


def wishme():

    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        speak("Good Morning Sir, How can i help you ?")
    elif 12 <= hour < 18:
        speak("Good Afternoon Sir, How can i help you ?")
    else:
        speak("Good Evening Sir, How can i help you ?")


def take_command():

    recogniser = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        recogniser.pause_threshold = 1  # threshold ignores the time when we stop to think  some command to it
        audio = recogniser.listen(source)

    try:
        print("Recognizing....")
        query = recogniser.recognize_google(audio,language="en-in")
        print(f"User said {query}\n")

    except Exception as e:
        print(e)

        print("Say that again please....")
        return "None"
    return query


if __name__ == '__main__':

    # speak("hey saurabh, how are you brother ?")
    wishme()
    while True:
        query = take_command().lower()

        if "wikipedia" in  query:
            speak("Searching wikipedia....")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("Acccording to wikipedia")
            print(result)
            speak(result)

        elif "is your name" in query:
            speak("My name is Sarah")

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "play music" in query:
            path = "F:\\New Songs"
            songs = os.listdir(path)
            print(songs)
            os.startfile(os.path.join(path,songs[0]))

        elif "the time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f" Sir  the time is {strtime}")

        elif "open pycharm" in query:
            path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1.4\\bin\\pycharm64.exe"
            os.startfile(path)