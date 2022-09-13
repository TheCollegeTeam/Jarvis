import speech_recognition as sr
import pyttsx3

def speak(audio):
    engine = pyttsx3.init()
    # engine.setProperty()
    engine.say(audio)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = .5
        r.energy_threshold = 10000
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio)
        print(f"user said : {query}\n")

    except Exception as e:
        print(e)
        speak("Say that again please....")
        return "none"
    return query
