from tkinter import *
from PIL import ImageTk, Image
import subprocess
from firebase_admin import credentials
from firebase_admin import firestore
import firebase_admin
cred = credentials.Certificate("retrostock-project-firebase-adminsdk-upta5-aaead3d509.json")
firebase_admin.initialize_app(cred)
db=firestore.client()

win = Tk()
win.geometry('1080x610')
win.title('PythonGuides')
win['bg']='#ccff99'

def close():
    doc=db.collection('currentUser').get()
    for docs in doc :
        db.collection('currentUser').document(docs.id).delete()
    win.destroy()

win.protocol("WM_DELETE_WINDOW", close)

def snes():
    win.destroy()
    subprocess.call(["python","selectgame/snes.py"])    

def nes():
    win.destroy()
    subprocess.call(["python","selectgame/nes.py"])

def gba():
    win.destroy()
    subprocess.call(["python","selectgame/gba.py"])

label1=Label(win,text="HOME",padx=1080,pady=15,font=90,bg="#ff9966")#.grid(row=0,column=0)
label1.pack()

bt1=Button(win,text="SNES",height=2,width=15,command=snes)#.grid(row=4,column=1)
bt1.pack(side=LEFT,expand=YES)

bt2=Button(win,text="NES",height=2,width=15,command=nes)#.grid(row=4,column=2)
bt2.pack(side=LEFT,expand=YES)

bt3=Button(win,text="GBA",height=2,width=15,command=gba)#.grid(row=4,column=3)
bt3.pack(side=LEFT,expand=YES)



win.mainloop()    


    