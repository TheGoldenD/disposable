from tkinter import *
from tkinter import messagebox
import tkinter.scrolledtext as tkst
import video_library as lib
import font_manager as fonts

#MISC Functions
def set_text(text_area, content):
    text_area.delete("1.0", END)
    text_area.insert(1.0, content)
    
def add_text(text_area, content):
    text_area.insert(1.0, content + "\n")  
    
def errorID():
    messagebox.showwarning(title="Invlid ID", message="Please enter a valid ID")
def errorDUP():
    messagebox.showinfo(title="Duplicate found", message="The video has already been added")
def errorNull():
    messagebox.showinfo(title="Playlist Empty",message="womp womp")
def errorOver():
    messagebox.showwarning(title="No more",message="Stop")
    
class CreatePlaylist():
        def __init__(self,window):
            window.geometry("850x550")
            window.title("Create Your Playlist")
            
            self.videoplaylist=[]
            self.dfplaylist = 0
            #GUI
            listall_button= Button(window, text="List All Videos",command = self.listall)
            listall_button.grid(row=0, column=0, padx=10, pady=10)
            
            self.video_box = tkst.ScrolledText(window, width=48, height=12, wrap="none")
            self.video_box.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)
            
            self.Video_ID = Label(window,text="Enter Video ID")
            self.Video_ID.grid(row=0, column=1, padx=10, pady=10)
            
            self.ID_input = Entry(window, width=3)
            self.ID_input.grid(row=0, column=2, padx=8, pady=10)
            
            self.Videoinfo_box = tkst.ScrolledText(window, width=17, height=10, wrap="none")
            self.Videoinfo_box.grid(row=1, column=3, columnspan=3, sticky="W", padx=10, pady=10)
            
            self.check_video = Button(window,text="Check Video",command = self.displayinfo)
            self.check_video.grid(row=0, column=3, padx=10, pady=10)
            
            self.add_video = Button(window,text="Add Video",command=self.add_btn_clicked)
            self.add_video.grid(row=0, column=6, padx=8, pady=10)
            
            self.delete_list = Button(window,text="Clear list",command=self.clear_btn_clicked)
            self.delete_list.grid(row=2, column=6, padx=8, pady=10)
            
            self.playlist = tkst.ScrolledText(window, width=17, height=12, wrap="none")
            self.playlist.grid(row=1, column=6, columnspan=3, sticky="W", padx=10, pady=10)
            
            self.playvideo = Button(window,text="Play Video",command=self.PlayVid)
            self.playvideo.grid(row=3, column=6, padx=8, pady=10)
            
            self.next = Button(window,text="Next",command=self.Next)
            self.next.grid(row=4, column=6, padx=8, pady=10)
            
            self.prev = Button(window,text="Prev",command=self.Prev)
            self.prev.grid(row=4, column=5, padx=8, pady=10)
        #Button Functions
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
        
        #Add a video to the playlist
        def add_btn_clicked(self):
            key , name = self.GetNameAndKey()
            if name is not None:
                if key not in self.videoplaylist:
                    self.videoplaylist.append(key)
                    addname=f"{name}"
                    add_text(self.playlist,addname)
                    print(self.videoplaylist)
                else:
                    errorDUP()
            else:
                errorID()
                
        #Clear PLaylist        
        def clear_btn_clicked(self):
            self.playlist.delete("1.0", "end")
            self.videoplaylist.clear()
            
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
        #Play Video
        def PlayVid(self):
                if len(self.videoplaylist) == 0:
                    errorNull()
                else:
                    key = self.videoplaylist[self.dfplaylist]
                    lib.increment_play_count(key)
                    name = lib.get_name(key)
                    self.DisplayInfo(key,name)
                    
        def Next(self):
            if self.dfplaylist < len(self.videoplaylist)-1:
                self.dfplaylist += 1
            elif self.dfplaylist > len(self.videoplaylist)-1:
                self.dfplaylist = len(self.videoplaylist)-1
                
                
        def Prev(self):
            if self.dfplaylist != 0:
                self.dfplaylist -= 1
            elif self.dfplaylist < 0:
                self.dfplaylist =0
                
            
if __name__ == "__main__":         
    window = Tk()
    fonts.configure()
    CreatePlaylist (window)
    window.mainloop()