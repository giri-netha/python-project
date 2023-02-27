from tkinter import *
from time import strftime
import time
root=Tk()
root.geometry("600x400")
root.title("digitalclock")
lbl=Label(root,font=("arial",15,'bold'),background='lightblue',fg='red',bd=30)
lbl.grid(row=0,column=1)

def digiclock():
    text_input=time.strftime("%H:%M:%S")
    lbl.config(text=text_input)
    lbl.after(10,digiclock)
digiclock()

root.mainloop()
