from tkinter import font
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

import time
import pyautogui
from tkinter import *

window = Tk()
window.geometry("700x600")

class TwitterBot:
    print("SAFE TILL CLASS EXECUTION")
    def __init__(self, username, password):
        self.username = username
        self.password = password
        print("USERNAME ND PASS CORRECT")
        service = Service(executable_path="chromedriver.exe")
        self.bot=webdriver.Chrome(service=service);
        print("SUCESSS")

    def login(self):
        bot = self.bot
        bot.get("https://twitter.com/login")
        time.sleep(5)
        
        email = bot.find_element(By.NAME, "text")
        # password = bot.find_element(By.NAME, "session[password]")
        
        email.clear()
        # # password.clear()
        
        email.send_keys(self.username)
        # password.send_keys(self.password)
        # password.send_keys(Keys.RETURN)
        # time.sleep(5)
        print("LOGINED")
        bot.quit();

    def like_tweet(self, hashtag):
        bot = self.bot
        bot.get(f"https://twitter.com/search?q={hashtag}&src=typed_query&f=live")
        time.sleep(5)
        
        try:
            heart_location = pyautogui.locateCenterOnScreen('heart.png')
            if heart_location:
                pyautogui.click(heart_location, duration=2)
            else:
                print("Heart icon not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
        
        time.sleep(5)
        bot.quit()

def execute():
    log = TwitterBot(str(entry1.get()), str(entry2.get()))
    print()
    log.login()
    # log.like_tweet(entry3.get())

# PLACING EMAIL
email_label = Label(window, text="Email: ", font="times 24 bold")
email_label.grid(row=0, column=0)
entry1 = Entry(window)
entry1.grid(row=0, column=1)

# PLACING PASSWORD
password_label = Label(window, text="Password: ", font="times 24 bold")
password_label.grid(row=2, column=0)
entry2 = Entry(window, show='*')
entry2.grid(row=2, column=1)

# PLACING HASHTAG
hashtag_label = Label(window, text="Hashtag: ", font="times 24 bold")
hashtag_label.grid(row=4, column=0)
entry3 = Entry(window)
entry3.grid(row=4, column=1)

# GO BUTTON
b1 = Button(window, text="GO!", command=execute, width=12, bg='gray')
b1.grid(row=7, column=1)
print("CLASS EXECUTED")

window.mainloop()
