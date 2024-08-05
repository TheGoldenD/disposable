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
def errorReview():
    messagebox.showwarning(title="Invalid Rating",message="Please enter a valid number")
class UpdateVideo():
    def __init__(self,window):
        window.geometry("950x350")
        window.title("Create Your Playlist")
        self.videoplaylist=[]
        self.ratingdtb=['1','2','3','4','5']
        
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
        
        self.Videoinfo_box = tkst.ScrolledText(window, width=20, height=12, wrap="none")
        self.Videoinfo_box.grid(row=1, column=3, columnspan=3, sticky="W", padx=10, pady=10)
        
        self.rating_input = Entry(window, width=3)
        self.rating_input.grid(row=0, column=5, padx=8, pady=10)
        
        self.label = Label(window,text="Enter New Rating")
        self.label.grid(row=0, column=4, padx=10, pady=10)
        
        self.save = Button(window,text="Save",command=self.NewRating)
        self.save.grid(row=0,column=6)
    
    def DisplayInfo(self,key,name,director=None,rating=None,playcount=None):
            director,playcount,rating = self.GetInfo(key)
            info = f"{name}\n{director}\nrating: {rating}\nplays: {playcount}"
            set_text(self.Videoinfo_box,info)
    def GetInfo(self,key):
            director = lib.get_director(key)
            playcount = lib.get_play_count(key)
            rating = lib.get_rating(key)
            return(director,playcount,rating)
    def GetNameAndKey(self):
            key = self.ID_input.get()
            name = lib.get_name(key)
            return(key,name)
    #Show All available video
    def listall(self):
        showlist = lib.list_all()
        set_text(self.video_box,showlist)
    #Check Video Info    
    def displayinfo(self):
        key , name =self.GetNameAndKey()
        director,rating,playcount = self.GetInfo(key)
        if name is not None:
            self.DisplayInfo( key,name,director,rating,playcount)
    
    def NewRating(self):
        key , name = self.GetNameAndKey()
        newrate = self.rating_input.get()
        if newrate in self.ratingdtb :
            lib.set_rating(key,newrate)
            a = lib.get_rating(key)
            self.DisplayInfo(key,name,rating=a)
        else:
            errorReview()
if __name__== "__main__":
    window = Tk()
    fonts.configure()
    UpdateVideo (window)
    window.mainloop()