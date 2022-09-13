try:
    import pyautogui
    from corefunction.textToSpeech import speak
    from corefunction.speechToText import take_command
    import time
    
except Exception as e:
    print(e)

def copy():
    try:
        time.sleep(2)
        pyautogui.hotkey('ctrl','c')
        speak("text copied")
    except Exception as e:
        print("Print exception")

def paste():
    try:
        pyautogui.hotkey('ctrl','v')
        speak("pasted here")
    except Exception as e:
        print(e)

def selectAll():
    try:
        pyautogui.hotkey('ctrl','a')
        speak("selecting all")
    except Exception as e:
        print(e)

def undo():
    try:
        pyautogui.hotkey('ctrl','z')
    except Exception as e:
        print(e)

def cut():
    try:
        pyautogui.hotkey('ctrl','x')
        speak("text cut from here")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    while True:
        choice = int(input("Enter your choice :"))
        if choice == 1:
            copy()
        elif choice ==2:
            paste()
        elif choice == 3:
            cut()
        else:
            pass