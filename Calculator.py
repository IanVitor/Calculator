from tkinter import *

root = Tk()

#FUNCTIONS------>
def click_equal():
    second_number = windom.get()
    windom.delete(0, END)
    if math == "sum":
        windom.insert(0, f_number + float(second_number))
    if math == "subtration":
        windom.insert(0, f_number - float(second_number))
    if math == "division":
        windom.insert(0, f_number / float(second_number))
    if math == "multiplication":
        windom.insert(0, f_number * float(second_number))

def click_multiplication():
    first_number = windom.get()
    global f_number
    global math
    math = "multiplication"
    f_number = float(first_number)
    windom.delete(0, END)

def click_division():
    first_number = windom.get()
    global f_number
    global math
    math = "division"
    f_number = float(first_number)
    windom.delete(0, END)

def click_subtration():
    first_number = windom.get()
    global f_number
    global math
    math = "subtration"
    f_number = float(first_number)
    windom.delete(0, END)

def click_sum():
    first_number = windom.get()
    global f_number
    global math
    math = "sum"
    f_number = float(first_number)
    windom.delete(0, END)

def delete():
    windom.delete(0, END)

def click_button(number):
    actual = windom.get()
    windom.delete(0, END)
    windom.insert(END, str(actual) + str(number))

windom = Entry(root)
windom.grid(row=0, column=0, columnspan=10, ipadx=16)

#BUTTONS------->
button_9 = Button(root, text="9", height=2, width=5, command=lambda: click_button(9))
button_9.grid(row=1, column=0)

button_8 = Button(root, text="8", height=2, width=5, command=lambda: click_button(8))
button_8.grid(row=1, column=1)

button_7 = Button(root, text="7", height=2, width=5, command=lambda: click_button(7))
button_7.grid(row=1, column=2)

button_6 = Button(root, text="6", height=2, width=5, command=lambda: click_button(6))
button_6.grid(row=2, column=0)

button_5 = Button(root, text="5", height=2, width=5, command=lambda: click_button(5))
button_5.grid(row=2, column=1)

button_4 = Button(root, text="4", height=2, width=5, command=lambda: click_button(4))
button_4.grid(row=2, column=2)

button_3 = Button(root, text="3", height=2, width=5, command=lambda: click_button(3))
button_3.grid(row=3, column=0)

button_2 = Button(root, text="2", height=2, width=5, command=lambda: click_button(2))
button_2.grid(row=3, column=1)

button_1 = Button(root, text="1", height=2, width=5, command=lambda: click_button(1))
button_1.grid(row=3, column=2)

button_0 = Button(root, text="0", height=2, width=5, command=lambda: click_button(0))
button_0.grid(row=4, column=0)

button_C = Button(root, text="C", height=2, width=5, command=delete)
button_C.grid(row=4, column=1)

button_equal = Button(root, text="=", height=2, width=5, command=click_equal)
button_equal.grid(row=4, column=2)

button_sum = Button(root, text="+", height=2, width=5, command=click_sum)
button_sum.grid(row=1, column=3)

button_subtration = Button(root, text="-", height=2, width=5, command=click_subtration)
button_subtration.grid(row=2, column=3)

button_multiplication = Button(root, text="x", height=2, width=5, command=click_multiplication)
button_multiplication.grid(row=3, column=3)

button_division = Button(root, text="%", height=2, width=5, command=click_division)
button_division.grid(row=4, column=3)

root.resizable(False, False)
root.mainloop()
