from plyer import notification
import pyttsx3
import time

if __name__ == "__main__":
    while True:
        your_message = "You have a meeting at 10 a.m with Mr X on Skype!"
        notification.notify(
            title = "Skype Call Reminder",
            message = your_message,
            app_icon = "icon.ico",
            timeout = 2
        )
        speak = pyttsx3.init()
        speak.say(your_message)
        speak.runAndWait()
        time.sleep(6)
        #'pythonw.exe main.py' to run this python script in background.
