import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia 
import smtplib
from smtplib import SMTPException
import webbrowser as wb
import os

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    speak("The Current time is ")
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back sir!")
    hour = datetime.datetime.now().hour
    if hour >=6 and hour <= 12:
        speak("Good Morning")
    elif hour >=12 and hour <= 18:
        speak("Good Afternoon")
    elif hour >=18 and hour <= 24:
        speak("Good Evening")
    else:
        speak("Good Night")
        
    speak("Friday at your service. How can I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        # print(query)
    except Exception as e:
        print(e)
        speak("Sorry! Please say again!")

        # return "None"
               #Removing this may help to make it unlimited but beware
    return query

# speak("Hello Welcome to AI Talks. Start speaking after 1 second.")
# speak(takeCommand())

def sendmail(to,content):
    server = smtplib.SMTP_SSL(smtp.gmail.com,587)
    server.ehlo()
    server.starttls()
    server.login("laughingmagic007@gmail.com","grejojoby123")
    server.sendmail("laughingmagic007@gmail.com",to,content)
    server.close()

if __name__ == "__main__":
    wishme()

    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "wikipedia" in query:
            speak("searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            speak(result)
        elif "send mail" in query:
            try:
                speak("What should i say?")
                content=takeCommand()
                to = "grejo00@gmail.com"
                sendmail(to,content)
                speak("The mail was sent successfully")
            except smtplib.SMTPException:
                print("Error")
            except Exception as e:
                print(e)
                speak("Enable to send email")
        elif "search in chrome" in query:
            speak("What should i search..?")
            chromepath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search)
        elif "log out" in query:
            speak("Logging off...")
            os.system("shutdown -l")
        elif "shut down" in query:
            speak("Shutting down...")
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            speak("Restarting...")
            os.system("shutdown /r /t 1")
        elif "" in query:
            

        elif "offline" in query:
            quit()
        
        