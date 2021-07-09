try:
    import pyautogui
    from corefunction.textToSpeech import speak
    from corefunction.wordContain import isContain
    from corefunction.speechToText import take_command
    import time
    import random
except Exception as e:
    raise ModuleNotFoundError

def copy():
    try:
        time.sleep(3)
        pyautogui.hotkey('ctrl','c')
        replies = ["text copied","okk copying text","done","okk"]
        speak(f"{random.choice(replies)}")
    except Exception as e:
        print("Print exception")

def paste():
    try:
        time.sleep(3)
        pyautogui.hotkey('ctrl','v')
        replies = ["pasted here","pasting here","text pasted","okk","done"]
        speak(f"{random.choice(replies)}")
    except Exception as e:
        print(e)

def selectAll():
    try:
        time.sleep(3)
        pyautogui.hotkey('ctrl','a')
        replies = ["selecting all","selected","done"]
        speak(f"{random.choice(replies)}")
    except Exception as e:
        print(e)

def undo():
    try:
        time.sleep(3)
        pyautogui.hotkey('ctrl','z')
        replies = ["undo","undoing"]
        speak(f"{random.choice(replies)}")
    except Exception as e:
        print(e)

def cut():
    try:
        time.sleep(3)
        pyautogui.hotkey('ctrl','x')
        replies = ["cut it","cut selected ","moving it from here"]
        speak(f"{random.choice(replies)}")
    except Exception as e:
        print(e)

def keyboradAutomation(query):

    if isContain(query,["copy"]):
        copy()

    elif isContain(query,["paste"]):
        paste()

    elif isContain(query,["cut","move"]):
        cut()

    elif isContain(query,["select all"]):
        selectAll()

    elif isContain(query,["undo"]):
        undo()

if __name__ == "__main__":
    while True:
        # choice = take_command()
        choice = int(input("Enter your choice :"))
        if choice == 1:
            copy()
        elif choice ==2:
            paste()
        elif choice == 3:
            cut()
        elif choice == 4:
            undo()
        elif choice == 5:
            selectAll()
        else:
            exit()
