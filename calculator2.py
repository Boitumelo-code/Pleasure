from tkinter import*

def button_click(number):
    current = ent.get()
    
    entry.insert(0, str(current) + str(number))
def button_clear():
    entry.delete(0, Tk.END)

def button_add():
    first_number = entry.get()
    global f_num
    f_num = int(first_number)
    entry.delete(0, Tk.END)

def button_equal():
    second_number = entry.get()
    entry.delete(0, Tk.END)
    entry.insert(0, f_num + int(second_number))

window = Tk()
window.title("Calculator")

ent =Entry(window, width=35, borderwidth=5)
ent.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

but_click1 = Button(window, text="1", padx=40, pady=20, command=lambda: button_click(1))
but_click2 = Button(window, text="2", padx=40, pady=20, command=lambda: button_click(2))
but_click3 = Button(window, text="3", padx=40, pady=20, command=lambda: button_click(3))
but_click4 = Button(window, text="4", padx=40, pady=20, command=lambda: button_click(4))
but_click5 = Button(window, text="5", padx=40, pady=20, command=lambda: button_click(5))
but_click6 = Button(window, text="6", padx=40, pady=20, command=lambda: button_click(6))
but_click7 = Button(window, text="7", padx=40, pady=20, command=lambda: button_click(7))
but_click8 = Button(window, text="8", padx=40, pady=20, command=lambda: button_click(8))
but_click9 = Button(window, text="9", padx=40, pady=20, command=lambda: button_click(9))
but_click0 = Button(window, text="0", padx=40, pady=20, command=lambda: button_click(0))

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

window.mainloop()



