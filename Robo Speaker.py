# For Windows Users
import pyttsx3

def text_to_speech(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()

text_to_speech("Wellcome to, Robo Speaker!")

while True:
    message = input("Enter the message : ")
    if message == "exit":
        text_to_speech("Bye bye, friend!")
        break
    text_to_speech(message)