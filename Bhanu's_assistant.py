# Createing a personal assistant
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voices',voices[0].id)
# print(voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("good morning bhanu!")
    elif hour<=12 and hour<=18:
        speak("good afternoon bhanu!")
    else:
        speak("good evening bhanu!")
    speak("I am chotu sir . your voice assistant . please tell me how may I help you")
def takecomand():
    #it takes microphone input from the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening your voice....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising your voice...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query} \n")
    except Exception as e:
        # print(e)

        print("say that again plaese sir...")
        return "None"
    return query
# def sendEmail(to, content):                             #This is use for send email if you want this the you can uncomment it and use
#     server = smtplib.SMTP('smtp.gmail.com',587)
#     server.ehlo()
#     server.starttls()
#     server.login('youremail@gmail.com',"yourpasswardhere")
#     server.sendmail('youremail@gmail.com',to,content)
#     server.close()


if __name__ == "__main__":
    # speak("Hii , bhanu")
    wishMe()
    # while True:     # This is use for continue listing 
    if 1:             # I use this if and 1 because it will run one time not continue 
        query = takecomand().lower()
    #Logic for executing task based on query
    if 'wikipedia' in query:
        speak("searching wikipedia for you sir...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'open whatsapp' in query:
        webbrowser.open("whatsapp.com")

    elif 'open github' in query:
        webbrowser.open("github.com")

    elif 'play music' in query:
        music_dir = 'F:\\mymusic'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))
        
    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"sir ,the time is {strTime}")

    elif 'open code'in query:
        codepath = "C:\\Users\\BHANU\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codepath)

    # elif 'email to bhanu' in query:   #This is use for send a email
    #     try:
    #         speak("what should I say..")
    #         content = takecomand()
    #         to = "yourEmail@gmail.com"
    #         sendEmail(to, content)
    #         speak("Email has been send.")
    #     except Exception as e:
    #         print(e)
    #         speak("sorry , My friend Bhnau I can not send this Email..")



    # In elif in query you can use your logic this is no limit and it is a simple code python program assistant



