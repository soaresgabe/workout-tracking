import tkinter as tk
from gui import GUI
from recorder import Recorder

if __name__ == '__main__':
    recorder = Recorder()
    root = tk.Tk()

    gui = GUI(root, recorder)

    root.mainloop()