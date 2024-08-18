import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser
from email.message import EmailMessage
import smtplib
from decouple import config

EMAIL = "mahboobhasan8770@gmail.com"
PASSWORD = "1998"
def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)
    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

query = takeCommand().lower()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("veronica","")
        query = query.replace("google search","")
        query = query.replace("google","")
        speak("This is what I found on google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            speak(result)

        except:
            speak("No speakable output available")

def searchYoutube(query):
    if "youtube" in query:
        speak("This is what I found for your search!") 
        query = query.replace("youtube search","")
        query = query.replace("youtube","")
        query = query.replace("veronica","")
        web  = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done, Sir anything else sir")

def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Searching from wikipedia....")
        query = query.replace("wikipedia","")
        query = query.replace("search wikipedia","")
        query = query.replace("veronica","")
        results = wikipedia.summary(query,sentences = 2)
        speak("According to wikipedia..")
        print(results)
        speak(results)

def searchFacebook(query):
    if "facebook" in query:
        speak("Searching facebook for you sir...")
        query = query.replace("open my facebook","")
        query = query.replace("search facebook","")
        query = query.replace("veronica","")
        web = "https://www.facebook.com/mahboob.hasan.1253"
        webbrowser.open(web)
        speak("Done, Sir anythig else sir")

def searchLinkedin(query):
    if "linkedin" in query:
        speak("Opening Linkedin for you sir...")
        query = query.replace("open my linkedin","")
        query = query.replace("search linkedin","")
        query = query.replace("veronica","")
        web = "https://www.linkedin.com/in/mahboob-hasan-24135319b"
        webbrowser.open(web)
        speak("Done, Sir anything else sir")

def searchInstagram(query):
    if "instagram" in query:
        speak("Opening instagram for you sir...")
        query = query.replace("open my instagram" ,"")
        query = query.replace("search instagram","")
        query = query.replace("veronica","")
        web = "https://www.instagram.com/mahboobhasan05/"
        webbrowser.open(web)
        speak("Done, Sir anything else sir") 
def searchGmail(query):
    if "gmail" in query:
        speak("Opening gmail for you sir...")
        query = query.replace("open my gmail" ,"")
        query = query.replace("search gmail","")
        query = query.replace("veronica","")
        web = "https://mail.google.com/mail/u/0/#inbox"
        webbrowser.open(web)
        speak("Done, Sir anything else sir") 
def send_emial(receiver_add,subject,message):
    try:
        email = EmailMessage()
        email['Subject'] = subject
        email['From'] = EMAIL
        email['To'] = receiver_add
        email.set_content(message)
        s = smtplib.SMTP("smtp.gmail.com",587)
        s.starttls()
        s.login(EMAIL,PASSWORD)
        s.send_message(email)
        s.close()
        return True
    except Exception as e:
        print(e)
        return False
    
