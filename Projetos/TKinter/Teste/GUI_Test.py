from tkinter import *

root = Tk()

root.title("Teste de GUI com Tkinter")
root.geometry("400x300")

menu = Menu(root)
item = Menu(menu)
item.add_command(label="Novo")
menu.add_cascade(label="Arquivo", menu=item)
root.config(menu=menu)

lbl = Label(root, text="Olá, Tkinter!")
lbl.grid()

txt = Entry(root, width=20)
txt.grid(column=0, row=1)


def clicked(): 
    res = "Você digitou: " + txt.get()
    lbl.configure(text=res)
    
btn = Button(root, text = "Clique-me!", fg="red", command=clicked)

btn.grid(column=0)


root.mainloop()