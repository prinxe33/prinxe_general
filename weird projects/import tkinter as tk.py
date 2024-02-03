import tkinter as tk
from tkinter import ttk
from tkinter import *

window = tk.Tk()
window.title("Bets Expected Value")
window.geometry("600x400")

def show_values():
    print (w1.get(), w2.get())

master = Tk()
master.geometry("600x400")
w1 = Scale(master, from_=0, to=42, tickinterval=8)
w1.set(19)
w1.pack()
w2 = Scale(master, from_=0, to=200, length=600,tickinterval=10, orient=HORIZONTAL)
w2.set(23)
w2.pack()
Button(master, text='Show', command=show_values).pack()

mainloop()

window.mainloop()