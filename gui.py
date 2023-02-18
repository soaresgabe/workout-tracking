import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

class GUI:
    def __init__(self, master, recorder):
        self.master = master
        self.recorder = recorder
        master.title("Workout Tracking APP")

        master.config(bg='#F0F0F0')
        master.attributes('-alpha', 0.9)

        master.geometry('400x600')

        self.canvas = tk.Canvas(master, width=100, height=100, bg='#F0F0F0', highlightthickness=0)
        self.canvas.pack(pady=20)

        mic_icon = Image.open('project\mic.png')
        mic_icon_resized = mic_icon.resize((50, 50), Image.ANTIALIAS)
        mic_icon_tk = ImageTk.PhotoImage(mic_icon_resized)

        self.canvas.create_image(50, 50, image=mic_icon_tk)

        self.record_button = tk.Button(master, text="Record", command=self.record_voice, bg='#64B5F6', fg='white')
        self.record_button.pack(pady=20)

    def record_voice(self):
        text = self.recorder.record_voice()
        if text:
            messagebox.showinfo("Recorded Text", text)
