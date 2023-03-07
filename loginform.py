from tkinter import *
root=Tk()
root.geometry("600x400")
root.title("registration form")
labl1=Label(root,text='enter name')
labl1.grid(row=0,column=0)
entry1=Entry(root,width=20)
entry1.grid(row=0,column=1)
labl2=Label(root,text='password')
labl2.grid(row=1,column=0)
labl3=Label(root,text='confirm password')
labl3.grid(row=3,column=0)

a=StringVar()
b=StringVar()


def onclick():
    x=entry2.get()
    y=entry3.get()
    if x==y:
        label3=Label(root,text='register successfully',width=15,fg='green',font='arial')
        label3.grid(row=4,columnspan=2)
    else:
        label4=Label(root,text='register unsuccessfull',width=15,fg='red',font='arial')
        label4.grid(row=4,columnspan=2)


entry3=Entry(root,textvariable=a,width=20)
entry3.grid(row=3,column=1)

entry2=Entry(root,textvariable=b,width=20)
entry2.grid(row=1,column=1)
b=Button(root,text='ENTER',width=15,bg='lightgreen',command=onclick)
b.grid(row=5,columnspan=2)
root.mainloop()
