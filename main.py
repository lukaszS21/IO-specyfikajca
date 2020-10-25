# Python program to  create a simple GUI  
# calculator using Tkinter 

# import everything from tkinter module 
from tkinter import *
import tkinter as tk
import tkinter.font as tkfont
# globally declare the expression variable 
expression = ""


# Function to update expressiom 
# in the text entry box 
def press(num):
    # point out the global expression variable 
    global expression

    # concatenation of string 
    expression = expression + str(num)

    # update the expression by using set method 
    equation.set(expression)


# Function to evaluate the final expression
def sprawdz():
    global expression
    print(len(expression))
    if len(expression)>10:
        equation.set(" error ")
        expression = ""
    else:
        pass
def equalpress():
    # Try and except statement is used 
    # for handling the errors like zero 
    # division error etc. 

    # Put that code inside the try block 
    # which may generate the error 
    try:

        global expression
        sprawdz()
        # eval function evaluate the expression
        # and str function convert the result
        # into string
        total = str(eval(expression))

        equation.set(total)

        # initialze the expression variable
        # by empty string
        expression = ""
        print("tu2")
        # if error is generate then handle
    # by the except block 
    except:

        equation.set(" error ")
        expression = ""
        print("tu")

    # Function to clear the contents




# of text entry box
def clear():
    global expression
    expression = ""
    equation.set("")

mycolor = '#%02x%02x%02x' % (64, 204, 208)
# Driver code 
if __name__ == "__main__":
    # create a GUI window 
    gui = Tk()

    # set the background colour of GUI window 
    gui.configure(background="light blue")

    # set the title of GUI window 
    gui.title("Kalkulator")

    # set the configuration of GUI window 
    gui.geometry("270x300")

    # StringVar() is the variable class 
    # we create an instance of this class 
    equation = StringVar()

    # create the text entry box for 
    # showing the expression . 
    expression_field = Entry(gui, textvariable=equation)

    # grid method is used for placing 
    # the widgets at respective positions 
    # in table like structure . 
    expression_field.grid(columnspan=4,pady=5,padx=74)

    equation.set(' wprowadz wyrażenie')
    # create a Buttons and place at a particular 
    # location inside the root window . 
    # when user press the button, the command or 
    # function affiliated to that button is executed . 
    button1 = Button(gui, text=' 1 ', fg='black', bg=mycolor ,
                     command=lambda: press(1),height=3, width=8)
    button1.grid(row=2, column=0)


    button2 = Button(gui, text=' 2 ', fg='black', bg=mycolor,
                  command=lambda: press(2), height=3, width=8)
    button2.grid(row=2, column=1)

    button3 = Button(gui, text=' 3 ', fg='black', bg=mycolor ,
                     command=lambda: press(3), height=3, width=8)
    button3.grid(row=2, column=2)

    button4 = Button(gui, text=' 4 ', fg='black', bg=mycolor ,
                     command=lambda: press(4), height=3, width=8)
    button4.grid(row=3, column=0)

    button5 = Button(gui, text=' 5 ', fg='black', bg=mycolor ,
                     command=lambda: press(5), height=3, width=8)
    button5.grid(row=3, column=1)

    button6 = Button(gui, text=' 6 ', fg='black', bg=mycolor ,
                     command=lambda: press(6), height=3, width=8)
    button6.grid(row=3, column=2)

    button7 = Button(gui, text=' 7 ', fg='black', bg=mycolor ,
                     command=lambda: press(7), height=3, width=8)
    button7.grid(row=4, column=0)

    button8 = Button(gui, text=' 8 ', fg='black', bg=mycolor ,
                     command=lambda: press(8), height=3, width=8)
    button8.grid(row=4, column=1)

    button9 = Button(gui, text=' 9 ', fg='black', bg=mycolor ,
                     command=lambda: press(9), height=3, width=8)
    button9.grid(row=4, column=2)

    button0 = Button(gui, text=' 0 ', fg='black', bg=mycolor ,
                     command=lambda: press(0), height=3, width=8)
    button0.grid(row=5, column=0)

    plus = Button(gui, text=' + ', fg='black', bg=mycolor ,
                  command=lambda: press("+"), height=3, width=8)
    plus.grid(row=2, column=3)

    minus = Button(gui, text=' - ', fg='black', bg=mycolor ,
                   command=lambda: press("-"), height=3, width=8)
    minus.grid(row=3, column=3)

    multiply = Button(gui, text=' * ', fg='black', bg=mycolor ,
                      command=lambda: press("*"), height=3, width=8)
    multiply.grid(row=4, column=3)

    divide = Button(gui, text=' / ', fg='black', bg=mycolor ,
                    command=lambda: press("/"), height=3, width=8)
    divide.grid(row=5, column=3)

    equal = Button(gui, text=' = ', fg='black', bg=mycolor ,
                   command=equalpress, height=3, width=8)
    equal.grid(row=5, column=2)

    clear = Button(gui, text='Clear', fg='black', bg=mycolor ,
                   command=clear, height=3, width=8)
    clear.grid(row=5, column='1')

    Decimal = Button(gui, text='.', fg='black', bg=mycolor ,
                     command=lambda: press('.'), height=3, width=8)
    Decimal.grid(row=6, column=0)
    procent = Button(gui, text='%', fg='black', bg=mycolor ,
                     command=lambda:press('%'), height=3, width=8)
    procent.grid(row=6, column=1)
    nawias1 = Button(gui, text='(', fg='black', bg=mycolor ,
                     command=lambda: press('('), height=3, width=8)
    nawias1.grid(row=6, column=2)
    nawias2 = Button(gui, text=')', fg='black', bg=mycolor ,
                     command=lambda: press(')'), height=3, width=8)
    nawias2.grid(row=6, column=3)
    # start the GUI

    gui.mainloop() 