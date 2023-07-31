from tkinter import *
from PIL import Image, ImageTk
import window_1 as mw1
from tkinter import filedialog
import time
import tkinter.messagebox as msg
import window_4 as mw4
from pygame import mixer
import os
import shutil
from pathlib import Path

username = ""
password= ""


class check():

    @staticmethod
    def main_win3():
        root = Toplevel()
        root.geometry("1920x1080")
        root.title("Eternal Music")
        root.configure(background="#000000")

        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        print(f"{width}x{height}")


        def play_song(event):
            music_name =playlist.get(ACTIVE)
            mixer.music.load(playlist.get(ACTIVE))
            mixer.music.play()


        global paused
        paused =False

        def pause_unpause():
            global paused
            if paused == True:
                mixer.music.unpause()
                paused = False
                playbtn['image'] = play

            else:
                mixer.music.pause()
                paused = True
                playbtn['image'] = pause

        global current
        current = 0


        def next_song():
            next_song = playlist.curselection()
            next_song = next_song[0] + 1
            song = playlist.get(next_song)
            song = f"C:\\Users\\ASUS\\Music\\{song}"
            mixer.music.load(song)
            mixer.music.play()
            playlist.selection_clear(0, END)
            playlist.activate(next_song)
            playlist.selection_set(next_song, last=None)


        def previous_song():
            next_song = playlist.curselection()
            next_song = next_song[0] - 1
            song = playlist.get(next_song)
            song = f"C:\\Users\\ASUS\\Music\\{song}"
            mixer.music.load(song)
            mixer.music.play()
            playlist.selection_clear(0, END)
            playlist.activate(next_song)
            playlist.selection_set(next_song, last=None)

        """def open_folder():
            path = "C:\\Users\\ASUS\\Music"
            os.chdir(path)
            songs = os.listdir(path)
            for song in songs:
                if song.endswith(".mp3"):
                    playlist.insert(END, song)"""


        def open_user_folder():
            path=""
            if username == "Pratik":
                path = r"C:\Users\ASUS\Videos\Pratik"
                print(path)
            if username == "Kiran":
                path ="C:\\Users\\ASUS\\Videos\\Kiran"
            if username == "Ashray":
                path = "C:\\Users\\ASUS\\Videos\\Ashray"
            if username == "Varad":
                path = "C:\\Users\\ASUS\\Videos\\Varad"
            
            print(path)
            os.chdir(path)
            songs = os.listdir(path)
            for song in songs:
                if song.endswith(".mp3"):
                    playlist.insert(END, song)


        """def load_music():
            playlist.delete(0, END)
            path = filedialog.askdirectory()
            if path:
                os.chdir(path)
                songs = os.listdir(path)
                for song in songs:
                    if song.endswith(".mp3"):
                        playlist.insert(END, song)

            add_song()"""

        def move_to_win4(event):
           mw4.win4()


        def add_song():
            song = filedialog.askopenfilename(initialdir="C:\\Users\\ASUS\\Music", title="chhoos a song",
                                          filetypes=(("mp3 Files", "*.mp3"),))
            song = song.replace('C:\\Users\\ASUS\\Music\\', " ")

            playlist.insert(END,song)          

            source = str(playlist.get(END))
            destination =StringVar()

            if username == "Pratik":
                destination =Path("C:/Users/ASUS/Videos/Pratik")
            if username == "Kiran":
                destination ="C:\\Users\\ASUS\\Videos\\Kiran"
            if username == "Ashray":
                destination = "C:\\Users\\ASUS\\Videos\\Ashray"
            if username == "Varad":
                destination = "C:\\Users\\ASUS\\Videos\\Varad"


            #destination = "C:\\Users\\ASUS\\Videos"
            shutil.copy(source, destination)
            playlist.delete(0, END)
            open_user_folder()

        """
        def create_folder():
            os.chdir("C:\\Users\\ASUS\\Videos")
            os.mkdir("pratik")"""

        mixer.init()

        pause = Image.open("C:\\Users\\ASUS\\Downloads\\Programming\\Python_Project\\play.png")
        pause = pause.resize((80, 80), Image.ANTIALIAS)
        pause = ImageTk.PhotoImage(pause)

        head = Image.open("C:\\Users\\ASUS\\Downloads\\Programming\\Python_Project\\top.png")
        head = head.resize((1530, 65), Image.ANTIALIAS)
        head = ImageTk.PhotoImage(head)
        headname = Label(root, image=head, bd=0)
        headname.place(x=2, y=1)

        frame_img = Frame(root, relief=SUNKEN, height=500, width=900)
        frame_img.place(x=18, y=84)
        frame_img.config(background="#627296")

        img134 = ImageTk.PhotoImage(file=f'C:\\Users\\ASUS\\Downloads\\Programming\\Python_Project\\Images\\3.jpg')
        img2 = ImageTk.PhotoImage(file=f'C:\\Users\\ASUS\\Downloads\\Programming\\Python_Project\\Images\\2.jpg')
        img3 = ImageTk.PhotoImage(file=f'C:\\Users\\ASUS\\Downloads\\Programming\\Python_Project\\Images\\3.jpg')
        img = Label(root,image=img134, bg="black", height=480, width=875)
        img.place(x=28, y=91)

        down = Frame(root, relief=SUNKEN, height=170, width=900)
        down.place(x=18, y=603)
        down.config(background="#627296")
        down.bind('<Double-1>', move_to_win4)

        play = Image.open("C:\\Users\\ASUS\\Downloads\\Programming\\Python_Project\\pause.png")
        play = play.resize((80, 80), Image.ANTIALIAS)
        play = ImageTk.PhotoImage(play)
        playbtn = Button(root, image=play, bd=0, command=pause_unpause)
        playbtn.place(x=425, y=643)

        next = Image.open("C:\\Users\\ASUS\\Downloads\\Programming\\Python_Project\\next.png")
        next = next.resize((80, 80), Image.ANTIALIAS)
        next = ImageTk.PhotoImage(next)
        nextbtn = Button(root, image=next, bd=0, command=next_song)
        nextbtn.place(x=553, y=643)

        previous = Image.open("C:\\Users\\ASUS\\Downloads\\Programming\\Python_Project\\previous.png")
        previous = previous.resize((80, 80), Image.ANTIALIAS)
        previous = ImageTk.PhotoImage(previous)
        previousbtn = Button(root, image=previous, bd=0, command=previous_song)
        previousbtn.place(x=297, y=644)

        loadbtn = Button(root, text="Load Music", bg="#4539ed", padx=8, pady=4, fg="white", font="Helvetica 13 bold", bd=0,
                        command=add_song)
        loadbtn.place(x=1373, y=101)

        my_music = PhotoImage(file="C:\\Users\\ASUS\\Downloads\\Programming\\Python_Project\\mlabel.png")
        mlabel = Label(root,image=my_music, bd=0)
        mlabel.place(x=954, y=87)

        play_frame = Frame(root, height=600, width=578, background="#9ba4e8", bd=0)
        play_frame.place(x=938, y=169)

        scroll = Scrollbar(play_frame)
        playlist = Listbox(play_frame, height=25, width=50, bg="#000000", font="Helvetica ", fg="white",
                       yscrollcommand=scroll.set)
        scroll.config(command=playlist.yview)
        scroll.pack(side=RIGHT, fill=Y)
        playlist.pack(fill=BOTH)
        playlist.bind('<Double-1>', play_song)


        open_user_folder()

        root.mainloop()


#-----------------------------------------------------------------------------------------------------------------------------------------#



class loginform(check) :


    def __init__(self, window):
        
        self.window=window
        width = window.winfo_screenwidth()
        height = window.winfo_screenheight()
        self. window.geometry(f"{width}x{height}")
        self.window.state('zoomed')
        self.window.resizable(0,0)
        self.bg_frame=Image.open('C:\\Users\\ASUS\\Downloads\\Programming\\Python_Project\\Images\\bg123.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel=Label(self.window,image=photo)
        self.bg_panel.image=photo
        self.bg_panel.pack(fill='both',expand='yes')
        self.lgn_frame=Frame(self.window,bg='#040405',width='950',height=600)
        self.lgn_frame.place(x=279,y=108)
        self.txt = 'WELCOME'
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, 'bold'), bg='#040405', fg='white')
        self.heading.place(x=80, y=30, width=300, height=30)

        self.side_image = Image.open('C:\\Users\\ASUS\\Downloads\\Programming\\Python_Project\\Images\\bg4.jpg')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo,bg='#040405')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5,y=100)


        self.sign_in_image = Image.open('C:\\Users\\ASUS\\Downloads\\Programming\\Python_Project\\Images\\login.jpg')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=729, y=52)

        self.sign_in_label=Label(self.lgn_frame,text='sign in',fg='white',font=('yu gothic ui',25,'bold'),bg='#040405')
        self.sign_in_label.place(x=707,y=98)

        self.username_label=Label(self.lgn_frame, text='Username', bg='#040405' , font=('yu gothic ui',17,'bold'),fg ='white')
        self.username_label.place(x=576, y=259)
        global Username_entry
        self.Username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg='#33362e', fg= "#6b6a69",font = ('yu gothic ui', 12, 'bold'))
        self.Username_entry.place (x=629, y=311, width=270)
        self.Username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.Username_line.place(x=629, y=340)


        self.username_icon = Image.open('C:\\Users\\ASUS\\Downloads\\Programming\\Python_Project\\Images\\user.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame,image=photo, bg='#040405')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=576, y=293)
        #self.username_icon_label.bind("<Button-1>", drag_start)
        #self.username_icon_label.bind("<B1-Motion>", drag_motion)


        self.password_label = Label(self.lgn_frame, text='Password', bg='#040405', font=('yu gothic ui', 17, 'bold'), fg='white')
        self.password_label.place(x=576, y=362)
        global password_entry
        self.password_entry = Entry(self.lgn_frame, show='*', highlightthickness=0, relief=FLAT, bg='#33362e', fg="#6b6a69", font=('yu gothic ui', 12, 'bold'))
        self.password_entry.place(x=629, y=410, width=244)
        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.password_line.place(x=629, y=439)

        self.password_icon = Image.open('C:\\Users\\ASUS\\Downloads\\Programming\\Python_Project\\Images\\pass.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=576, y=395)
        #self.password_icon_label.bind("<Button-1>", drag_start)
        #self.password_icon_label.bind("<B1-Motion>", drag_motion)


        



        global log
        log=False

        def verify():
            
            
            global password
            global username

            
            username = self.Username_entry.get()
            password = self.password_entry.get()
            user_data = {"Pratik":"pass@pratik","kiran":"pass@abc","harsh":"pass@xyz","Ashray":"pass@48"}
            list1=list(user_data.keys())
            list2=list(user_data.values())
            if username == "Pratik" and password=="pass@pratik":
                window1.withdraw()
                check.main_win3()
            elif username == "Kiran" and password=="pass@abc":
                 window1.withdraw()
                 check.main_win3()
            elif username == "Varad" and password=="pass@xyz":
                 window1.withdraw()
                 check.main_win3()
            elif username == "Ashray" and password=="pass@48":
                 window1.withdraw()
                 check.main_win3()
            else:
                msg.showwarning("Alert","Invalid username or Password")



        #self.lgn_button = Image.open('images/login12.jpg')
        #photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame,width=100,height=60, bg='#040405')
        #self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=541, y=450)
        self.login = Button(self.lgn_button_label, text='LOGIN', font=('yu gothic vi', 13, 'bold'), width=15, bd=0, bg='#6f99f2', cursor='hand2', activebackground='#2f6aeb', fg='white',command=verify)
        self.login.place(x=97, y=10)

        


#--------------------------------------------------------------------------------------------------------------------------------------------


def Intro():
    root = Tk()
    root.geometry("1920x1080")
    root.title("Eternal Music")

    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    print(f"{width}x{height}")

    photo= PhotoImage(file= "C:\\Users\\ASUS\\Downloads\\Programming\\Python_Project\\intro.png")
    l1= Label( image = photo)
    l1.pack()
    root.after(3000,root.destroy)
    root.mainloop()


Intro()
global window1
window1=Tk()
loginform(window1)
window1.mainloop()




#---------------------------------------------------------------------------------------------------------------------------------------------------





    



