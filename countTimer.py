import time
import threading
import tkinter as tk
from tkinter import Label, Button
# from corefunction.speechToText import take_command
import playsound


def getTime(query):
    print("Entering in getTime function")
    query = query.split()
    numList = []
    for nums in query:
        if nums.isdigit():
            numList.append(int(nums))
    if isContain(query,["second","sec","seconds"]):
        totalTime = numList[0]
    elif 'minute' in query:
        totalTime = (numList[0]*60)
    elif 'minute' and 'second' in query:
        totalTime = (numList[0]*60 + numList[1])
    elif 'hour' and 'minute' and 'second' in query:
        totalTime = (numList[0]*60*60 + numList[1]*60 + numList[2])
    else:
        return
    print("timer started")
    time.sleep(totalTime)
    threading.Thread(target=timer).start()
    playsound.playsound("resources\\audio\\Countdown timer.mp3")

def timer():
    root = tk.Tk()
    root.geometry("200x200")
    root.resizable(False,False)
    root.title("Timer")
    timerLable = Label(root,text="Time's up",font=("Arial",20,"bold"),fg="black")
    timerLable.pack(pady=20)
    okButton = Button(root, text="  OK  ", font=("Arial", 15), relief=tk.FLAT, bg='#14A769', fg='white', command=lambda:quit())
    okButton.pack()
    root.mainloop()

if __name__ == '__main__':
    query = input("Enter query :")
    # query = take_command().lower()
    getTime(query)
    # t1 = threading.Thread(target=getTime, args=(query,))
    # t1.start()
