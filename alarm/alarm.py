import datetime
from threading import *
from pygame import mixer
from corefunction.textToSpeech import speak
from corefunction.speechToText import take_command

def playSound():
    """ 
    This function use pygame 
    module to play music.
    """
    try:
        mixer.init()
        mixer.music.load("alarm\\lutGaye.mp3")
        mixer.music.play()
        while True:
            query = take_command().lower()
            if 'stop' in query:
                # Stop the mixer
                mixer.music.stop()
                break
    except Exception as e:
        print(e)

def am(query):
    """
    This fiunction takes am time in input
    """
    try:
        query = query.split()
        list = []
        for words in query:
            if words.isdigit():
                list.append(int(words))

        if len(list) == 1:
            alarmHour = list[0]
            alarmMinute = 0       
            if alarmHour>12:
                print("wrong input") 
            else :
                print(f"Setting alarm at {alarmHour}")
                while True:
                    # this loop continously check the current time and match with alarm time
                    currentTime = datetime.datetime.now()
                    nowHour = int(currentTime.strftime("%H"))
                    nowMinute= int(currentTime.strftime("%M"))
                    if alarmHour==nowHour and alarmMinute == nowMinute:
                        playSound()
                        break
        else:
            print(f"setting alarm at{list[0]}:{list[1]}")
            alarmHour = list[0]
            alarmMinute = list[1]
            if alarmHour>12 or alarmMinute>59:   #this if statement return function again 
                print("wrong input")
            else:
                while True:
                    # this loop continously check the current time and match with alarm time
                    currentTime = datetime.datetime.now()
                    nowHour = int(currentTime.strftime("%H"))
                    nowMinute= int(currentTime.strftime("%M"))
                    if alarmHour==nowHour and alarmMinute == nowMinute:
                        playSound()
                        break
    except Exception as e:
        print(e)

def pm(query):
    try:
        query = query.split()
        list = []
        for words in query:
            if words.isdigit():
                list.append(int(words))

        alarmHour = list[0]  
        if alarmHour == 12:
            pass     
        else:
            alarmHour = alarmHour + 12   
        print(alarmHour)
        if(len(list)) == 1:
            alarmMinute = 0 
            if alarmHour>23:   #this if statement return function again 
                print("Time Hour can't be More than 23 ")
                pm()
            else :
                print(f"Setting alarm at {alarmHour}")
                while True:
                    # this loop continously check the current time and match with alarm time
                    currentTime = datetime.datetime.now()
                    nowHour = int(currentTime.strftime("%H"))
                    nowMinute= int(currentTime.strftime("%M"))
                    if alarmHour==nowHour and alarmMinute == nowMinute:
                        playSound()
                        break
                        
        else:
            print(f"setting alarm at{alarmHour}:{list[1]}")
            alarmMinute = list[1]
            if alarmHour>23 or alarmMinute>59:   #this if statement return function again 
                print("wrong input")
            else:
                while True:
                    # this loop continously check the current time and match with alarm time
                    currentTime = datetime.datetime.now()
                    nowHour = int(currentTime.strftime("%H"))
                    nowMinute= int(currentTime.strftime("%M"))
                    if alarmHour==nowHour and alarmMinute == nowMinute:
                        playSound()
                        break
    except Exception as e:
        print(e)

def set_alarm_24_hour_clock(query):
    try:
        query = query.split()
        list = []
        for words in query:
            if words.isdigit():
                list.append(int(words))
        if(len(list)) == 1:
            alarmHour = list[0]
            alarmMinute = 0
            if alarmHour>12:   #this if statement return function again 
                print("Time Hour can't be More than 24 ")
            else :
                print(f"Setting alarm at {alarmHour}")
                while True:
                    # this loop continously check the current time and match with alarm time
                    currentTime = datetime.datetime.now()
                    nowHour = int(currentTime.strftime("%H"))
                    nowMinute= int(currentTime.strftime("%M"))
                    if alarmHour==nowHour and alarmMinute == nowMinute:
                        playSound()
                        break

        else:
            print(f"setting alarm at{list[0]}:{list[1]}")
            alarmHour = list[0]
            alarmMinute = list[1]
            if alarmHour>23 or alarmMinute>59:   #this if statement return function again 
                print("wrong input")
                
            while True:
                # this loop continously check the current time and match with alarm time
                currentTime = datetime.datetime.now()
                nowHour = int(currentTime.strftime("%H"))
                nowMinute= int(currentTime.strftime("%M"))
                if alarmHour==nowHour and alarmMinute == nowMinute:
                    playSound()
                    break
    except Exception as e:
        print(e)
        
if __name__ == '__main__': 
    
    query = take_command()
    # query = input("<<< :")
    query = query.replace(":"," ")
    query = query.replace(".","")
    print(query)    
    
    if 'set alarm' in query and 'am' in query:
        am(query)

    elif 'set alarm' in query and 'pm' in query:
        pm(query)

    elif 'set alarm' in query:
        set_alarm_24_hour_clock(query)

    else:
        exit()
