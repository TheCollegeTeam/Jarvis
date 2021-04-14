import pyttsx3
import speech_recognition as sr


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
        r.energy_threshold = 7000
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio)
        # print(f"user said : {query}\n")

    except Exception as e:
        print(e)
        speak("Say that again please....")
        return "none"
    return query


def binaryCalculator():
    try:
        query = take_command().lower()
        print(query)
        query = query.split()
        print(query)
        if query[1] == 'plus' or query[1] == '+' or query[1] == 'sum':
            result = int(query[0]) + int(query[2])


        elif query[1] == 'subtract' or query[1] == 'minus' or query[1] == '-':
            result = int(query[0]) - int(query[2])


        elif query[1] == 'into' or query[1] == 'multiply' or query[1] == '*' or query[1] == 'multiply by':
            result = int(query[0]) * int(query[2])


        elif query[1] == 'divieded' or query[1] == 'by':
            result = int(query[0]) // int(query[2])

        elif query[1] == 'module' or query[1] == 'remainder' or query[1] == '%':
            result = int(query[0]) % int(query[2])

        else:
            print("Wrong input sir")

        return result

    except Exception as e:
        print("Please speak in 3 plus 4 formate  ")


if __name__ == '__main__':
    while True:

        result = binaryCalculator()
        speak(result)
        print(result)
