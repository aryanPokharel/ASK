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


            elif said.lower() == "what is your age?":
                print("Nepali : Timro Umer/age kati ho?")
            elif said.lower() == "timro umer kati ho?" or said.lower() == "timro age kati ho":
                print("English : What is your age?")
            elif said.lower == "where are you from" or said.lower() == "where is your home":
                print("Nepali : Timro ghar kata ho?")
            elif said.lower() == "timro ghar kata ho" or said.lower() == "timi kata bata ho" or said.lower() == "timi kaha ko ho":
                print("English : Where are you from?")
            elif said.lower() == "what do you do":
                print("Nepali : Timi k garchau?")
            elif said.lower() == "timi k garchau":
                print("English : What do you do?")
            elif said.lower() == "where do you study":
                print("Nepali : Timi k padchau?")
            elif said.lower() == "timi k padchau":
                print("English : What do you study?")
            elif said.lower() == "where is the taxi stand" or said.lower() == "where can i find taxis" or said.lower() == "where can i find a taxi":
                print("Nepali : Taxi kata paincha?")
            elif said.lower() == "taxi kaha paincha" or said.lower() == "taxi kata paincha" or said.lower() == "yaha taxi kaha paincha" or \
                    said.lower() == "yaha taxi kata paincha":
                print("English : Where can i find a taxi?")

            else:
                print("That phrase is not recorded!")

        except:
            print("Sorry! Sound Unrecognised!")
            playsound('sounds/nepali/feriBol.mp3')



