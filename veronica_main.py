import pyttsx3
import speech_recognition 
import requests
from bs4 import BeautifulSoup
import datetime
import os
import pyautogui
import webbrowser
import random
import speedtest
from decouple import config
from plyer import notification
from pygame import mixer
from INTRO import play_gif
play_gif

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
rate = engine.setProperty("rate",190)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("I am veronica, welcome to the most advance AI assistant")
def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,5)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query



if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir , You can me call anytime")
                    break
                
                #To do list
                elif "schedule my day" in query:
                    tasks = []  
                    speak("Do you want to clear old tasks (Plz speak YES or NO)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()

                elif "show my schedule" in query:
                    file = open("tasks.txt","r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("notification.mpeg")
                    mixer.music.play()
                    notification.notify(
                        title = "My schedule :-",
                        message = content,
                        timeout = 15
                        )
                
                #Focus mode
                elif "focus mode" in query:
                    a = int(input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO "))
                    if (a==1):
                        speak("Entering the focus mode....")
                        os.startfile("C:\\Users\\mahboob\\OneDrive\\Documents\\veronica\\FocusMode.py")
                        exit()
                    else:
                        pass
                
                #Translate
                elif "translate" in query:
                    from Translator import translategl
                    query = query.replace("veronica","")
                    query = query.replace("translate","")
                    translategl(query)

                #Open apps  
                elif "open" in query:
                    query = query.replace("open","")
                    query = query.replace("veronica","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter") 

                #chech internet speed
                elif "internet speed" in query:
                    wifi  = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576         
                    download_net = wifi.download()/1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ",download_net)
                    speak(f"Wifi download speed is {download_net}")
                    speak(f"Wifi Upload speed is {upload_net}")
                
                #Check Cricket Score
                elif "cricket score" in query:
                    from plyer import notification
                    import requests
                    from bs4 import BeautifulSoup
                    try:
                        url = "https://www.cricbuzz.com/cricket-match/live-scores/recent-matches"
                        page = requests.get(url)

                        if page.status_code == 200:
                            soup = BeautifulSoup(page.text, "html.parser")
                            team_elements = soup.find_all("a", class_="cb-ovr-flo cb-hmscg-tm-nm")
                            score_elements = soup.find_all("div", class_="cb-ovr-flo")

                            if len(team_elements) >= 2 and len(score_elements) >= 2:
                                team1 = team_elements[0].get_text().strip()
                                team2 = team_elements[1].get_text().strip()

                                # Filter out the score elements that do not contain team scores
                                team_scores = [el for el in score_elements if el.find("a", class_="cb-ovr-flo cb-hmscg-tm-nm")]
                                
                                if len(team_scores) >= 2:
                                    team_score1 = team_scores[0].get_text().strip()
                                    team_score2 = team_scores[1].get_text().strip()
                                    
                                    print(f"{team1} : {team_score1}")
                                    print(f"{team2} : {team_score2}")

                                    notification.notify(
                                        title="IPL Score Brief",
                                        message=f"{team1} : {team_score1}\n{team2} : {team_score2}",
                                        timeout=10
                                    )
                                else:
                                    print("Scores not found for the teams.")
                            else:
                                speak("Sorry, No Cricket Match is Live Now...!!")
                        else:
                            print(f"Failed to fetch the webpage. Status code: {page.status_code}")
                    except requests.RequestException as e:
                        print(f"An error occurred while fetching the webpage: {e}")

                #Game
                elif "game" in query:
                    from game import game_play
                    game_play()
                    
                
                #Take Screenshot
                elif "screenshot" in query:
                     import pyautogui 
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")

                #Take photos
                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")

                #Normal conversation
                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "how r u" in query:
                    speak("Perfect, sir")
                elif "thank u" in query:
                    speak("you are welcome, sir")
                elif "what is your name" in query:
                    speak("My name is veronica, sir")
                
                #Play any song 
                elif "choice" in query:
                    speak("Playing my favourite songs, sir")
                    a = (1,2,3,4,5) 
                    b = random.choice(a)
                    if b==1:
                     webbrowser.open("https://www.youtube.com/watch?v=35Q1gs07LkU&list=RD35Q1gs07LkU&start_radio=1")
                    elif b==2:
                     webbrowser.open("https://www.youtube.com/watch?v=-2kl2re74Dk&list=RD35Q1gs07LkU&index=3")
                    elif b==3:
                     webbrowser.open("https://www.youtube.com/watch?v=9sekgEXGm-E")
                    elif b==4:
                     webbrowser.open("https://www.youtube.com/watch?v=o7In7se2Kl4&list=RD9sekgEXGm-E&index=9")
                    elif b==5:
                     webbrowser.open("https://www.youtube.com/watch?v=9oVBbcqN6m4")   
                
                #Control youtube 
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")
                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up,sir")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown()

                #Open particular apps
                elif "open" in query: 
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)
                           
                #Search 
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)
                elif "facebook" in query:
                    from SearchNow import searchFacebook
                    searchFacebook(query)
                elif "linkedin" in query:
                    from SearchNow import searchLinkedin
                    searchLinkedin(query)
                elif "inistagram" in query:
                    from SearchNow import searchInstagram
                    searchInstagram(query)
                elif "gmail" in query:
                    from SearchNow import searchGmail
                    searchGmail(query)
                elif "send an email" in query:
                    from SearchNow import send_emial
                    speak("please enter the email address you want to send an email")
                    receiver_add = input("Enter the email address: ")
                    speak("what should be the subject sir")
                    subject = takeCommand().capitalize()
                    speak("what should be the message sir")
                    message = takeCommand().capitalize()
                    if send_emial(receiver_add,subject,message):
                        speak("email has been sent")
                    else:
                        speak("something went wrong please check the error sir")

                #News
                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()

                #Calculator
                elif "calculate" in query:
                    from Calculatenumbers import WolfRamAlpha
                    from Calculatenumbers import Calc
                    query = query.replace("calculate","")
                    query = query.replace("jarvis","")
                    Calc(query)

                #Open whatsapp  
                elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage() 

                #Current weather and time                                       
                elif "temperature" in query:
                    search = "temperature in noida"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "weather" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"Sir, the time is {strTime}")
                
                #Alarm
                elif "set an alarm" in query:
                        from alarm import alarm
                        print("Input Time for Alarm(i.e: 08:10 AM/PM): ")
                        speak('Set the Time')
                        t = input("Please tell the time: ")
                        t = str(t).replace(".", " ")
                        t = t.upper()
                        alarm(t)
                        speak("Done, Sir")


                #Exit  
                elif "finally sleep" in query:
                    speak("Going to sleep,sir")
                    exit()
                
                #Remember 
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("veronica","")
                    speak("You told me to"+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me to" + remember.read())

                #System shutdown
                elif "shutdown" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")
                    elif shutdown == "no":
                        break
