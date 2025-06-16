from tkinter import *

expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)
    
def equal_press():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("Erro")
        expression = ""
        
def clear():
    global expression
    expression = ""
    equation.set("")

if __name__ == "__main__":
    root = Tk()
    root.title("Calculadora")
    root.geometry("400x300")

    equation = StringVar()

    expression_field = Entry(root, textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=70)

    btn1 = Button(root, text="1", command=lambda: press(1), width=5)
    btn1.grid(row=1,column=0)
    btn2 = Button(root, text="2", command=lambda: press(2), width=5)
    btn2.grid(row=1,column=1)
    btn3 = Button(root, text="3", command=lambda: press(3), width=5)
    btn3.grid(row=1,column=2)
    btn4 = Button(root, text="4", command=lambda: press(4), width=5)
    btn4.grid(row=2,column=0)
    btn5 = Button(root, text="5", command=lambda: press(5), width=5)
    btn5.grid(row=2,column=1)
    btn6 = Button(root, text="6", command=lambda: press(6), width=5)
    btn6.grid(row=2,column=2)
    btn7 = Button(root, text="7", command=lambda: press(7), width=5)
    btn7.grid(row=3,column=0)
    btn8 = Button(root, text="8", command=lambda: press(8), width=5)
    btn8.grid(row=3,column=1)
    btn9 = Button(root, text="9", command=lambda: press(9), width=5)
    btn9.grid(row=3,column=2)
    btn0 = Button(root, text="0", command=lambda: press(0), width=5)
    btn0.grid(row=4,column=1)

    btn_plus = Button(root, text="+", command=lambda: press("+"), width=5)
    btn_plus.grid(row=1,column=3)

    btn_minus = Button(root, text="-", command=lambda: press("-"), width=5)
    btn_minus.grid(row=2,column=3)

    btn_multiply = Button(root, text="*", command=lambda: press("*"), width=5)
    btn_multiply.grid(row=3,column=3)

    btn_divide = Button(root, text="/", command=lambda: press("/"), width=5)
    btn_divide.grid(row=4,column=3)

    btn_equal = Button(root, text="=", command=equal_press, width=5)
    btn_equal.grid(row=5,column=2)

    btn_clear = Button(root, text="C", command=clear, width=5)
    btn_clear.grid(row=5,column=1)

    btn_decimal = Button(root, text=".", command=lambda: press("."), width=5)
    btn_decimal.grid(row=5,column=0)

    root.mainloop()