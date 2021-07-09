import pyttsx3
def speak(audio):
    """
    This function convert text to 
    speech using pyttsx3 module.
    """
    try:
        engine = pyttsx3.init()
        # engine.setProperty()
        engine.say(audio)
        engine.runAndWait()
    except Exception as e:
        print(e)