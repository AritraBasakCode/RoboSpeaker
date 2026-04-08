'''import os

if __name__ == '__main__':
    print("Welcome to RoboSpeaker")
    while True:
        
        x = input("Enter what you want me to say: ")
        if x == 'q':
            os.system("say 'bye bye for the time'")
            break
        command = f"say {x}"
        os.system(command)
        '''
import pyttsx3

engine = pyttsx3.init()

if __name__ == '__main__':
    print("Welcome to RoboSpeaker")

    while True:
        x = input("Enter what you want me to say: ")

        if x == "q":
            engine.say("bye bye for the time")
            engine.runAndWait()
            break

        engine.say(x)
        engine.runAndWait()