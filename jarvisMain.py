
try:
    import os
    from home import *
    from calculator import *
    from conversion import Celsius_to_fahrenhite
    from conversion import fahrenhite_to_Celsius
    # from alarm import *
    from threading import Thread
    from alarm.countTimer import getTime
    from wishing.birthdayWishing import myBirthday
    from threading import Thread
    from corefunction.wordContain import isContain
    from appData import openApp,setting_page
    from keyboardAutomation import keyboradAutomation
    from corefunction.speechToText import speak
    from login_page import create_login_window,auto_login
except Exception as e:
    print(e)
=======
from home import *
from calculator import *
from conversion import *
from alarm import *
from threading import Thread

"""
greet
calculate
news
current time
who are you
weather
internet speed
screenshot
operating system
shutdown
restart
battery percentage
joke
today's date
today's day
setting alarm
convert temeperature
make a note
copy,paste,select all
undo,cut
set timer
"""
################################################## Main function #############################################

if __name__ == "__main__":
    # greet()
    # take_command()
    # city = input("Enter city name :")
    # weather_data("gorakhpur")
    path = "userDetails"
    if os.path.isdir(path)==False:
        create_login_window()
    else:
        auto_login()

    while True:
        # take_command()
        query = take_command().lower()
        
        # query = input("Enter query :").lower()
        # query = query.replace(":"," ")
        # query = query.replace(".","")
        print(query)
        if 'wikipedia' in query :
            speak('searching wikipedia.....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentence=2)
            speak(results)

        elif isContain(query,["greet","wish","good morning","good afternoon","good evening","good night"]):
=======

        elif 'greet me' in query or 'wish me' in query:

            greet()

        elif isContain(query,["joke","jokes","make me laugh","laugh"]):
            jokes()

        elif isContain(query,["who i am","who am i","about me","about user","user detail"]):
            whoAmI()

        elif isContain(query,["copy","paste","select all","cut","undo","move"]):
            keyboradAutomation(query)

        elif 'my birthday' in query:
            myBirthday()

        elif isContain(query,["exit","bye","goodbye","sleep"]) :
            bye()
        
        elif isContain(query,["timer"]):
            print("enterd in timer")
            t1 = Thread(target=getTime,args=(query,))
            t1.start()

        elif 'open' in query and 'setting' in query:
            setting_page()

        elif 'open' in query:
            openApp(query)
=======
        if 'greet me' in query or 'wish me' in query:
            greet()

        elif 'exit' in query or 'bye' in query or 'goodbye' in query :
            quit()

        elif 'set alarm' in query and 'am' in query:
            t1 = Thread(target=am,args=(query,))
            t1.start()
            t1.join()

        elif 'set alarm' in query and 'pm' in query:

            t2 = Thread(target=pm,args=(query,))
            t2.start()
            t2.join()

        elif 'set alarm' in query:

            t3 = Thread(target=set_alarm_24_hour_clock,args=(query,))
            t3.start()
            t3.join()


        elif 'subtract' in query or 'minus' in query or '-' in query :
            subtract_num(query)

        elif 'multiply' in query or 'into' in query or 'x' in query or 'multiplied' in query :
            multiply_num(query)
        
        elif 'add' in query or 'plus' in query or '+' in query :
            add_num(query)
        
        elif 'devide' in query or 'by' in query or '/' in query:
            devide_num(query)
        
        elif 'reminder' in query :
            reminder(query)

        elif 'square root' in query:
            sqrt(query)
    
        elif 'square' in query :
            squre(query)
        
        elif 'cube root' in query :
            cube_root(query) 
        
        elif 'cube' in query :
            cube(query)
   
        elif 'power' in query :
            power(query)

        elif 'fahrenhite to Celsius' in query:
            fahrenhite_to_Celsius(query)

        elif 'celsius to fahrenheit' in query:
            Celsius_to_fahrenhite(query)  

        elif isContain(query,["news","today's update"]) :
            news()

        elif isContain(query,["current time","time","now time"]):
            current_time()
            
        elif isContain(query,["youtube"]):
            webbrowser.open("youtube.com")

        elif isContain(query,["battery percentage","power level"]) :
            batteryPercantage()

        elif isContain(query,["who are you","about yourself"]):
            whoareyou()

        elif isContain(query,["weather"]):
            weather_data()

        elif isContain(query,['internet speed']):
            speedTest()

        elif isContain(query, ["take a screenshot","screenshot"]):
            screenshot(query)    
        
        elif isContain(query,["operating system","os"]):
            osName()

        elif isContain(query,["current date", "today\'s date","date"]):
            currentDate()

        elif isContain(query,["today's day","current day","day"]):
            currentDay()    
        
        elif isContain(query,["what task","features","feature"]) :
            features()

        elif isContain(query,["make a note","create a note","note","notes","show note"]):
            note(query)

        elif isContain(query,["turn off","switch off","shutdown","shut down"]):
            shutdown()

        elif isContain(query,["restart","reboot"]):
            restart()
=======

        # elif 'open' in query:
        #     open_website(query)

        elif 'what task' in query or 'features' in query or 'feature' in query:
            features()

        elif 'make a note' in query or 'create a note' in query:
            makeAnote()
=======
        elif 'open' in query:
            open_website(query)

        elif 'what task' in query or 'features' in query or 'feature' in query:
            features()



        else:
            speak("wrong choice")