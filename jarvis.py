import speech_recognition as s
import datetime
import pyttsx3
import wikipedia
import webbrowser
import os
import smtplib
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>>0 and hour<12:
        speak("GOOD MORNING GARVIT.WELCOME TO YOUR LAPTOP.")
    elif hour>>12 and hour<18:
        speak("GOOD AFTERNOON GARVIT.WELCOME TO YOUR LAPTOP.")
    else:
        speak("GOOD EVENING GARVIT.WELCOME TO YOUR LAPTOP.")
    speak("I AM JARVIS SIR. PLEASE TELL ME HOW MAY I HELP YOU")

def tc():
    r=s.Recognizer()
    with s.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        r.energy_threshold=100
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return"None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('garvit0221@gmail.com','Garvit57@')
    server.sendmail('garvit0221@gmail.com',to,content)
    server.close()

if __name__=="__main__":
    wish()
    while True:
        query=tc().lower()
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=3)
            speak("According to wikipedia...")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'play music' in query:
            music='wulumulu.m4a'
            songs=os.listdir(music)
            os.startfile(os.path.join(music,songs[0]))
        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"SIR,THE TIME IS{strTime}")
        elif 'email to mother' in query:
            try:
                speak("WHAT MESSAGE SHOULD I SEND?")
                content=tc()
                to="gpankaj0221@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print (e)
                speak("Sorry.I AM NOT ABLE TO SEND THIS EMAIL.")
        elif 'open chrome' in query:
            url="C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(url)
        elif 'exit jarvis' in query:
            break