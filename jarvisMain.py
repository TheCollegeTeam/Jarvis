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
"""
################################################## Main function #############################################

if __name__ == "__main__":
    # greet()
    # take_command()
    # city = input("Enter city name :")
    # weather_data("gorakhpur")
    while True:
        # take_command()
        # query = take_command().lower()
        
        query = input("Enter query :").lower()
        query = query.replace(":"," ")
        query = query.replace(".","")
        print(query)

        # if 'wikipedia' in query :
        #     speak('searching wikipedia.....')
        #     query = query.replace("wikipedia","")
        #     results = wikipedia.summary(query, sentence=2)
        #     speak(results)

        if 'greet me' in query:
            greet()

        elif 'subtract' in query :
            subtract_num(query)

        elif 'set alarm' in query and 'am' in query:
            t1 = Thread(target=am,args=(query,))
            t1.start()
            t1.join()

        elif 'set alarm' in query and 'pm' in query:
            # pm(query)
            t2 = Thread(target=pm,args=(query,))
            t2.start()
            t2.join()

        elif 'set alarm' in query:

            t3 = Thread(target=set_alarm_24_hour_clock,args=(query,))
            t3.start()
            t3.join()
            # print("execution done")
            # set_alarm_24_hour_clock(query)

        elif 'multiply' in query :
            multiply_num(query)
        
        elif 'add' in query :
            add_num(query)
        
        elif 'devide' in query :
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

        elif 'news' in query:
            news()

        elif 'current time' in query or 'time' in query:
            current_time()
            
        elif 'youtube' in query:
            speak("opening Youtube")
            webbrowser.open("youtube.com")

        elif 'battery percentage' in query :
            batteryPercantage()

        elif 'who are you' in query:
            whoareyou()

        elif 'weather' in query:
            weather_data()

        elif 'internet speed' in query:
            speedTest()

        elif 'take a screenshot' in query or 'screenshot' in query:
            screenshot()    

        elif 'operating system' in query or 'os' in query:
            osName()

        elif 'current date' in query or 'today\'s date ' in query or 'date' in query:
            currentDate()

        elif 'current day' in query or 'today\'s day ' in query or 'day' in query:
            currentDay()    
        
        elif 'open' in query:
            open_website(query)

        elif 'exit' in query :
            quit()

        else:
            speak("wrong choice")