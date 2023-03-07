from tkinter import *
from time import strftime
import time
root=Tk()
root.geometry("600x400")
root.title("digitalclock")
lbl=Label(root,font=("arial",15,'bold'),background='lightblue',width=20,fg='red',bd=30)
lbl.grid(row=0,columnspan=3)

def digiclock():
    text_input=time.strftime("%H:%M:%S")
    lbl.config(text=text_input)
    lbl.after(10,digiclock)
digiclock()
# lbl1=Button(root,text="TIMER",fg="blue",bg='lightpink',font=("times",15,'italic bold'),width=10,bd=20)
# lbl1.grid(row=1,column=0)
# lbl2=Button(root,text="STOP",fg="blue",bg='lightpink',font=("times",15,'italic bold'),width=10,bd=20)
# lbl2.grid(row=1,column=1)

# def countdown1(t):
#         mins, secs = divmod(t, 60)
#         timer = ('{:02d}:{:02d}'.format(mins, secs))
#         lbl3=Label(root,fg="blue",bg='lightpink',font=("times",15,'italic bold'),width=10,bd=20)
#         lbl3.grid(row=2,column=0)
#         lbl3.config(text=timer)
# countdown1(5)
hour=StringVar()
min=StringVar()
sec=StringVar()

hour.set("00")
min.set("00")
sec.set("00")

hourentry=Entry(root,width=8,font=("arial",18,""),textvariable=hour)
hourentry.grid(row=2,column=0)
minentry=Entry(root,width=8,font=("arial",18,""),textvariable=min)
minentry.grid(row=2,column=1)
secentry=Entry(root,width=8,font=("arial",18,""),textvariable=sec)
secentry.grid(row=2,column=2)
def submit():
    try:
        temp=int(hour.get())*3600+int(min.get())*60+int(sec.get())
    except:
        print("please input the right value")
    while temp>0:
        mins,secs=divmod(temp,60)
        hour=0
        if mins>60:
            hours,mins=divmod(mins,60)

        hour.set("{0:2d}".format(hours))
        min.set("{0:2d}".format(mins))
        sec.set("{0:2d}".format(sec))

        root.update()
        time.sleep(1)
        if (temp==0):
            messagebox.showinfo("time countdown","Time's up")

btn=Button(root,text="Time countdown",width=15,command=submit,bg="lightyellow")
btn.grid(row=3,columnspan=3)
root.mainloop()
