import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from time import sleep

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)





def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'atlas' in command:
                command = command.replace('atlas', '')
                print(command)
    except:
        sleep(5)
        try:
            with sr.Microphone() as source:
                print('listening...')
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
                if 'atlas' in command:
                    command = command.replace('atlas', '')
                    print(command)
        except:
            pass

    return command


def run_atlas():
    while True:
        command = take_command()
        song = command.replace('play', '')
        if 'play' in command:
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'search' in command:
            subject = command.replace('search', '')
            talk('searching' + subject)
            pywhatkit.search(subject)
        elif 'what time is it' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            talk('Current time is' + time)
        elif 'tell me about' in command:
            try:
                about = command.replace('tell me about', '')
                info = wikipedia.summary(about, 1)
                print(info)
                talk(info)
            except:
                talk("I can't found anything")
        elif 'date' in command:
            talk("Sorry, I think we don't match")
        elif 'are you single' in command:
            talk('I am in a relationship with wi-fi')
        elif 'do you love me' in command:
            talk('of course, we are best friends')
        elif 'tell me a joke' in command:
            joke = pyjokes.get_joke()
            print(joke)
            talk(joke)
        elif 'see you later' in command:
            talk('Ok, bye-bye')
            break
        elif 'how are you' in command:
            talk('Im good, glad that you ask, and you')
        elif 'are you alive' in command:
            talk('Of course, you made me')
        elif 'who is the queen' in command:
            talk('Renata Guimarães')
        elif 'are you there' in command:
            talk('yes, Im here')
        elif 'Im not talking to you' in command:
            talk('Ok, sorry')
        else:
            talk('Sorry, I cant understand, say again')


run_atlas()
