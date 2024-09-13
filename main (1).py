from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox as msg
import pyttsx3
import speech_recognition as sr
import os
import socket

def listen(duration, language="ta-IN"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recognizer.record(source, duration=duration)
        try:
            # Recognize Tamil speech but output in English
            return recognizer.recognize_google(audio, language="en-IN")
        except sr.UnknownValueError:
            return "Didn't hear perfectly!"
        except sr.RequestError:
            return "API unavailable!"

def ssk():
    text = listen(5, "ta-IN")  # Listening for Tamil speech
    e.insert(END, text)
    sh.place_forget()  # Hide the label
    e.place(x=10, y=10)

def write_text():
    if socket.gethostbyname(socket.gethostname()) == "127.0.0.1":
        msg.showerror("App", "Your device is not connected to the internet")
    else:
        e.place_forget()
        sh.place(x=10, y=10)
        t.after(100, ssk)  # Reduced delay for faster response

def speak():
    text = e.get("1.0", END).replace("\n", "")
    pyttsx3.speak(text)

def save():
    p = simpledialog.askstring("Save", "Enter filename.")
    if (p + ".txt" in os.listdir()):
        pyttsx3.speak("File with this name already exists")
        msg.showerror("Error", "File with this name already exists")
    else:
        with open(p + ".txt", "a", encoding="utf-8") as file:  # Save with UTF-8 encoding
            file.write(e.get("1.0", END))
        pyttsx3.speak("File saved successfully.")
        msg.showinfo("Success", "File saved successfully")

t = Tk()
t.geometry("1000x1000")
t.title("Speech Processing App")
t.configure(bg="#00FF00")

# Widgets
sh = Label(t, text="Say something...!", font=("Arial", 30), bg="#00FF00", fg="white")
e = Text(t, bd=4, height=18, width=80, font=("Arial", 14))

# Positioning the "Activate Microphone" button on one line with increased width
Button(t, text="Activate Microphone", command=write_text, width=35, font=("Arial", 16)).place(x=250, y=550)

# Positioning the "Speak" and "Save" buttons on the next line with an adjusted gap
Button(t, text="Speak", command=speak, width=18, font=("Arial", 16)).place(x=230, y=600)
Button(t, text="Save", command=save, width=18, font=("Arial", 16)).place(x=480, y=600)

# Positioning the text and label widgets
e.place(x=50, y=100)
sh.place(x=10, y=10)

t.mainloop()
