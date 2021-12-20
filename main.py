import pyttsx3
from playsound import playsound
import speech_recognition as sr

mic = sr.Recognizer()

recognized = False
with sr.Microphone() as source1:
    
    while recognized == False:
        print("Say something : ")
        something = mic.listen(source1)

        try:
            said = str(mic.recognize_google(something))
            print(">>", said)
            recognized = True

            if said.lower() == "how are you":
                print("Nepali : k cha khabar")
                playsound('sounds/nepali/kChaKhabar.mp3')

            elif said.lower() == "k cha khabar" or said.lower() == "ke chha khabar":
                print("English : how are you")
                playsound('sounds/english/howAreYou.mp3')

            elif said.lower() == "i am fine":
                print("Nepali : Ma sanchai chu")
            elif said.lower() == "ma sanchai chu":
                print("English : I am fine")
            elif said.lower() == "what is your name":
                print("Nepali : Timro naam k ho")
                playsound('sounds/nepali/timroNaamKHo.mp3')
            elif said.lower() == "timro naam k ho":
                print("English : What is your name?")
                playsound('sounds/english/whatIsYourName.mp3')
            else:
                print("That phrase is not recorded!")

        except:
            print("Sorry! Sound Unrecognised!")
            playsound('sounds/nepali/feriBol.mp3')



