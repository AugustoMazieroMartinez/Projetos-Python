from tkinter import *
from PIL import Image, ImageTk

def forward(image_no):
    global label, button_forward, button_back, button_exit
    
    label.grid_forget()
    label = Label(image=list_images[image_no])
    
    label.grid(row=1, column=0, columnspan=3)
    button_forward = Button(root, text="Forward", command=lambda: forward(image_no + 1))
    
    if image_no == len(list_images) - 1:
        button_forward = Button(root, text="Forward", state=DISABLED)
        
    button_back = Button(root, text="Back", command=lambda: back(image_no - 1))
    
    button_back.grid(row=5, column=0)
    button_exit.grid(row=5, column=1)
    button_forward.grid(row=5, column=2)


def back(img_no):
    global label
    global button_forward
    global button_back
    global button_exit
    label.grid_forget()

    label = Label(image=list_images[img_no - 1])
    label.grid(row=1, column=0, columnspan=3)
    button_forward = Button(root, text="forward",
                            command=lambda: forward(img_no + 1))
    button_back = Button(root, text="Back",
                         command=lambda: back(img_no - 1))

    if img_no == 1:
        button_back = Button(root, text="Back", state=DISABLED)

    label.grid(row=1, column=0, columnspan=3)
    button_back.grid(row=5, column=0)
    button_exit.grid(row=5, column=1)
    button_forward.grid(row=5, column=2)
    

root = Tk()
root.title("Image Viewer")
root.geometry()

image_01 = ImageTk.PhotoImage(Image.open("C:\\Users\\augus\\Downloads\\Recoiless_Rifle.png"))
image_02 = ImageTk.PhotoImage(Image.open("C:\\Users\\augus\\Downloads\\Orbital_380mm_Barrage.png"))
image_03 = ImageTk.PhotoImage(Image.open("C:\\Users\\augus\\Downloads\\Eagle_500KG_Bomb.png"))
image_04 = ImageTk.PhotoImage(Image.open("C:\\Users\\augus\\Downloads\\Portable_Hellbomb.png"))

list_images = [image_01, image_02, image_03, image_04]

label = Label(image = image_01)

label.grid(row=1, column=0, columnspan=3)

button_back = Button(root, text="Back", command=back, state=DISABLED)

button_exit = Button(root, text="Exit", command=root.quit)

button_forward = Button(root, text="Forward", command=lambda: forward(1))
button_back.grid(row=5, column=0)
button_exit.grid(row=5, column=1)
button_forward.grid(row=5, column=2)

root.mainloop()