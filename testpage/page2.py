from tkinter import *
import subprocess

win = Tk()
win.geometry('1080x610')
win.title('NES')
win['bg']='#ffbf00'
f = ("Times bold", 14)

 
def back():
    win.destroy()
    subprocess.call(["python","testpage/homepage.py"])

Label(
    win,
    text="This is Second page",
    padx=20,
    pady=20,
    bg='#ffbf00',
    font=f
).pack(expand=True, fill=BOTH)

Button(
    win, 
    text="back", 
    font=f,
    command=back
    ).pack(fill=X, expand=NO, side=LEFT)


win.mainloop()