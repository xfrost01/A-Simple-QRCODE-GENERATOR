import qrcode
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("QRCode Generator")
root.geometry("300x200")

url_entry = Entry(root, width=30)
url_entry.pack(pady=10)

qr_label = Label(root)  
qr_label.pack(pady=10)


def generate_qr_code():  
    img = qrcode.make()
    type(img)  
    img.save("QRCODE.png")
    img = ImageTk.PhotoImage(Image.open("QRCODE.png"))

main_menu = Menu(root)
root["menu"] = main_menu

    
qrcode_menu = Menu(main_menu)   
qrcode_menu.add_command(label="Item1", command=generate_qr_code)
main_menu.add_cascade(label="Program", menu=qrcode_menu) 
enter_button = Button(root, text="Valider", command=generate_qr_code)
enter_button.place(x=110,y=60)


root.mainloop()





