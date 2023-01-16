# System Module ======================
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter as tk
import sys
from threading import Thread
import threading
from time import sleep
import time
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes
from PyDictionary import PyDictionary

# Local modules ======================
import Functions
import SystemFunctions
import Calculator

# Global Variables ===================
AI_NAME = "KRISTHEL"
EXIT_COMMANDS = ['shutdown', 'shut down', 'quit', 'exit', 'bye', 'good bye']
ai_text = ""
bg = "white"
bg1 = "#0b4072"
bg2 = "#EBF8FF"
status = True

# AI VIRTUAL ASSISTANT VOICE ==================================================
try:
    engine = pyttsx3.init()
    r = sr.Recognizer()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # male
except Exception as e:
    print(e)

# TEXT TO SPEECH ==============================================================
def speak(text):
    lbl_ai_stat['text'] = 'Speaking...'
    ai_text['text'] = text
    print(text)
    engine.say(text)
    engine.runAndWait()

# SPEECH TO TEXT ==============================================================
def record():
    with sr.Microphone() as source:
        if status: r.adjust_for_ambient_noise(source, duration=1)
        if status: ai_text['image'] = ''
        if status: speak('Listening..')
        if status: lbl_ai_stat['text'] = 'Listening...'
        if status: ai_text['text'] = '...'
        if status: audio = r.listen(source)
    try:
        if status: print("Processing...")
        if status: lbl_ai_stat['text'] = 'Processing...'
        if status: query = r.recognize_google(audio, language='en_US')  # Google for voice recognition.
        if status: print('Your message:', format(query))
    except:
        return

    if status: return query
    else: return

# ACTIVATING AI VIRTUAL ASSISTANT =============================================
def aiActive1():
    speak(Functions.greet())
    speak(f'My name is {AI_NAME}')
    speak('I am an AI virtual assistant always ready to help you.')
    aiActive()

def aiActive():
    speak('How may i help you?')
    global status
    while status:
        query = record()
        if query == None: continue
        if isContain(query, EXIT_COMMANDS):
            speak("Im going OFFLINE. Good Bye!")
            lbl_ai_stat['text'] = 'Exiting...'
            ai_text['text'] = '...'
            close()
            break
        else:
            main(query.lower())

def micSwitch():
    global status
    if status:
        status = False
        print(f"STATUS: {status} OFFLINE")
        lbl_ai_stat['text'] = 'Sleeping Zzz...'
        ai_text['text'] = "..."
    else:
        status = True
        print(f"STATUS: {status} ACTIVE")
        Thread(target=aiActive).start()

#  COMMAND HANDLER =========================================================
def isContain(txt, lst):
    for word in lst:
        if word in txt:
            return True
    return False

def main(query):
    # AI VIRTUAL ASSISTANT NAME
    if isContain(query, ['what\'s your name', 'what is your name', 'who are you', 'what are you']):
        speak('My name is, ' + AI_NAME)
        speak('I am an AI Virtual Assistant created to help you')
        return
    # GREETS BACK
    if isContain(query, ['morning', 'evening', 'noon']) and 'good' in query:
        speak(Functions.chat("good"))
        return
    # CURRENT DATE / TIME
    if isContain(query, ['time', 'date']):
        speak(Functions.chat(query))
        return
    # PLAY YOUTUBE VIDEO
    if 'play' in query:
        speak('Opening youtube...')
        engine.runAndWait()
        pywhatkit.playonyt(query)
        micSwitch()
        return
    # SEARCH IN GOOGLE
    if 'google' in query:
        speak('Searching on Google...')
        engine.runAndWait()
        pywhatkit.search(query)
        micSwitch()
        return
    # DICTIONARY
    if isContain(query, ['definition', 'meaning', 'define']):
        dictionary = PyDictionary()
        query = query.replace('what is', '')
        query = query.replace('the', '')
        query = query.replace('definition', '')
        query = query.replace('meaning', '')
        query = query.replace('define', '')
        query = query.replace('of', '')
        result = dictionary.meaning(query)
        speak(result)
        return
    # TELLS A JOKE
    if 'joke' in query:
        speak(pyjokes.get_joke())
        engine.runAndWait()
        return
    # SEARCH IN WIKIPEDIA
    if 'wikipedia' in query:  # if wikipedia found in the query then this block will be executed
        ai_text['text'] = 'Searching Wikipedia...'
        speak('Searching Wikipedia...')
        try:
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        except:
            speak(f"Your query: {query} was Not Found")
            speak("Please Repeat command")
            return
        return
    # TRANSLATOR
    if "translate" in query:
        sentence = query.replace('translate', '')
        speak("Which language to translate ?")
        language = record()
        result = Functions.lang_translate(sentence, language)

        if result == "None":
            speak("This language doesn't exists")
        else:
            speak(f"In {language.capitalize()} you would say:")
            print(f"In {language.capitalize()} you would say: ", result.text)
            speak(result.text)
        return
    # TOSS A COIN / ROLL A DIE
    if isContain(query, ['coin', 'dice', 'die']):
        if isContain(query, ['toss', 'roll', 'flip', 'throw']):
            result = Functions.generate(query)
            print(result)
            if "Head" in result:
                image = ImageTk.PhotoImage(Image.open('images/head.png').resize((200, 200), Image.ANTIALIAS))
                ai_text['image'] = image
            elif "Tail" in result:
                image = ImageTk.PhotoImage(Image.open('images/tail.png').resize((200, 200), Image.ANTIALIAS))
                ai_text['image'] = image
            else:
                image = ImageTk.PhotoImage(Image.open('images/' + result[-1] + '.png').resize((200, 200), Image.ANTIALIAS))
                ai_text['image'] = image
            speak(result)
            return
    # BASIC CALCULATOR
    if isContain(query, ['calculate', 'compute']):
        try:
            query = query.replace('calculate', '')
            query = query.replace('compute', '')
            query = query.replace('negative ', '-')

            speak(('Result is: ' + Calculator.calculate(query)))
        except Exception as e:
            return
        return
    # OPEN WEBSITE / SYSTEM PROGRAM
    if 'open' in query:
        bool = SystemFunctions.accessApp(query)
        if bool == False:
            speak(f"Your query: {query} was Not Found")
        micSwitch()
        return
    # TAKE SCREENSHOT
    if 'screenshot' in query:
        # Thread(target=SystemFunctions.winOpt(query), args=('screenshot', 'capture', 'snapshot')).start()
        SystemFunctions.winOpt(query)
        speak("Screenshot Taken")
        micSwitch()
        return
    # CLOSE CURRENT SELECTED/ACTIVE WINDOW
    if isContain(query, ['window', 'close that']):
        SystemFunctions.winOpt(query)
        return
    # CLOSE CURRENT TAB
    if isContain(query, ['tab']):
        SystemFunctions.tabOpt(query)
        return
    # WRITE
    if isContain(query, ['type', 'save', 'delete', 'select', 'press enter']):
        SystemFunctions.systemOpt(query)
        return

# GUI Functions ===========================================================================================
def progressbar():
    s = ttk.Style()
    s.theme_use('clam')
    s.configure("cyan.Horizontal.TProgressbar", foreground='#2ee3ec', background='#2ee3ec')
    progress_bar = ttk.Progressbar(splash_root, style="cyan.Horizontal.TProgressbar", orient="horizontal",
                                   mode="determinate", length=303)
    progress_bar.pack()
    splash_root.update()
    progress_bar['value'] = 0
    splash_root.update()

    while progress_bar['value'] < 100:
        progress_bar['value'] += 5
        splash_root.update()
        sleep(0.3)

def destroySplash():
    splash_root.destroy()

def close():
    time.sleep(1)
    root.destroy()
    sys.exit()

# Driver Program ===============================================================================================================
if __name__ == '__main__':
    # SPLASH Screen ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    splash_bg = "#0b4072"
    splash_root = Tk()
    splash_root.configure(bg=splash_bg)
    splash_root.overrideredirect(True)

    w_width, w_height = 500, 550
    s_width, s_height = splash_root.winfo_screenwidth(), splash_root.winfo_screenheight()
    x, y = (s_width / 2) - (w_width / 2), (s_height / 2) - (w_height / 2)
    splash_root.geometry('%dx%d+%d+%d' % (w_width, w_height, x, y - 30))

    obj_bot = ImageTk.PhotoImage(Image.open("images/bot.png").resize((350, 350), Image.ANTIALIAS))
    img_ai = Label(splash_root, image=obj_bot, bg=splash_bg)
    img_ai.pack(pady=(20, 0))

    splash_label = Label(splash_root, text=AI_NAME, font=('calibri', 15, "bold"), bg=splash_bg, fg='white')
    splash_label.pack()
    splash_label1 = Label(splash_root, text="AI Virtual Assistant", font=('calibri', 15, "bold"), bg=splash_bg, fg='white')
    splash_label1.pack(pady=(0,40))

    progressbar()
    splash_root.after(10, destroySplash)
    splash_root.mainloop()

    # MAIN Screen ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    root = Tk()
    root.title(AI_NAME)
    icon = PhotoImage(file='images/bot.png')
    root.iconphoto(True, icon)
    w_width, w_height = 500, 800
    s_width, s_height = root.winfo_screenwidth(), root.winfo_screenheight()
    x, y = (s_width / 2) - (w_width / 2), (s_height / 2) - (w_height / 2)
    root.geometry('%dx%d+%d+%d' % (w_width, w_height, x, y - 30))  # center location of the screen
    root.configure(bg=bg2)
    root.resizable(width=False, height=False)
    # FRAME 1: AI logo and status ------------------------------------------
    frame1 = Frame(root, bg=bg1)
    frame1.pack(fill="both", expand=True)

    obj_bot = ImageTk.PhotoImage(Image.open("images/bot.png").resize((300, 300), Image.ANTIALIAS))
    img_ai = Label(frame1, image=obj_bot, bg=bg1)
    img_ai.pack()

    lbl_ai_stat = Label(frame1, text='OFFLINE', font=('calibri', 16), fg='white', bg=bg1)
    lbl_ai_stat.pack(pady=(0, 20))

    # FRAME 2: AI Text output ------------------------------------------
    frame2 = Frame(root, bg=bg2)
    frame2.pack(fill="both", expand=True)

    canvas = tk.Canvas(frame2, bg=bg2, height=360)
    scrollbar = ttk.Scrollbar(frame2, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        ),
    )
    style = ttk.Style()
    style.configure("Vertical.TScrollbar", background="green", bordercolor="red", arrowcolor="white")
    canvas.create_window((0, 0), window=scrollable_frame)
    canvas.configure(yscrollcommand=scrollbar.set)

    ai_text = Label(scrollable_frame, text="", font=('calibri', 12),
                    wraplength=450, bg=bg2, justify="center", anchor="center")
    ai_text.pack(ipady=10, ipadx=15)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # FRAME 3: mic switch ----------------------------------------------
    frame3 = Frame(root, bg=bg2)
    frame3.pack(fill="both", expand=True, side = BOTTOM)

    obj_mic = ImageTk.PhotoImage(Image.open("images/mic-1.png").resize((55, 55), Image.ANTIALIAS))
    btn_mic = tk.Button(frame3, image=obj_mic, bg=bg2, activebackground=bg2,
                        command=micSwitch)
    btn_mic["border"] = "0"
    btn_mic.pack(pady=10)

# Activate KRISTHEL AI Virtual Assistant =============================================================
    try:
        main_thread = threading.Thread(target=aiActive1)
        main_thread.start()
    except:
        pass

root.mainloop()