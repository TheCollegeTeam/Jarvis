try:
    import pyttsx3
    from datetime import *
    # this module detect human voice and converts it into text form.
    import speech_recognition as sr
    # this module is use to request on server.
    import requests
    # This module use to fetch data from wikipedia
    import wikipedia
    # This module is use to open web browser
    import webbrowser
    # This module is use to work on system os
    import os
    import time
    import calculator
    # This module is used for Test internet speed
    import speedtest   #pip install speedtest-cli
    # This module tells us that which os we are using basically it tells all the information about our os
    import platform
    # This module is use to automate tasks
    import pyautogui
    import psutil
    import pyjokes
    from googlesearch import search
    import tkinter as tk
    from PIL import Image, ImageTk
except Exception as e:
    print(e)
############################################ Weather API #########################################################

# newsUrl = 'http://newsapi.org/v2/top-headlines?country=in&apiKey=9f17ea0361774831bb8906e2426c1e22'
api_address = "http://api.openweathermap.org/data/2.5/weather?appid=40b98f754f6b23dc8725fd2cfc6d9769&q="

def currentDay ():
    """
    This function tells current day.
    """
    try:
        today = date.today().strftime("%A")
        speak(f"Today's date is : {today}")
    except Exception as e:
        print(e)
    
def currentDate():
    """
    This function tells current date.
    """
    try:
        date1 = date.today()
        speak(date1)
    except Exception as e:
        print(e)

def jokes():
    """
    This function tells joke 
    using pyjoke module.
    """
    try:
        My_joke = pyjokes.get_joke(language="en", category="all")  
        speak(My_joke)
        query=take_command().lower()
        if "haha " in query or "good one" in query:
            speak("thanks sir should i tell you one more joke")
            query = take_command().lower()
            if "yeah" in query:
                jokes()
            else :
                return  
    except Exception as e:
        print(e)

def batteryPercantage():
    """
    This function uses psutil
    module to get battery percantage
    """
    try:
        battery = psutil.sensors_battery()
        if battery.percent == 100:
            speak("battery is fully charged")
        else:
            speak(f"battery is {battery.percent} percent charge") 
        if battery.power_plugged == 'true':
            speak("battery is charging")
        else:
            speak("battery is not charging")          
    except Exception as e:
        print(e)

def fullSystemDetail():
    pass

def osName ():
    """
    This function tells that which 
    operating system  we are using now.
    """
    try:
        os = platform.system()
        speak(f"you are using {os} operating system")
    except Exception as e:
        print(e)

def screenshot():
    """
    This function takes a screenshot
    using pyautogui and save it in 
    screenshot directory.
    """
    try:

        isdir = os.path.isdir("screenshot")
        if isdir==True:
            myScreenshot = pyautogui.screenshot()
            speak("taking screenshot")
            lst = os.listdir('screenshot')
            lstLength = int(len(lst))
            path = f"screenshot\\screenshot{lstLength+1}.png"
            myScreenshot.save(path)
            speak("Screenshot taken")
        else :
            os.mkdir("screenshot")
            screenshot()
    except Exception as e:
        print(e)
        speak("Can not take screenshot")

def speedTest():
    """
    This function used to fetch
    the internet speed.
    """
    try:
        speak("ok sir trying to fetch download speed")
        st = speedtest.Speedtest()
        downloadSpeed = st.download()
        downloadSpeed = downloadSpeed/1048576   #for converting bytes in Kbytes we have to divied by 1024 and then To convert from Kbyte to Mbyte we have to divide by 1024 then we can multiply 1024*1024 = 1048576  
        downloadSpeed = "{:.2f}".format(downloadSpeed)
        speak(f"{downloadSpeed} Megabyte per second")
    except Exception as e:
        print(e)

def current_time ():
    """
    This function tells the 
    current time using datetime module.
    """
    try:
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        speak(f"The time is {current_time}")
    except Exception as e:
        print(e)

def news():
    """
    This function use news api and fetch 
    10 latest news and speak news.
    """
    try:
        newsUrl = 'http://newsapi.org/v2/top-headlines?country=in&apiKey=9f17ea0361774831bb8906e2426c1e22'
        json_data = requests.get(newsUrl).json()
        for i in range(0, 10):
            title = json_data['articles'][i]['title']
            description = json_data['articles'][i]['description']
            print(f"{i + 1} :-{title}")
            speak(title)
            print(f"        {description}")
            speak(description)
    except Exception as e:
        print(e)

def weather_data():
    """
        This function use a API. This function send request to open weather site
        fetch data from that site a speak.
    """
    try:
        url = api_address + "gorakhpur"  # in url we add a place address to get particular location weather data

        json_data = requests.get(url).json()

        weather_data = json_data['weather'][0]['main']
        temp_data = json_data['main']['temp']
        temp_data = int(temp_data - 273.15)
        # formatted_data = weather_data + temp_data
        # print(json_data)
        speak(f"Hello sir the weather is {weather_data} and the temerature is {temp_data} degree celsius")
    except Exception as e:
        print(e)
################################################### Greet Function #############################################
def greet():
    """
    This Function used for greeting

    """
    try:
        hour = int(datetime.now().hour)
        today = date.today()
        curr_day = today.strftime("%B %d , %Y")
        now = datetime.now()
        curr_time = now.strftime("%H %M")

        if hour >= 3 and hour <= 11:
            speak(f"Hello sir good morning  It's {curr_day} and the time is {curr_time}")
            weather_data()


        elif hour >= 12 and hour <= 18:
            speak("Hello Good After noon ")


        elif hour > 18 and hour <= 24:
            speak("Hello Good evening ")


        else:
            speak("Hello Good night")
    except Exception as e:
        print(e)

################################################ Speak Function ###############################################
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

############################################### Take Command ##################################################
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

######################################### Who are You ######################################################
def whoareyou():
    """
    This function tells about that who is this 
    """
    try:
        speak("Hello sir")
        time.sleep(1)
        speak("i am edith your personal assistant")
        speak("would you like to know what can i do")
        query = take_command.lower()
        if 'yes' in query or 'yeah' in query or 'sure' in query:
            features()
    except Exception as e:
        print(e)

def shutdown():
    """
    First this function check os name using platform
    module and then shutdown the system.
    """
    try:
        os = platform.system()
        os = os.lower()
        if os =='windows':
            os.system("shutdown /s")
        elif os =='linux':
            os.system()
        elif os =='macos':
            os.system()
        else:
            speak("Sorry but it can only used in windows , linux , macos")
    except Exception as e:
        print(e)

def restart():
    """
    This function works as shutdown function
    first it checks os name and then restart
    the system.
    """
    try:
        os = platform.system()

        os = os.lower()
        
        if os =='windows':
            os.system("shutdown/r")
        elif os =='linux':
            os.system()
        elif os =='macos':
            os.system()
        else:
            speak("Sorry but it can only used in windows , linux , macos")
    except Exception as e:
        print(e)

def open_website(query):
    """
    This function open any website this 
    function uses search function which is 
    in the google search module.
    """
    try:
        for j in search(query, tld="co.in", num=1, stop=1, pause=2):
            webbrowser.open(j)
    except Exception as e:
        print(e)

def features():
    try:
        speak("hello sir, i can perform many tasks such as calculating numbers or opening a website for you i can play music for you")
        speak("I can automate some task for you ")
    except Exception as e:
        print(e)

def makeAnote():
    try:
        if os.path.isdir("notes"):
            lst = os.listdir("notes")
            lstLength = int(len(lst))
            file_path = f"notes\\note{lstLength+1}.txt"
            with open (file_path,"a") as file:
                def write_note():
                    speak("Okk sir tell me what to write")
                    # query = input("Enter query :")
                    query = take_command()
                    file.write(query)
                    # print("Want to add more sir :")
                    speak("Want to add more sir :")
                    # query = input("More ??")
                    query = take_command()
                    if query in ['yes','yeah','hmm','sure']:
                        write_note()
                    else:
                        print("Done sir")
                        speak("saving note sir")
                write_note()
        else:
            os.makedirs("notes")
            makeAnote()
    except Exception as e:
        print(e)

def myBirthday():
    try:
        root = tk.Tk()
        image1 = Image.open("resources\\images\\birthdayImg.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tk.Label(image=test)
        label1.pack()
        root.after(10000,lambda:root.destroy())
        root.mainloop()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    pass