import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime


#Initialize Voice Engine
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def take_commands():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening......")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing....")
        command = recognizer.recognize_google(audio)
        print("You said :",command)
        return command.lower()
    
    except Exception:
        print("Sorry, Please say that again...")
        return""


def wish_user():
    hour = datetime.datetime.now().hour
    
    if hour < 12:
        speak("Good Morning \nI am your Virtual Assistant")
    elif hour <18:
        speak("Good Afternoon \nI am your Virtual Assistant")
    else:
        speak("Good Evening \nI am your Virtual Assistant")
wish_user()


while True:
    command = take_commands()
    if "time" in command:
        time = datetime.datetime.now().strftime("%I:%M:%p")
        speak(f"The time is {time}")
        
    elif "Open Youtube" in command:
        webbrowser.open("https://www.youtube.com")
        
    elif "Open Google" in command:
        webbrowser.open("https://www.google.com")


    elif "Who is" in command:
        person = command.replace("Who is", "")
        info = wikipedia.summary(person, 2)
        print(info)
        speak(info)
    elif "exit" in command:
        speak("Good bye")
        break











