from tkinter import *

import calendar

def showCal():
    
    root2 = Tk()
    root2.title("Calendário")
    root2.geometry("550x600")
    
    fetch_year = int(year_field.get())
    cal_content = calendar.calendar(fetch_year)
    cal_year = Label(root2, text = cal_content, font = "Consolas 10 bold")
    cal_year.grid(row=5, column=1, padx=20)
    
    root2.mainloop()
    
if __name__ == "__main__":
    root = Tk()
    
    root.title("Calendário")
    root.geometry("250x140")
    
    cal = Label(root, text="Calendário", font=("Helvetica", 28, "bold"))
    year = Label(root, text="Digite o ano")
    year_field = Entry(root)
    
    show = Button(root, text="Mostrar Calendário", fg="Black", bg="Red", command=showCal)
    
    Exit = Button(root, text="Sair", fg="Black", bg="Red", command = exit)
    
    cal.grid(row=1, column=1)
    year.grid(row=2, column=1)
    year_field.grid(row=3, column=1)
    show.grid(row=4, column=1)
    Exit.grid(row=6, column=1)
    
    root.mainloop()
    
    