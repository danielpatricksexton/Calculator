from tkinter import *

root = Tk()

formula = ""
equation = StringVar()
equation.set("0")
# google global keyword python
calculation = Label(root, textvariable = equation)
calculation.grid(row = 0, columnspan = 4)

def pressBut(num):
    global formula
    formula = formula + str(num)
    equation.set(formula)

def equalBut():
    global formula
    result = str(eval(formula)) # eval will calculate
    equation.set(result)
    formula = ""

def clearBut():
    global formula
    formula = ""
    equation.set(formula)


# cannot print () with function or it will run right away (pressBut no ())
# you have to lambda to kinda pause the function until something is pressed
calcBut1 = Button(root, text = "1", padx = 15, pady = 15, command = lambda: pressBut(1))
calcBut1.grid(row = 1, column = 1)

calcBut2 = Button(root, text = "2", padx = 15, pady = 15, command = lambda: pressBut(2))
calcBut2.grid(row = 1, column = 2)

calcBut3 = Button(root, text = "3", padx = 15, pady = 15, command = lambda: pressBut(3))
calcBut3.grid(row = 1, column = 3)

calcBut4 = Button(root, text = "4", padx = 15, pady = 15, command = lambda: pressBut(4))
calcBut4.grid(row = 2, column = 1)

calcBut5 = Button(root, text = "5", padx = 15, pady = 15, command = lambda: pressBut(5))
calcBut5.grid(row = 2, column = 2)

calcBut6 = Button(root, text = "6", padx = 15, pady = 15, command = lambda: pressBut(6))
calcBut6.grid(row = 2, column = 3)

calcBut7 = Button(root, text = "7", padx = 15, pady = 15, command = lambda: pressBut(7))
calcBut7.grid(row = 3, column = 1)

calcBut8 = Button(root, text = "8", padx = 15, pady = 15, command = lambda: pressBut(8))
calcBut8.grid(row = 3, column = 2)

calcBut9 = Button(root, text = "9", padx = 15, pady = 15, command = lambda: pressBut(9))
calcBut9.grid(row = 3, column = 3)

calcBut0 = Button(root, text = "0", padx = 15, pady = 15, command = lambda: pressBut(0))
calcBut0.grid(row = 4, column = 1)

calcButClear = Button(root, text = "C", padx = 15, pady = 15, command = clearBut)
calcButClear.grid(row = 4, column = 2)

calcButEqual = Button(root, text = "=", padx = 15, pady = 15, command = equalBut)
calcButEqual.grid(row = 4, column = 3)

calcButDivide = Button(root, text = "/", padx = 15, pady = 15, command = lambda: pressBut("/"))
calcButDivide.grid(row = 4, column = 4)

calcButTimes = Button(root, text = "*", padx = 15, pady = 15, command = lambda: pressBut("*"))
calcButTimes.grid(row = 3, column = 4)

calcButMinus = Button(root, text = "-", padx = 15, pady = 15, command = lambda: pressBut("-"))
calcButMinus.grid(row = 2, column = 4)

calcButPlus = Button(root, text = "+", padx = 15, pady = 15, command = lambda: pressBut("+"))
calcButPlus.grid(row = 1, column = 4)

root.geometry("500x500")
root.mainloop()

# 30 days html
