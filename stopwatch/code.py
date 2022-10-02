from tkinter import *
from tkinter.ttk import *
from time import strftime
root=Tk()
root.title("clock")
label=Label(root,font=("ds-digital", 80),background="black",foreground="blue")
label.pack(anchor="center")
def gettime():
    t=strftime('%H %M %S : %p')
    label.config(text=t)
    label.after(1000, gettime)
gettime()
root.mainloop()