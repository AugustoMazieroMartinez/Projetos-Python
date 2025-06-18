from tkinter import *

root = Tk()
root.title("Weight Conversion")
root.geometry("400x300")

def from_kilo():
    try:
        kg = float(e2_value.get())
        grams = kg * 1000
        pounds = kg * 2.20462
        ounces = kg * 35.274
        print(kg, grams, pounds, ounces)
        t1.delete("1.0", END)
        t1.insert(END, grams)

        t2.delete("1.0", END)
        t2.insert(END, pounds)

        t3.delete("1.0", END)
        t3.insert(END, ounces)
    except ValueError:
        t1.delete("1.0", END)
        t2.delete("1.0", END)
        t3.delete("1.0", END)
        t1.insert(END, "Invalid input")
        t2.insert(END, "Invalid input")
        t3.insert(END, "Invalid input")

e1 = Label(root, text="Enter weight in kilograms: ").grid(row=0, column=0, padx=10, pady=10)
e2_value = StringVar()
e2 = Entry(root, textvariable=e2_value).grid(row=0, column=1, padx=10, pady=10)
b1 = Button(root, text="Convert: ", command=from_kilo).grid(row=0, column=2, padx=10, pady=10)
e3 = Label(root, text="Grams").grid(row=1, column=0, padx=10, pady=10)
e4 = Label(root, text="Pounds").grid(row=1, column=1, padx=10, pady=10)
e5 = Label(root, text="Ounces").grid(row=1, column=2, padx=10, pady=10)

t1 = Text(root, height=1, width=20)
t1.grid(row=2, column=0, padx=10, pady=10)
t2 = Text(root, height=1, width=20)
t2.grid(row=2, column=1, padx=10, pady=10)
t3 = Text(root, height=1, width=20)
t3.grid(row=2, column=2, padx=10, pady=10)

root.mainloop()