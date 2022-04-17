import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
#from selenium import webdriver
import pyautogui as pt
import pyperclip as pc
from pynput.mouse import Controller, Button
from time import sleep
from Wtrainer import response

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")

        elif 'whatsapp' in query:
            #driver = webdriver.Chrome("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
            #driver.get("web.whatsapp.com")
            #webbrowser.Chrome.open("whatsapp.com")
            #webbrowser.get("C:\\Program Files(x86)\\Google\\Chrome\\Application\\chrome.exe").open("https://web.whatsapp.com/")
            webbrowser.open("web.whatsapp.com")

            sleep(10)

            # Requires opencv
            # -python package for image recognition confidence

            # Mouse click workaround for MAC OS
            mouse = Controller()


            # Instructions for our WhatsApp Bot
            class WhatsApp:

                # Defines the starting values
                def __init__(self, speed=.5, click_speed=.3):
                    self.speed = speed
                    self.click_speed = click_speed
                    self.message = ''
                    self.last_message = ''

                # Navigate to the green dots for new messages
                def nav_green_dot(self):
                    try:
                        position = pt.locateOnScreen('green_dot.png', confidence=.7)
                        pt.moveTo(position[0:2], duration=self.speed)
                        pt.moveRel(-100, 0, duration=self.speed)
                        pt.doubleClick(interval=self.click_speed)
                    except Exception as e:
                        print('Exception (nav_green_dot): ', e)

                # Navigate to our message input box
                def nav_input_box(self):
                    try:
                        position = pt.locateOnScreen('paperclip.png', confidence=.7)
                        pt.moveTo(position[0:2], duration=self.speed)
                        pt.moveRel(120, 20, duration=self.speed)
                        pt.doubleClick(interval=self.click_speed)
                    except Exception as e:
                        print('Exception (nav_input_box): ', e)

                # Navigates to the message we want to respond to
                def nav_message(self):
                    try:
                        position = pt.locateOnScreen('paperclip.png', confidence=.7)
                        pt.moveTo(position[0:2], duration=self.speed)
                        pt.moveRel(60, -65, duration=self.speed)  # x,y has to be adjusted depending on your computer
                    except Exception as e:
                        print('Exception (nav_message): ', e)

                # Copies the message that we want to process
                def get_message(self):
                    mouse.click(Button.left, 3)
                    sleep(self.speed)
                    mouse.click(Button.right, 1)
                    sleep(self.speed)
                    pt.moveRel(80, -580, duration=self.speed)  # x,y has to be adjusted depending on your computer
                    mouse.click(Button.left, 1)
                    sleep(1)

                    # Gets and processes the message
                    self.message = pc.paste()
                    print('User says: ', self.message)

                # Sends the message to the user
                def send_message(self):
                    try:
                        # Checks whether the last message was the same
                        if self.message != self.last_message:
                            bot_response = response(self.message)
                            reply = bot_response

                            print('You say: ', bot_response)

                            pt.typewrite(bot_response, interval=.1)
                            pt.typewrite('\n')  # Sends the message (Disable it while testing)
                            engine = pyttsx3.init()
                            engine.say(reply)
                            engine.runAndWait()

                            # Assigns them the same message
                            self.last_message = self.message
                        else:
                            print('No new messages...')

                    except Exception as e:
                        print('Exception (send_message): ', e)

                # Close response box
                def nav_x(self):
                    try:
                        position = pt.locateOnScreen('x.png', confidence=.7)
                        pt.moveTo(position[0:2], duration=self.speed)
                        pt.moveRel(23, 23, duration=self.speed)  # x,y has to be adjusted depending on your computer
                        mouse.click(Button.left, 1)
                    except Exception as e:
                        print('Exception (nav_x): ', e)


            # Initialises the WhatsApp Bot
            wa_bot = WhatsApp(speed=.5, click_speed=.4)

            # Run the programme in a loop
            while True:
                wa_bot.nav_green_dot()
                wa_bot.nav_x()
                wa_bot.nav_message()
                wa_bot.get_message()
                wa_bot.nav_input_box()
                wa_bot.send_message()

                # Delay between checking for new messages
                sleep(10)