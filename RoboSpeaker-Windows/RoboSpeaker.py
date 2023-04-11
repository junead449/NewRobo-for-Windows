import pyttsx3

engine = pyttsx3.init()
print("Welcome to RoboSpeaker Version 1.1:  ")
while True:
    engine.say(input("Enter The Word that you want to speak: "))
    if engine.say=='q':
        break
    engine.runAndWait()
