from tkinter import *
from PIL import Image, ImageTk
from Lista import Lista as ls

def forward():
    global label, button_forward, button_back, button_exit, current
    current = current.next
    label.grid_forget()
    label = Label(image = current.value)
    label.grid(row=1, column=0, columnspan=3)
    button_forward = Button(root, text="Forward", command=forward)

    if current.next is None:
        button_forward = Button(root, text="Forward", state=DISABLED)
    button_back = Button(root, text="Back", command=back)
    
    button_back.grid(row=5, column=0)
    button_exit.grid(row=5, column=1)
    button_forward.grid(row=5, column=2)


def back():
    global label, button_back, button_forward, button_exit, current
    label.grid_forget()
    current = current.prev
    label = Label(image = current.value)
    label.grid(row=1, column=0, columnspan=3)
    button_back = Button(root, text="Back", command=back)

    if current.prev is None:
        button_back = Button(root, text="Back", state=DISABLED)
        
    button_forward = Button(root, text="forward", command=forward)

    label.grid(row=1, column=0, columnspan=3)
    button_back.grid(row=5, column=0)
    button_exit.grid(row=5, column=1)
    button_forward.grid(row=5, column=2)
    

root = Tk()
root.title("Image Viewer")
root.geometry()
lista = ls()
lista.append(ImageTk.PhotoImage(Image.open("C:\\Users\\augus\\Downloads\\Recoiless_Rifle.png")))
lista.append(ImageTk.PhotoImage(Image.open("C:\\Users\\augus\\Downloads\\Orbital_380mm_Barrage.png")))
lista.append(ImageTk.PhotoImage(Image.open("C:\\Users\\augus\\Downloads\\Eagle_500KG_Bomb.png")))
lista.append(ImageTk.PhotoImage(Image.open("C:\\Users\\augus\\Downloads\\Portable_Hellbomb.png")))
current = lista.head

label = Label(image = current.value)

label.grid(row=1, column=0, columnspan=3)

button_back = Button(root, text="Back", command=back, state=DISABLED)

button_exit = Button(root, text="Exit", command=root.quit)

button_forward = Button(root, text="Forward", command=forward)
button_back.grid(row=5, column=0)
button_exit.grid(row=5, column=1)
button_forward.grid(row=5, column=2)

root.mainloop()