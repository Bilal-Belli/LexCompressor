import subprocess
import shutil
from tkinter import *
from tkinter import filedialog, ttk
from tkinterdnd2 import DND_FILES, TkinterDnD

global path

# hover the buttons effect
def hoverActive(boton, color1, color2, color3):
	boton.configure(bg=color1)
	def fuera(e):
		boton.configure(bg=color1)
	def dentro(e):
		boton.configure(bg=color2)
	def activo(e):
		boton.configure(activebackground=color3)
	boton.bind("<Enter>", dentro)
	boton.bind("<Leave>", fuera)
	boton.bind("<ButtonPress-1>", activo)

def fonction1():
    global path
    path = filedialog.askopenfilename()
    # shutil.copyfile(path, "./test.txt")

def fonction2():
    global path
    if 1==1:
        print("Inside Python file.....")
        subprocess.call(["gcc", "Compresser.c"])
        # subprocess.call("./decompression.exe")
        subprocess.call("./a.exe")
        print("Task is done.")

def fonction3():
    global path
    if 1==1:
        print("Inside Python file.....")
        subprocess.call(["gcc", "Decompresser.c"])
        subprocess.call("./a.exe")
        # subprocess.call("./compression.exe")
        print("Task is done.")

# define of gui of app
root = TkinterDnD.Tk()
root.title('RARLE')
# Designate Height and Width of our app
app_width = 250
app_height = 120
# The Height and Width of our pc screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2 ) - (app_height / 2)
root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
label_1 = Label(root,width="250",height="130",bg="#EE4E34")#to colorate the space of application
label_1.place(x=0,y=0)
root.resizable(False,False)
BtnUpld = Button(root,fg= "#000",text="Choisir un Fichier text", cursor="hand2",borderwidth=0,width=26,command = fonction1)
hoverActive(BtnUpld, "#ffffff", "#FCEDDA", "#ffffff")
BtnUpld.pack( ipadx=1, ipady=5, padx=6, pady=4)
BtnCompress = Button(root,fg= "#000",text="Compresser", cursor="hand2",borderwidth=0,width=26,command = fonction2)
hoverActive(BtnCompress, "#ffffff", "#FCEDDA", "#ffffff")
BtnCompress.pack( ipadx=2, ipady=5, padx=6, pady=4)
BtnDecompress = Button(root,fg= "#000",text="Decompresser", cursor="hand2",borderwidth=0,width=26,command = fonction3)
hoverActive(BtnDecompress, "#ffffff", "#FCEDDA", "#ffffff")
BtnDecompress.pack( ipadx=3, ipady=5, padx=6, pady=4)

root.mainloop()