import pyttsx3
import pyjokes
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import time
import cv2
import random
from requests import get as ag
import pywhatkit as kit
import sys

import pyaudio
engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voices",voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wish_me():
    hour=int(datetime.datetime.now().hour)
    if hour >=4 and hour <11:
        speak("good morning sir, !")
    elif hour>=11 and hour <16:
        speak("good afternoon Sir,")
    elif hour >=16 and hour<21:
        speak("good evening sir, ")
    else:
        speak("")
f="xxxxxxx"
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1

        audio=r.listen(source)
    try:
        print("recognizing...")
        query=r.recognize_google(audio,language="en-in")
        print(f"user said: {query}\n")
    except Exception as e:
        speak("please speak again")
        return "None"
    return query
e=f
a=e
def sendemail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("shubhsharma3108@gmail.com",a)
    server.sendmail("shubhsharma3108@gmail.com",to,content)
    server.close()
def Youtubesongs():
    speak("opening")
    ab="https://www.youtube.com/watch?v=4NRXx6U8ABQ"
    ac="https://www.youtube.com/watch?v=50VNCymT-Cs"
    ad="https://www.youtube.com/watch?v=r7qovpFAGrQ"
    ae="https://www.youtube.com/watch?v=zNrKoWG7Cj0"
    af="https://www.youtube.com/watch?v=CYDP_8UTAus"
    ah="https://www.youtube.com/watch?v=_70Q-Xj3rEo"
    ai="https://www.youtube.com/watch?v=Z6L4u2i97Rw"
    aj="https://www.youtube.com/watch?v=kXptPzKNMq4"
    ak="https://www.youtube.com/watch?v=Tc-XxqEyolU"
    al="https://www.youtube.com/watch?v=YKqDiNJJPXk"
    am="https://www.youtube.com/watch?v=XbGs_qK2PQA"
    an="https://www.youtube.com/watch?v=8CdcCD5V-d8"
    ao="https://www.youtube.com/watch?v=ApXoWvfEYVU"
    ap="https://www.youtube.com/watch?v=m7Bc3pLyij0"
    aq="https://www.youtube.com/watch?v=op4B9sNGi0k"
    ar="https://www.youtube.com/watch?v=_dJn2BnGBM4"
    av="https://www.youtube.com/watch?v=YqeW9_5kURI"
    at="https://www.youtube.com/watch?v=Bznxx12Ptl0"
    au="https://www.youtube.com/watch?v=ft4jcPSLJfY"

    list=[ab,ac,ad,ae,af,ah,ai,aj,ak,al,am,an,ao,ap,aq,ar,av,at,au]

    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(random.choice(list))

if __name__=="__main__":


    hello=True
    while hello:

        query= takecommand().lower()
        if "wikipedia" in query:
            speak("serching wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=3 )
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif"open youtube" in query:
            speak("opening")
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open("https://youtube.com")
        elif "exit"in query or " quit" in query :
            hello=False
        elif  "the time" in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time now is {strtime}")
        elif "open chess" in query:
            speak("opening")
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open("https://chess.com")
        elif "open chess.com" in query:
            speak("opening")
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open("https://chess.com")
        elif "about yourself" in query:
            speak("I am david your personal assistant")
            speak("i was designed by shubh sir on 3rd of  december")
        elif "open facebook" in query:
            speak("opening")
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open("https://www.facebook.com/")
        elif "open instagram" in query:
            speak("opening")
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open("https://www.instagram.com/")
        elif "open whatsapp" in query:
            speak("opening")
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open("https://web.whatsapp.com/")
        elif "open sublime text" in query:
            speak("opening")
            sublimepath="C:\Program Files (x86)\Sublime Text 3\sublime_text.exe"
            os.startfile(sublimepath)
        elif "send email" in query:
            try:
                speak("what should i mail sir")
                content=takecommand()
                to="shubhsharma3108@gmail.com"
                sendemail(to,content)
                speak("email has been sent")
            except Exception as e:
                speak("sorry sir email wasn't sent ")
        elif "cricket score" in query:
            speak("opening sir")
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open("https://www.google.com/search?q=cricket+score&rlz=1C1NDCM_enIN863IN863&sxsrf=ALeKk00gH8BDLErwzoDkUfMrY1JAoyqcfw:1607073645869&source=lnms&sa=X&ved=0ahUKEwiMi6ju_7PtAhWcwzgGHcO6D3sQ_AUIDigA&biw=1280&bih=578&dpr=1.5")
        elif "tell me the date" in query:
            year=int(datetime.datetime.now().year)
            month = int(datetime.datetime.now().month)
            day= int(datetime.datetime.now().day)
            speak(day)
            speak(month)
            speak(year)
        elif "open notepad" in query:
            notepath="C:\\Windows\\system32\\notepad.exe"
            os.startfile(notepath)
        elif "open command prompt" in query:
            os.system("start cmd")
        elif "open camera" in query:
            cap=cv2.VideoCapture(0)
            while True:
                ret, img= cap.read()
                cv2.imshow("webcam",img)
                k=cv2.waitKey(50)
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()
        elif "music on my laptop" in query:
            music_dir="C:\\Music"
            song=os.listdir(music_dir)
            a = random.choice(song)
            os.startfile(os.path.join(music_dir,a))
        elif "ip address" in query:
            ip=ag("https://api.ipify.org").text
            speak(f"your Ip address is {ip}")
            print(ip)
        elif"play a song on youtube" in query:
            Youtubesongs()
        elif "play song on youtube" in query:
            Youtubesongs()
        elif"the temprature" in query:
            pass
        elif "send message" in query:
            kit.sendwhatmsg("+916377002845","hello i am sleepy",13,31)
            speak("message has been sent sir")
        elif "quit programme" in query:
            speak("thank you for using me sir,have a good day")
            sys.exit()
        elif "close notepad" in query:
            speak("oky sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")
        elif"tell me a joke" in query:
            joke=pyjokes.get_joke()
            speak(joke)
            
