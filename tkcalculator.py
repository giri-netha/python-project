from tkinter import *
root=Tk()
root.geometry("400x320")
root.title("calculator")
e=Entry(root,font=20,width=50,borderwidth=4,justify=RIGHT)
e.grid(row=0,column=0,columnspan=3,padx=40,pady=10)
def click(number):
	# e.delete(0,END)
	e.insert(END,number)
def click_clear():
	e.delete(0,END)

first_num=0
second_num=0
math=""
def click_get(mathtype):
	global first_num,math
	math=mathtype
	first_num=e.get()
	click_clear()
def click_sub():
	global first_num
	first_num=e.get()
	click_clear()

def click_equal():
	second_num=e.get()
	click_clear()
	if math=='add':
		res=int(first_num)+int(second_num)
		e.insert(0,res)
	elif math=='sub':
		res=int(first_num)-int(second_num)
		e.insert(0,res)
	elif math=='div':
		res=int(first_num)/int(second_num)
		e.insert(0,res)
	elif math=='mul':
		res=int(first_num)*int(second_num)
		e.insert(0,res)
button=Button(root,text="9",font=20,borderwidth=3,width=9,height=4,padx=20,pady=10,command=lambda:click(9))
button1=Button(root,text="8",font=20,borderwidth=5,width=9,height=4,padx=20,pady=10,command=lambda:click(8))
button2=Button(root,text="7",font=20,borderwidth=5,width=9,height=4,padx=20,pady=10,command=lambda:click(7))
button3=Button(root,text="6",font=20,borderwidth=5,width=9,height=4,padx=20,pady=10,command=lambda:click(6))
button4=Button(root,text="5",font=20,borderwidth=5,width=9,height=4,padx=20,pady=10,command=lambda:click(5))
button5=Button(root,text="4",font=20,borderwidth=5,width=9,height=4,padx=20,pady=10,command=lambda:click(4))
button6=Button(root,text="3",font=20,borderwidth=5,width=9,height=4,padx=20,pady=10,command=lambda:click(3))
button7=Button(root,text="2",font=20,borderwidth=5,width=9,height=4,padx=20,pady=10,command=lambda:click(2))
button8=Button(root,text="1",font=20,borderwidth=5,width=9,height=4,padx=20,pady=10,command=lambda:click(1))
button9=Button(root,text="0",font=20,borderwidth=5,width=9,height=4,padx=20,pady=10,command=lambda:click(0))
button_clear=Button(root,text="clear",borderwidth=5,font=20,width=9,height=4,padx=20,pady=10,command=lambda:click_clear())
button_equal=Button(root,text="=",font=20,borderwidth=5,width=9,height=4,padx=20,pady=10,command=lambda:click_equal())
button_add=Button(root,text="+",font=20,borderwidth=5,width=19,height=4,padx=20,pady=10,command=lambda:click_get('add'))
button_sub=Button(root,text="-",font=20,borderwidth=5,width=9,height=4,padx=20,pady=10,command=lambda:click_get('sub'))
button_div=Button(root,text="/",font=20,borderwidth=5,width=9,height=4,padx=20,pady=10,command=lambda:click_get('div'))
button_mul=Button(root,text="x",font=20,borderwidth=5,width=9,height=4,padx=20,pady=10,command=lambda:click_get('mul'))


button.grid(row=1,column=0)
button1.grid(row=1,column=1)
button2.grid(row=1,column=2)
button3.grid(row=2,column=0)
button4.grid(row=2,column=1)
button5.grid(row=2,column=2)
button6.grid(row=3,column=0)
button7.grid(row=3,column=1)
button8.grid(row=3,column=2)
button9.grid(row=4,column=0)
button_clear.grid(row=4,column=1)
button_equal.grid(row=4,column=2)
button_add.grid(row=6,columnspan=3)
button_sub.grid(row=5,column=0)
button_div.grid(row=5,column=1)
button_mul.grid(row=5,column=2)

root.mainloop()
