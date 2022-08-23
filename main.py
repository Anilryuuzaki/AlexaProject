# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
from datetime import datetime
import pyjokes


# This function convert text to speech
def talk(answer):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(answer)
    engine.runAndWait()


# this function get the question from the user
def getQuestion():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        try:
            print(r.recognize_google(audio))
            question = r.recognize_google(audio)
            if "Alexa" in question:
                question = question.replace('Alexa', '')
                print(question)
                return question
            else:
                print("You are not talking with me")
                return "notwithme"

        except sr.UnknownValueError:
            print("Sorry i Can't recognize your question")
            return True


# This function process the question and give the output to the user
def processQuestion(question):
    if 'what are you doing' in question:
        print('i am waiting for your question')
        talk('i am waiting for your question')

    elif 'how are you' in question:
        print('Iam good, thank you. How can i help you')
        talk('Iam good, thank you. How can i help you')
        return True
    elif 'play' in question:
        question = question.replace('play', '')
        pywhatkit.playonyt(question)
        return True
    elif 'who is' in question:
        question = question.replace('who is', '')
        print(wikipedia.summary("Wikipedia"))
        talk(wikipedia.summary(question, 1))
        return True
    elif "time" in question:
        time = datetime.today().time().strftime("%I : %M %p")
        print(time)
        talk(time)
        return True
    elif "joke" in question:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
        return True
    elif "bye" in question:
        talk("Ok carry on with your friends, bye!")
        return False
    else:
        print("i didn't your question, can you say that again")
        return True


# while loop run until the return false
canAskQuestion = True
while canAskQuestion:
    question = getQuestion()
    if question == "notwithme":
        talk("Ok carry on with your friends, bye!")
        canAskQuestion = False
    else:
        canAskQuestion = processQuestion(question)
