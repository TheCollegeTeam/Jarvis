import speech_recognition as sr
from corefunction.textToSpeech import speak

def take_command():
    """
    take command takes human voice as input
    and then convert it into text to perform
    operation using speech recognition.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 2
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