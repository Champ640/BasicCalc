from tkinter import *

root = Tk()
root.title("Calculator")

# Entry widget
e = Entry(root, width=35, bd=5, state='readonly', font=('Arial', 18))
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def click(no):
    curr = e.get()
    e.config(state=NORMAL)
    e.delete(0, END)
    e.insert(0, str(curr) + no)
    e.config(state='readonly')

def clear():
    e.config(state=NORMAL)
    e.delete(0, END)
    e.config(state='readonly')

def backspace():
    curr = e.get()
    e.config(state=NORMAL)
    e.delete(0, END)
    e.insert(0, curr[:-1])
    e.config(state='readonly')

def add():
    fno = e.get()
    global fnum
    global math
    math = "add"
    fnum = float(fno)
    e.config(state=NORMAL)
    e.delete(0, END)
    e.config(state='readonly')

def sub():
    fno = e.get()
    global fnum
    global math
    math = "sub"
    fnum = float(fno)
    e.config(state=NORMAL)
    e.delete(0, END)
    e.config(state='readonly')

def mul():
    fno = e.get()
    global fnum
    global math
    math = "mul"
    fnum = float(fno)
    e.config(state=NORMAL)
    e.delete(0, END)
    e.config(state='readonly')

def div():
    fno = e.get()
    global fnum
    global math
    math = "div"
    fnum = float(fno)
    e.config(state=NORMAL)
    e.delete(0, END)
    e.config(state='readonly')

def equal():
    sno = e.get()
    e.config(state=NORMAL)
    e.delete(0, END)
    if math == "add":
        e.insert(0, fnum + float(sno))
    elif math == "sub":
        e.insert(0, fnum - float(sno))
    elif math == "mul":
        e.insert(0, fnum * float(sno))
    elif math == "div":
        if float(sno) != 0:
            e.insert(0, fnum / float(sno))
        else:
            e.insert(0, "Error")
    e.config(state='readonly')

# Number Buttons
button1 = Button(root, text='1', padx=20, pady=20, command=lambda: click("1"), font=('Arial', 14))
button2 = Button(root, text='2', padx=20, pady=20, command=lambda: click("2"), font=('Arial', 14))
button3 = Button(root, text='3', padx=20, pady=20, command=lambda: click("3"), font=('Arial', 14))
button4 = Button(root, text='4', padx=20, pady=20, command=lambda: click("4"), font=('Arial', 14))
button5 = Button(root, text='5', padx=20, pady=20, command=lambda: click("5"), font=('Arial', 14))
button6 = Button(root, text='6', padx=20, pady=20, command=lambda: click("6"), font=('Arial', 14))
button7 = Button(root, text='7', padx=20, pady=20, command=lambda: click("7"), font=('Arial', 14))
button8 = Button(root, text='8', padx=20, pady=20, command=lambda: click("8"), font=('Arial', 14))
button9 = Button(root, text='9', padx=20, pady=20, command=lambda: click("9"), font=('Arial', 14))
button0 = Button(root, text='0', padx=20, pady=20, command=lambda: click("0"), font=('Arial', 14))
buttondot = Button(root, text='.', padx=22, pady=20, command=lambda: click("."), font=('Arial', 14))

# Operation Buttons
buttonplus = Button(root, text='+', padx=20, pady=20, command=add, font=('Arial', 14), bg='lightblue')
buttonsub = Button(root, text='-', padx=22, pady=20, command=sub, font=('Arial', 14), bg='lightblue')
buttonmul = Button(root, text='*', padx=22, pady=20, command=mul, font=('Arial', 14), bg='lightblue')
buttondiv = Button(root, text='/', padx=22, pady=20, command=div, font=('Arial', 14), bg='lightblue')
buttonclear = Button(root, text='C', padx=20, pady=20, command=clear, font=('Arial', 14), bg='red')
buttonback = Button(root, text='←', padx=20, pady=20, command=backspace, font=('Arial', 14), bg='orange')
buttonequal = Button(root, text='=', padx=85, pady=20, command=equal, font=('Arial', 14), bg='lightgreen')

# Place the buttons on the grid
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
buttonplus.grid(row=1, column=3)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
buttonsub.grid(row=2, column=3)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
buttonmul.grid(row=3, column=3)

button0.grid(row=4, column=0)
buttondot.grid(row=4, column=1)
buttonback.grid(row=4, column=2)
buttondiv.grid(row=4, column=3)

buttonclear.grid(row=5, column=0)
buttonequal.grid(row=5, column=1, columnspan=3)

# Start the main event loop
root.mainloop()

