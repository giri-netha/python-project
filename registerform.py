from tkinter import *
root=Tk()
root.geometry("600x800")
root.title("registrationform")
lbl1=Label(root,text="Name",font=("arial",10,'bold'),width=8,bg="lightyellow",fg="red")
lbl1.grid(row=0,column=0)
entry1=Entry(root,width=15)
entry1.grid(row=0,column=1)

lbl2=Label(root,text="Surname",font=("arial",10,'bold'),width=8,bg="lightyellow",fg="red")
lbl2.grid(row=1,column=0)
entry2=Entry(root,width=15)
entry2.grid(row=1,column=1)

lbl3=Label(root,text="gender",font=("arial",10,'bold'),width=8,bg="lightyellow",fg="red")
lbl3.grid(row=2,column=0)
lbl4=Label(root,text="selcted",font=("arial",10,'bold'),width=8,bg="lightyellow",fg="red")
lbl4.grid(row=2,column=3)

def select():
    selection=str(var.get())
    lbl4.config(text=selection)

var=StringVar()

r1=Radiobutton(root,text="Male",variable=var,value="Male",command=select)
r1.grid(row=2,column=1)
r1=Radiobutton(root,text="Female",variable=var,value="Female",command=select)
r1.grid(row=3,column=1)

lbl5=Label(root,text="Languages",font=("arial",10,'bold'),width=8,bg="lightyellow",fg="red")

lbl5.grid(row=4,column=0)

btn1=Checkbutton(root,text="Python")
btn1.grid(row=4,column=1)
btn2=Checkbutton(root,text="Java")
btn2.grid(row=5,column=1)
btn3=Checkbutton(root,text="C++")
btn3.grid(row=6,column=1)

def call():
    lbl7=Label(root,text="register successfully",width=15,font=("arial",10,'bold'))
    lbl7.grid(row=8,columnspan=3)
    lbl7.config()

lbl6=Button(root,text="SUBMIT",font=("arial",10,'bold'),relief=SUNKEN,width=8,bg="GREEN",fg="BLUE",command=call)
lbl6.grid(row=7,column=1) 



root.mainloop()
