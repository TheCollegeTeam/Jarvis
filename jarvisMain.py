from home import *
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
"""
################################################## Main function #############################################

if __name__ == "__main__":
    # greet()
    # take_command()
    # city = input("Enter city name :")
    # weather_data("gorakhpur")
    while True:
        # take_command()
        query = take_command().lower()
        print(query)

        # if 'wikipedia' in query :
        #     speak('searching wikipedia.....')
        #     query = query.replace("wikipedia","")
        #     results = wikipedia.summary(query, sentence=2)
        #     speak(results)

        if 'google' in query:
            # chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            # webbrowser.get("google-chrome")
            # webbrowser.open("google.com")
            webbrowser.open_new_tab("google.com")

        elif 'calculate' in query :

            while True:
                mathOperation()

        elif 'chrome' in query:
            # codepath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            # os.startfile(codepath)
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        # elif 'open web browser' in query :

        elif 'news' in query:
            news()

        elif 'current time' in query or 'time' in query:
            time()
            
        elif 'youtube' in query:
            speak("opening Youtube")
            webbrowser.open("youtube.com")
            

        elif 'who are you' in query:
            whoareyou()


        elif 'weather' in query:
            weather_data()

        elif 'internet speed' in query:
            speedTest()

        elif 'take a screenshot' in query or 'screenshot' in query:
            screenshot()    

        elif 'operating system' in query:
            osName()

        elif 'exit' in query:
            quit()

        else:
            speak("wrong choice")