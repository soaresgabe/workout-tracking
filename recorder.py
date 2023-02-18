import speech_recognition as sr
from tkinter import messagebox

class Recorder:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def record_voice(self):
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        try:
            text = self.recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            messagebox.showerror("Error", "Could not understand audio")
        except sr.RequestError as e:
            messagebox.showerror("Error", f"Request error: {e}")
