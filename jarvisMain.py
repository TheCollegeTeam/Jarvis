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

        elif 'what task' in query or 'features' in query or 'feature' in query:
            features()

        else:
            speak("wrong choice")