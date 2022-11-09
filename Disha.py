import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import os
import sys
import pywhatkit
import cv2
import random
from googletrans import Translator
from requests import get

# to speak
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)


# def=function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak('Good Morning!')
    elif hour >= 12 and hour < 18:
        speak('Good Afternoon!')
    elif hour >= 18 and hour < 24:
        speak('Good Evening!')

    speak('I am Disha sir,please tell me How can i help you')


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f'user said: {query}')
    except Exception as e:
        print('say that again please...')
        return "none"
    query = query.lower()
    return query


def taskexecution():
    wishme()
    # if 1:
    while True:
        query = takecommand()
        # logic building
        # conversation with ai
        if 'hello disha' in query:
            speak('hello sir,How are you doing')
        elif"I am fine" in query:
            speak('it sounds good to hear from you')



        elif "can we talk for some time" in query:
            speak("sure sir,please don't make me feel guilty by saying so")

        elif "do you know Roshani" in query:
            speak('yes I do , she is your sister. Am i right')
        elif"do you know saroj" in query:
            speak('Saroj Chaudhary,oh yes he is your about to be  Brother in law.Right')
        elif"yes you are"in query:
            speak("Disha is always Right")
        elif"would you like to say something to them" in query:
            speak('for what sir')
        elif"for their engagement" in query:
            speak('yes I was waiting for this time since long')
        elif"wish them" in query:
            speak("So happy for the both of you. and I can’t wait to celebrate this new chapter of your lives ")
            speak("Of all the big life events I’ve celebrated ever, this one tops the list. Congratulations!")
            speak("and Best wishes for a long and happy life together.")
        elif"for their marriage"in query:
            speak("sure sir")
            speak("So happy for the both of you. and I can’t wait to celebrate this new chapter of your lives ")
            speak("Of all the big life events I’ve celebrated ever, this one tops the list. Congratulations!")
            speak("and Best wishes for a long and happy life together.")


        elif "who is your boss" in query:
            speak("well, i call him DK it's easier to say")

        elif 'who are you' in query or "say something about yourself"in query:
            speak(' I am artificial intelligence, Programmed by DK who call me  Disha ')

        elif 'are you married' in query:
            speak('no i am not but searching for a loyal programme which can work with me for my boss dk')

        elif 'will you marry Aadarsh bhai' in query:
            speak('i would love to but he is not ready although his age is flowing as river')

        elif "how are you" in query:
            speak('I am fine ,what about you sir ')

        elif 'as usual' in query:
            speak('It means that you are bored,shall i play music for you sir')

        elif 'do you love me' in query or 'i love you' in query:
            speak('Sorry sir i am already committed and i have a boyfriend ')
        elif 'i am your boss' in query:
            speak('so what i cannot love you.i have a boyfriend and i am searching for a loyal husband   ')

        elif "alright let's get back to work" in query:
            speak('sure sir,just let me know the way i can help you')

        # command for work
        elif 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=4)
            speak('According to wikipedia ')
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open facebook' in query:
            webbrowser.open('fb.com')
        elif 'open free Bitcoin' in query:
            webbrowser.open('freebitco.in')
        elif 'open google' in query:
            speak('sir what should i search on google')
            cm = takecommand()
            webbrowser.open(f'{cm}')

        elif 'open command prompt' in query:
            os.system('start cmd')

        elif "ip address" in query:
            ip = get("https://api.ipify.org").text
            speak(f" your IP address is {ip}")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
        #    music_dir = "C:\\Users\\Ramjay\\Music\\Hindi song"
            music_dir = "D:\\Users\\Ramjay\\Downloads\\Safe\\songs"

            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))


        elif "please" in query:
           # music_dir = "C:\\Users\\Ramjay\\Music\\Hindi song"
            music_dir = "D:\\Users\\Ramjay\\Downloads\\Safe\\songs"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))
        elif 'emotional song' in query:
            speak('searching on youtube...')
            pywhatkit.playonyt("meri pyari behna  song")

        elif"not this"in query:
            speak('sorry sir wait a second')
            pywhatkit.playonyt("dilbaro song")
        elif "close youtube"in query:
            speak("closing youtube sir")
            os.system("taskkill/f/im youtube.com")
        elif"close facebook"in query:
            speak('closing facebook,sir')
            os.system("taskkill/f/im facebook.com")


        elif 'take rest' in query:
            speak('thank you sir it was pleasure working for you,call me anytime')
            break


if __name__ == '__main__':
    while True:
        permission = takecommand()
        if 'wake up ' in permission:
            taskexecution()
        elif 'rest now' in permission or 'exit' in permission:
            speak('thank you sir,it was amazing working with you')
            sys.exit()
