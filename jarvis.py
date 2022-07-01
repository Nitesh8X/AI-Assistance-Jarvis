import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import psutil
import pyjokes
import os
import random
import json
import requests
from urllib.request import urlopen
import wolframalpha
import time
import smtplib
import pyautogui
import winshell
# import strfTime



engine = pyttsx3.init()
wolframalpha_app_id = 'wolfram alpha id will go here'

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time=datetime.datetime.now().strftime("%H:%M:%S") #for 12 hours use I instead of H
    speak("The current time is")
    speak(Time)

def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().date
    speak("The Current Date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome Back Nitesh!")
    time_()
    date_()

    hour = datetime.datetime.now().hour

    if hour >= 6 and hour < 12:
        speak("Good Morning Sir!")
    if hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")
    if hour >= 18 and hour < 24:
        speak("Good Evening Sir!")
    

    speak("Jarvis at your service. Please tell me how can I help you today?")

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-US')
        print(query)

    except Exception as e:
        print("Say that again please")

def sendEmail(to,content):
    server = smtplib.SMIP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    #to work this function properly we need to enable low security in gmail which we are going to use as sender

    server.login('username@gmail.com','password')
    server.sendEmail('username@gmail.com',to,content)
    server.close()

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is a'+usage)
    battery = psutil.sensors_battery()
    speak(battery.percent)

def screenshot():
    img = pyautogui.screenshot()
    img.save('C:/Users/gupta/Desktop/screenshot.png')

def joke():
    speak(pyjokes.get_joke())

def introduction():
    speak("I am JARVIS ,Your Personal AI assistant , "
    "I am created by Nitesh , "
    "I can help you in various regards , "
    "I can search for you on the Internet , "
    "I can also grab definitions for you from wikipedia , "
    "In layman terms , I can try to make your life a bed of roses , "
    "Where you just have to command me , and I will do it for you , ")

def creator():
    speak("Nitesh is an extra-ordinary person ,"
    "He has a passion for Artificial Intelligence and Machine Learning")



if __name__ == "__main__":
    wishme()
    while True:
        query = TakeCommand().lower()
        if query is None:
            print("System Offline!")

        if 'time' in query :
            time_()
        elif 'date' in query:
            date_()
        if 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia",'')
            result = wikipedia.summary(query,sentances=3)
            speak('According to wikipedia')
            print(result)
            speak(result)

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content=TakeCommand()
                # reciever = 'reciever_is_me@gmail.com'
                speak("Who is the Reciever?")
                reciever = input("Enter Reciever's Email Address: ")
                to = reciever
                sendEmail(to,content)
                speak(content)
                speak('Email has been Sent!')

            except Exception as e:
                print(e)
                speak("Unable to Send Email!")

        elif 'search in chrome' in query:
            speak('What to search?')
            chromepath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe' 

            search = TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')  #only opens websites that ends with .com

        elif 'search in youtube' in query:
            speak('Waht to search?')
            search_Term = TakeCommand().lower()
            speak("Here we go to Youtube!")
            wb.open('https://www.youtube.com/results?search_query='+search_Term)

        elif 'search in google' in query:
            speak("What to search?")
            search_Term = TakeCommand().lower()
            speak("Searching...")
            wb.open('https://www.google.com/search?q='+search_Term)

        elif 'cpu' and 'CPU' in query:
            cpu()

        elif 'joke' in query:
            joke()

        elif 'go offline' in query:
            speak("Going offline Sir!")
            quit()

        elif 'tell me about yourself' and 'who are you' in query:
            introduction()
        elif 'tell me about Nitesh' and 'creator' in query:
            creator()

        elif 'open word' in query:
            speak("Opening Microsoft Word...")
            ms_word = r'C:\Program Files (x86)\Microsoft Office\root\Office16\WORDICON.EXE'
            os.startfile(ms_word)

        elif 'write a note' in query:
            speak("What should I write, Sir?")
            notes = TakeCommand()
            file.open('notes.txt','w')
            speak("Sir, Should I add Current Date and Time too?")
            ans = TakeCommand().lower()
            if 'yes' in ans or 'sure' in ans:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(time.strptime)
                file.write(':-')
                file.write(notes)
                speak("Done Taking Notes, Sir!")
            else:
                file.write(notes)

        elif 'show notes' in query:
            speak("Showing Notes")
            file = open('notes.txt','r')
            print(file.read())
            speak(file.read())

        elif 'screenshot' in query:
            screenshot()

        elif 'play music' in query:
            songs_dir = 'D:/SONGS'
            music = os.listdir(songs_dir)
            speak('What should I play?')
            speak('Select a number...')
            ans = TakeCommand().lower()
            while('number' not in ans and ans !='random' and ans != 'you choose'):
                speak("I could not understand you, Please Try Again...")
                ans = TakeCommand().lower()
            if 'number' in ans:
                no = int(ans.replace('number',''))
            elif 'random' or 'you choose' in ans:
                no = random.randint(1,100)
            os.startfile(os.path.join(songs_dir,music[no]))

        elif 'remember that' in query:
            speak("What should I remeber?")
            memory = TakeCommand()
            speak("You asked me to remeber that"+memory)
            remember = open('memory.txt','w')
            remember.write(memory)
            remember.close()

        elif 'do you remember anything' in query:
            remember = open('memory.txt','r')
            speak('You asked me to remeber that'+remember.read())

        elif 'where is' in query:
            query = query.replace("where is","")
            location = query
            speak("User asked to locate"+location)
            wb.open_new_tab("https://www.google.com/maps/place/"+location)

        elif 'news' in query:
            try:
                jsonObj = urlopen("https://newsapi.org/v2/everything?q=tesla&from=2021-03-22&sortBy=publishedAt&apiKey=a0f83c81a59d4db1a51442777856421b")
                data = json.load(jsonObj)
                i = 1

                speak("here are some top headlines from buisness")
                print("=========TOP HEADLINES======="+'\n')
                for item in data['articles']:
                    print(str(i)+'. '+item['title']+'\n')
                    print(item['description']+'\n')
                    speak(item['title'])
                    i += 1

            except Exception as e:
                print(str(e))
        elif 'calculate' in query:
            client = wolframalpha.client(wolframalpha_app_id)
            indx = query.lower().split().index('calculate')
            res = client.query(''.join(query))
            answer = next(res.results).text
            print("The answer is: "+answer)
            speak("The answer is: "+answer)

        elif 'what is' in query or 'who is' in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            res = client.query(query)

            try:
                print(next(res.result).text)
                speak(next(res.result).text)
            
            except StopIteration:
                print("No Result Found!")

        elif "don't listen" in query or "stop listening" in query:
            speak("for how many seconds you want me to stop listening commands")
            a = int(TakeCommand())
            time.sleep(a)
            print(a)

        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about, may be you should give me some time")
            
        elif "i love you" in query:
            speak("It's hard to understand, I am still trying to figure this out.")

        elif "weather" in query: 
            api_key = "open weather api"
            base_url = "http://api.openweathermap.org/data /2.5/weather?q="
            speak(" City name ")
            print("City name : ")
            city_name = TakeCommand()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url)
            x = response.json()            
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
            else:
                speak(" City Not Found ") 

        elif 'what is love' and 'tell me about love' in query:
            speak("It is 7th sense that destroy all other senses , "
            "And I think it is just a mere illusion , "
            "It is waste of time")

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled") 

        

        elif 'log out' in query:
            os.system("Shutdown -l")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif 'shutdown' in query:
            os.systrm("shutdown /s /t i")

        
