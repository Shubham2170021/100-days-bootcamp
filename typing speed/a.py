from tkinter import *
import time
import threading
import random
class SpeedTypeGUI:
    def __init__(self):
        self.root = Tk()
        self.wpm = 0
        self.cpm = 0
        self.root.title("Typing Speed Test")
        self.root.geometry("800x300")
        self.counter = 0

        self.text = open('text.txt', 'r').read().split('\n')
        self.words = random.choice(self.text)

        self.label_frame = Frame(self.root, width=100, height=10, pady=1)
        self.text_frame = Frame(self.root, bg='gray', width=400, height=150, pady=1)
        self.entry_frame = Frame(self.root)

        # layout all of the main containers
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.label_frame.grid(row=0)
        self.text_frame.grid(row=1)
        self.entry_frame.grid(row=2)

        # Label Frame

        self.wpm_label = Label(self.label_frame, text=f'WPM: {self.wpm}', font=('Arial', 11))
        self.wpm_label.grid(row=0, column=0, padx=15)

        self.cpm_label = Label(self.label_frame, text=f'CPM: {self.cpm}', font=('Arial', 11))
        self.cpm_label.grid(row=0, column=1, padx=15)

        self.time_label = Label(self.label_frame, text=f"Time: {self.counter}", font=('Arial', 11))
        self.time_label.grid(row=0, column=2, padx=15)

        # Words Frame

        self.word_window = Label(self.text_frame, text=self.words, font=('Arial', 15))
        self.word_window.grid(row=0, column=0, ipadx=100, ipady=55, padx=15, pady=2)

        self.word_entry = Entry(self.entry_frame, font=('Arial', 13))
        self.word_entry.grid(row=0, column=0, ipadx=100, ipady=15)
        self.word_entry.bind('<KeyPress>', self.start)

        self.restart_button = Button(self.entry_frame, text='Restart', command=self.restart)
        self.restart_button.grid(row=1, column=0, pady=3)

        # adding the boolean to know that the app is started or not
        self.running = False

        self.root.mainloop()

    def start(self, event):
        if not self.running:
            if not event.keycode in [16, 17, 18]:
                self.running = True
                t = threading.Thread(target=self.time_thread)
                t.start()

        if not self.word_window.cget('text').startswith(self.word_entry.get()):
            self.word_entry.config(fg='red')

        else:
            self.word_entry.config(fg='black')

        if self.word_entry.get() == self.word_window.cget('text')[:-1]:
            self.running = False
            self.word_entry.config(fg='green')

    def time_thread(self):
        while self.running:
            time.sleep(.1)
            self.counter += 0.1
            cps = len(self.word_entry.get()) / self.counter
            self.cpm = round(float(cps) * 60, 2)
            wps = len(self.word_entry.get().split(" ")) / self.counter
            self.wpm = round(float(wps) * 60, 2)
            self.cpm_label.config(text=f'CPM: {self.cpm}')
            self.wpm_label.config(text=f'WPM: {self.wpm}')
            self.time_label.config(text=f"Time: {int(self.counter)} secs")

    def restart(self):
        self.running = False
        self.counter = 0
        self.cpm = 0
        self.wpm = 0
        self.words = random.choice(self.text)
        self.word_window.config(text=self.words)
        self.word_entry.delete(0, END)


SpeedTypeGUI()