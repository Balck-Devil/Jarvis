import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
# print(voices[1].id)
engine.setProperty("voice",voices[1].id)
# engine.say("Good Morning ! how are you")
engine.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<16:
        speak("Goof Afternoon")
    
    else :
        speak("Good Evening")

    speak("I am Sahil ! Sir Please tell me how may i help you ?")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio=r.listen(source)

    try :
        print("Recognizing...")
        query=r.recognize_google(audio,language="en-in")
        print(f"User Said :- {query}\n")
    
    except Exception as e:
        print("Say That Again Please...")
        return "None"

    return query

def sendEmail(to,content):
    server=smtplib.SMTP("smpt.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("sahilkhirsariya130@gmail.com","7043388294")
    server.sendmail("sahilkhirsariya130@gmail.com",to,content)
    server.close()

if __name__== "__main__":
    wishMe()
    while True:
        quary=takeCommand().lower()
        if "wikipedia" in quary:
            speak("Searching Wikipedia....")
            quary=quary.replace("wikipedia","")
            results=wikipedia.summary(quary,sentences=5)
            speak("According To Wikipedia")
            print(results)
            speak(results)
        
        elif "open youtube" in quary:
            webbrowser.open("youtube.com")

        elif "open " in quary:
            webbrowser.open("google.com")

        elif "open stackoverflow" in quary:
            webbrowser.open("stackoverflow.com")

        elif "play music" in quary:
            music_dir=r"E:\SONGS\Favourite"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif "the time" in quary:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"The Time Is {strTime}")

        elif "open code" in quary:
            codePath=r"C:\Users\admin\ AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(codePath)

        elif "email to sahil" in quary:
            try:
                speak("What Should I Say ?")
                content=takeCommand()
                to="sahilpatel1300@gmail.com"
                sendEmail(to,content)
                speak("Emial has been sent")
            except Exception as e:
                print(e)

        elif "quit" in quary:
            speak("ok bye ! have a good day !!! Take Care")
            exit()
        