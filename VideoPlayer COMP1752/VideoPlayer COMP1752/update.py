from tkinter import *
from tkinter import messagebox
import csv
import tkinter.scrolledtext as tkst
import video_library as lib
import font_manager as fonts

def set_text(text_area, content):
    text_area.delete("1.0", END)
    text_area.insert(1.0, content) 
def errorID():
    messagebox.showwarning(title="Invlid ID", message="Please enter a valid ID")
class UpdateVideo():
    def __init__(self,window):
        window.geometry("850x350")
        window.title("Create Your Playlist")
        self.videoplaylist=[]

        listall_button= Button(window, text="List All Videos",command = self.listall)
        listall_button.grid(row=0, column=0, padx=10, pady=10)
        
        self.video_box = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.video_box.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)
            
        self.Video_ID = Label(window,text="Enter Video ID")
        self.Video_ID.grid(row=0, column=1, padx=10, pady=10)
            
        self.ID_input = Entry(window, width=3)
        self.ID_input.grid(row=0, column=2, padx=8, pady=10)
        
        self.check_video = Button(window,text="Check Video",command = self.displayinfo)
        self.check_video.grid(row=0, column=3, padx=10, pady=10)
        
        self.Videoinfo_box = tkst.ScrolledText(window, width=38, height=12, wrap="none")
        self.Videoinfo_box.grid(row=1, column=3, columnspan=3, sticky="W", padx=10, pady=10)
        
        self.rating_input = Entry(window, width=3)
        self.rating_input.grid(row=0, column=5, padx=8, pady=10)
        
        self.update = Button(window,text="Update",command = self.updateinfo)
        self.update.grid(row=0, column=4, padx=10, pady=10)
        
    def listall(self):
        showlist = lib.list_all()
        set_text(self.video_box,showlist)
        
    def displayinfo(self):
        key = self.ID_input.get()
        name = lib.get_name(key)
        if name is not None:
            director = lib.get_director(key)
            playcount = lib.get_play_count(key)
            rating = lib.get_rating(key)
            info = f"{name}\n{director}\nrating: {rating}\nplays: {playcount}"
            set_text(self.Videoinfo_box,info)
    
            
if __name__== "__main__":
    window = Tk()
    fonts.configure()
    UpdateVideo (window)
    window.mainloop()