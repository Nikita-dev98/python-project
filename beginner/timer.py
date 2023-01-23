import time
import tkinter as tk
from tkinter import *
from datetime import datetime
import win10toast
import winsound

# GUI window creation
window = Tk()
window.geometry('500x500')
header = Label(window, text="countdown clock and timer", font=("Calibri 15"))
header.pack()  # leaving the attriutes empty

# displaying the current time
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
Label(window,text=current_time).pack()

check = tk.BooleanVar()
hour = tk.IntVar()
minute = tk.IntVar()
sec = tk.IntVar()

# create countdown and timer function
def countdown():
    h = hour.get()
    m = minute.get()
    s = sec.get() 
    t = h*3600 + m*60 + s
    while t:
        mins, secs = divmod(t,60)
        display = ('{:02d}:{:02d}'.format(mins, secs))
        time.sleep(1)
        t-=1
        Label(window,text=display).pack()
    
    if (check.get()==True):
        winsound.Beep(440, 1000) #beep sound
    
    Label(window,text="Time-up",font=('bold',20)).place(x=250,y=230)
    # adding desktop notification
    toast = win10toast.ToastNotifier()
    toast.show_toast("Notification","Timer is Off",duration = 20,icon_path = NONE,threaded = True)

Label(window,text="Enter time in HH:MM:SS",font=('bold')).pack()
Entry(window,textvariable=hour,width=30).pack()
Entry(window,textvariable=minute,width=30).pack()
Entry(window,textvariable=sec,width=30).pack()

Checkbutton(text='Check for music',onvalue=True,variable=check).pack()
Button(window,text='Set countdown',command=countdown,bg="yellow").place(x=250,y=230)


window.update()
window.mainloop()