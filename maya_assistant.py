#python project
#Maya Assistant.py

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import speedtest
import time
import instaloader
import pyautogui
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning")

    elif hour >= 12 and hour < 18:
        speak("good afternoon")

    else:
        speak("good evening")

    speak("I AM Maya ASSISTANT SIR , PLEASE TELL ME HOW MAY I HELP YOU ")


def takecommand():
    # it takes microphone  input from the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.energy_threshold = 6000
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recongnizer....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said:  {query}\n")

    except Exception as e:
        # print(e)

        print("say that again please...")
        return "None"
    return query


def taskexecution():
    wishme()
    while True:
        query = takecommand().lower()

        # logic for executing task based on query
        if 'wikipedia' in query:
            try:
                speak('searching wikipedia ....')
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=5)
                speak("According to wikipedia")
                print(result)
                speak(result)
                time.sleep(3)
                speak("i am done sir , now i am ready for next work ")
                print("i am done sir , now i am ready for next work ")
            except Exception as e:
                speak("dosen't find anything on wikipedia")
                print("dosen't find anything on wikipedia")

        elif 'open youtube' in query:
            speak("opening youtube")
            print("opening youtube....")
            webbrowser.open("https://youtube.com")
            time.sleep(3)
            speak("i am done sir , now i am ready for next work ")
            print("i am done sir , now i am ready for next work ")

        elif 'open google' in query:
            speak("opening google")
            print("opening google....")
            webbrowser.open("https://google.com")
            time.sleep(3)
            speak("i am done sir , now i am ready for next work ")
            print("i am done sir , now i am ready for next work ")

        elif 'open blogger' in query:
            speak("opening blogger")
            print("opening blogger....")
            webbrowser.open("https://blogger.com")
            time.sleep(3)
            speak("i am done sir , now i am ready for next work ")
            print("i am done sir , now i am ready for next work ")

        elif 'play music' in query or 'play song' in query:
            try:
                speak("playing music")
                print("playing music....")

                music_dir = 'F:\music'
                songs = os.listdir(music_dir)
                n = random.randint(0, len(songs))
                os.startfile(os.path.join(music_dir, songs[n]))
                time.sleep(3)
                speak("i am done sir , now i am ready for next work ")
                print("i am done sir , now i am ready for next work ")

            except Exception as e:
                speak("sorry! i can't find your directory ")

        elif 'thanks maya ' in query or 'thanks' in query:
            speak("your welcome sir")
            print("your welcome sir")

        elif 'i love you maya' in query:
            speak("ooooo baby i love you too")
            print("i love you too")

        elif 'maya i love you' in query or 'i love u' in query:
            speak("ooooo baby i love you too")
            print("i love you too")

        elif 'maya you are so amazing' in query:
            speak("thank you very much sir")
            print("thank you very much sir ")

        elif 'the time' in query or 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strTime}")
            print(strTime)

        elif 'open vs code' in query:
            try:
                speak("opening vs code")
                print("opening vs code....")
                vscodepath = "E:\\Microsoft VS Code\\Code.exe"
                os.startfile(vscodepath)
                time.sleep(3)
                speak("i am done sir , now i am ready for next work ")
                print("i am done sir , now i am ready for next work ")

            except Exception as e:
                speak("dosen't find anything ")
                print("dosen't find anyhing")

        elif 'sleep maya' in query or 'you can sleep' in query:
            print("okay sir i am going to sleep you can call me anytime")
            speak("okay sir i am going to sleep you can call me anytime")
            break;


        elif 'open android studio' in query:
            try:
                speak("opening android studio")
                print("opening android studio....")
                androidstudiopath = "E:\\android studio\\Android Studio\\bin\\studio64.exe"
                os.startfile(androidstudiopath)
                time.sleep(3)
                speak("i am done sir , now i am ready for next work ")
                print("i am done sir , now i am ready for next work ")

            except Exception as e:
                speak("dosen't find anything ")
                print("dosen't find anyhing")

        elif 'open intellij idea' in query:
            try:
                speak("opening intellij idea")
                print("opening intellij idea....")
                intellijideapath = "E:\\java--- phython\\JetBrains\\IntelliJ IDEA Community Edition 2020.2.3\\bin\\idea64.exe"
                os.startfile(intellijideapath)
                time.sleep(3)
                speak("i am done sir , now i am ready for next work ")
                print("i am done sir , now i am ready for next work ")

            except Exception as e:
                speak("dosen't find anything ")
                print("dosen't find anyhing")

        elif 'open pycharm' in query:
            try:
                speak("opening pycharm")
                print("opening pycharm....")
                pycharmpath = "E:\\java--- phython\\JetBrains\\PyCharm Community Edition 2020.1.3\\bin\pycharm64.exe"
                os.startfile(pycharmpath)
                time.sleep(3)
                speak("i am done sir , now i am ready for next work ")
                print("i am done sir , now i am ready for next work ")

            except Exception as e:
                speak("dosen't find anything ")
                print("dosen't find anyhing")

        elif 'open dev c' in query:
            try:
                speak("opening dev c")
                print("opening dev c....")
                devcpath = "C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe"
                os.startfile(devcpath)
                time.sleep(3)
                speak("i am done sir , now i am ready for next work ")
                print("i am done sir , now i am ready for next work ")

            except Exception as e:
                speak("dosen't find anything ")
                print("dosen't find anyhing")

        elif 'open notepad plus plus' in query:
            try:
                speak("opening notepad++")
                print("opening notepad++....")
                notepadpluspluspath = "C:\\Program Files (x86)\\Notepad++\\notepad++.exe"
                os.startfile(notepadpluspluspath)
                time.sleep(3)
                speak("i am done sir , now i am ready for next work ")
                print("i am done sir , now i am ready for next work ")

            except Exception as e:
                speak("dosen't find anything ")
                print("dosen't find anyhing")

        elif 'open notepad' in query:
            try:
                speak("opening notepad")
                print("opening notepad....")
                notepadpath = "%windir%\\system32\\notepad.exe"
                os.startfile(notepadpath)
                time.sleep(3)
                speak("i am done sir , now i am ready for next work ")
                print("i am done sir , now i am ready for next work ")

            except Exception as e:
                speak("dosen't find anything ")
                print("dosen't find anyhing")

        elif 'open Chrome' in query:
            try:
                speak("opening chrome")
                print("opening chrome....")
                chromepath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(chromepath)
                time.sleep(3)
                speak("i am done sir , now i am ready for next work ")
                print("i am done sir , now i am ready for next work ")

            except Exception as e:
                speak("dosen't find anything ")
                print("dosen't find anyhing")

        elif 'shut up maya' in query or 'shut up' in query:
            speak("fuck off")
            print("fuck off")

        elif 'internet speed test' in query:
            speak("wait i am checking sir")
            print("checking.....")
            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            speak(f"sir we have {dl} bit per second downloading speed and {up} bit per uploading speed")
            print(f"sir we have {dl} bit per second downloading speed and {up} bit per uploading speed")
            time.sleep(3)
            speak("i am done sir , now i am ready for next work ")
            print("i am done sir , now i am ready for next work ")

        elif 'instagram profile' in query or 'profile on instagram' in query:
            speak("please enter the user name correctly")
            name = input("enter username here")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"sir here is the profile of the user{name}")
            time.sleep(5)
            speak("sir would you like to download profile picture of this account")
            print("sir would you like to download profile picture of this account")
            condition = takecommand().lower()
            print(condition)
            if "yes" in condition:
                try:
                 mod = instaloader.Instaloader()
                 mod.download_profile(name, profile_pic_only=True)
                 speak("i am done sir , profile picture is saved in your main folder , now i am ready for next work ")
                 print("i am done sir , profile picture is saved in your main folder , now i am ready for next work ")

                except Exception  as e:
                    speak("id not found sir")
                    print("id not found sir")

            else:
                pass

        elif 'take screenshot' in query or 'take a screenshot' in query:
            speak("sir, please tell me the name of the screenshot file")
            print("sir, please tell me the name of the screenshot file")
            name = takecommand().lower()
            print(name)
            speak("please sir hold the screen for few second , i am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}png")
            print("i am done sir , the screenshot is saved in our main folder , now i am ready for next work")

        elif 'how are you maya' in query or 'how are you' in query:
            print("i am fine sir what about you")
            speak("i am fine sir what about you")

        elif 'i am also fine' in query or 'i am also good ' in query:
            print("that's great to hear from you")
            speak("that's great to hear from you")

        elif 'search maya' in query or 'search something maya' in query:
            print("what do you want to search sir")
            speak("what do you want to search sir")
            search = takecommand().lower()
            print(search)
            webbrowser.open(f"wwww.google.com/{search}")
            time.sleep(5)
            speak("i am done sir , now i am ready for next work ")
            print("i am done sir ,  now i am ready for next work ")

        elif 'my ip address' in query:
            ipadd = requests.get('https://api.ipify.org').text
            print(ipadd)
            speak(f"sir ip address is {ipadd}")

        elif 'hello maya' in query or 'hello' in query:
            speak("hello sir what can i do for you sir")
            print("hello sir what can i do for you sir")

        elif 'goodbye' in query:
            speak("thanks for using me sir have a good day")
            exit()


if __name__ == '__main__':
    while True:
        permission = takecommand()
        if "wake up" in permission:
            taskexecution()
        elif "goodbye" in permission:
            speak("thanks for using me sir have a good day")
            exit()
