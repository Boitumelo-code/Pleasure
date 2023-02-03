from tkinter import*

window = Tk()
window.title("Calculator")
ent = Entry(window, width=30,borderwidth=10)
ent.grid(column=0, row=0,columnspan=3,pady=10,padx=10)
window.geometry('300x350')
equation = StringVar()

mycee = " "

def click(number):
    current = ent.get()
    ent.delete(0,END)
    ent.insert(0, str(current) + str(number))

def clear():
   ent.delete(0,END)
    

def add():
    first_number = ent.get()
    global f_num
    f_num = int(first_number)
    ent.delete(0,END)

def equal():
    try:
        y=str(eval(ent.get()))
        ent.delete(0,END)
        ent.insert(0,y)
    except:
            tkinter.messagebox.showinfo("Error", "Syntax Error")


    



    
but_click0 = Button(window,text='0', padx=40, pady=20,command=lambda:click(0))
but_click1 = Button(window,text='1', padx=40, pady=20,command=lambda:click(1))
but_click2 = Button(window,text='2', padx=40, pady=20,command=lambda:click(2))
but_click3 = Button(window,text='3', padx=40, pady=20,command=lambda:click(3))

but_click4 = Button(window,text='4', padx=40, pady=20,command=lambda:click(4))
but_click5 = Button(window,text='5', padx=40, pady=20,command=lambda:click(5))
but_click6 = Button(window,text='6', padx=40, pady=20,command=lambda:click(6))
but_click7 = Button(window,text='7', padx=40, pady=20,command=lambda:click(7))

but_click8 = Button(window,text='8', padx=40, pady=20,command=lambda:click(8))
but_click9 = Button(window,text='9', padx=40, pady=20,command=lambda:click(9))

but_clickAdd = Button(window,text='+', padx=40, pady=20,command=lambda:click("+"))
but_clickEqual = Button(window,text='=', padx=40, pady=20,command=(equal))
but_clickClear= Button(window,text='clear', padx=40, pady=20,command=clear)
but_clickSub= Button(window,text='-', padx=40, pady=20,command=lambda:click('-'))
but_clickDiv= Button(window,text='/', padx=40, pady=20,command=lambda:click('/'))
but_clickMulti = Button(window,text='*', padx=40, pady=20,command=lambda:click('*'))



but_click1.grid(column=1, row=3)
but_click2.grid(column=2, row=3)
but_click3.grid(column=3, row=3)

but_click4.grid(column=1, row=2)
but_click5.grid(column=2, row=2)
but_click6.grid(column=3, row=2)

but_click7.grid(column=1, row=1)
but_click8.grid(column=2, row=1)
but_click9.grid(column=3, row=1)

but_click0.grid(column=1, row=4)

but_clickAdd.grid(column=5,row=1)
but_clickEqual.grid(column=3,row=4)
but_clickClear.grid(column=2,row=4)
but_clickDiv.grid(column=1,row=5)
but_clickSub.grid(column=2,row=5)
but_clickMulti.grid(column=3,row=5)



   
window.mainloop()


