from tkinter import *
from time import strftime
import time
root=Tk()
root.geometry("600x400")
root.title("digitalclock")
lbl=Label(root,font=("arial",15,'bold'),background='lightblue',width=20,fg='red',bd=30)
lbl.grid(row=0,columnspan=2)

def digiclock():
    text_input=time.strftime("%H:%M:%S")
    lbl.config(text=text_input)
    lbl.after(10,digiclock)
digiclock()
lbl1=Button(root,text="TIMER",fg="blue",bg='lightpink',font=("times",15,'italic bold'),width=10,bd=20)
lbl1.grid(row=1,column=0)
lbl2=Button(root,text="STOP",fg="blue",bg='lightpink',font=("times",15,'italic bold'),width=10,bd=20)
lbl2.grid(row=1,column=1)


root.mainloop()
