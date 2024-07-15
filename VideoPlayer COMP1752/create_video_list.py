from tkinter import *
from tkinter import messagebox
import video_library as lib
import font_manager as fonts

window = Tk()
window.geometry()
label = Label(window,text="Create Your Playist",font=('Helvetica,30'))
def Nolibrary():
    messagebox.showinfo(title="Song library not found",Message='Please enter a vallibrarylibrary')
def input_library():
    global listbox
    inputlibrary.get()
    listbox=Listbox()
    listbox.place(x=250,y=250)
    listbox.insert(0,inputlibrary.get())
    listbox.pack()
def checksonglibrary():
    key = inputlibrary.get()
    name = lib.get_name(key)
    if name is not None:
       listbox.insert(lib.get_name)
    else:
        Nolibrary()
inputlibrary= Entry(window,font=("Helvetica",50))
inputlibrary.pack(slibrarye=LEFT)
    

label.pack()
create_button = Button(window,text="Create playlist",font=("Helvetica"),command=lambda:[input_library(),checksonglibrary()],relief=RAISED,bd=7)
create_button.pack(slibrarye=RIGHT)



window.mainloop()