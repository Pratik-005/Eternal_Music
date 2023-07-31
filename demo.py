from tkinter import *
from PIL import Image , ImageTk
from pygame import mixer
import os
import time


def img_changer():
    i =0
    while(True):
        image1 = ImageTk.PhotoImage(file=f'C:\\Users\\ASUS\\Downloads\\Programming\\Python_Project\\Images\\{i+1}.jpg')
        img.config(image=image1)
        time.sleep(7)
        i=i+1
        if i == 10:
            i=0


def play_song(event):
    music_name=playlist.get(ACTIVE)
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()


global pauased
paused =False
def pause_unpause():
    global paused
    if paused == True :
        mixer.music.unpause()
        paused=False
        playbtn['image'] = play

    else:
        mixer.music.pause()
        paused=True    
        playbtn['image']= pause



global current
current=0
def next_song():
    next_song = playlist.curselection()
    next_song =next_song[0] + 1
    song = playlist.get(next_song)
    song =f"C:\\Users\\ASUS\\Music\\{song}"
    mixer.music.load(song)
    mixer.music.play()
    playlist.selection_clear(0,END)
    playlist.activate(next_song)
    playlist.selection_set(next_song,last=None)


def previous_song():
    next_song = playlist.curselection()
    next_song =next_song[0] - 1
    song = playlist.get(next_song)
    song =f"C:\\Users\\ASUS\\Music\\{song}"
    mixer.music.load(song)
    mixer.music.play()
    playlist.selection_clear(0,END)
    playlist.activate(next_song)
    playlist.selection_set(next_song,last=None)


def open_folder():
    path = "C:\\Users\\ASUS\\Music"
    os.chdir(path)
    songs = os.listdir(path)
    for song in songs:
        if song.endswith(".mp3"):
            playlist.insert(END,song)


#def move_to_win3(event):
#  mw2.main_win2()


root = Tk()
root.geometry("1920x1080")
root.title("Eternal Music")
root.configure(background="#000000")

mixer.init()

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
print(f"{width}x{height}")


pause=Image.open("C:\\Users\\ASUS\\Downloads\\Programming\\Python_Project\\play.png")
pause = pause.resize((80,80),Image.ANTIALIAS)
pause = ImageTk.PhotoImage(pause)

head=Image.open("C:\\Users\\ASUS\\Downloads\\Programming\\Python_Project\\top.png")
head = head.resize((1530,65),Image.ANTIALIAS)
head= ImageTk.PhotoImage(head)
headname=Label(root,image=head,bd=0)
headname.place(x=2,y=1)

frame_img = Frame(root, relief=SUNKEN, height=500, width=900)
frame_img.place(x=18,y=84)
frame_img.config(background="#627296")

img1 = ImageTk.PhotoImage(file=f'C:\\Users\\ASUS\\Downloads\\Programming\\Python_Project\\Images\\3.jpg')
img = Label(image=img1,bg="black",height=480, width=875)
img.place(x=28,y=91)

down= Frame(root, relief=SUNKEN, height= 170, width=900)
down.place(x=18,y=603)
down.config(background="#627296")
#down.bind('<Double-1>',move_to_win3 )

play=Image.open("C:\\Users\\ASUS\\Downloads\\Programming\\Python_Project\\pause.png")
play = play.resize((80,80),Image.ANTIALIAS)
play =ImageTk.PhotoImage(play)
playbtn=Button(root,image = play,bd=0,command=pause_unpause)
playbtn.place(x=425,y=643)


next=Image.open("C:\\Users\\ASUS\\Downloads\\Programming\\Python_Project\\next.png")
next = next.resize((80,80),Image.ANTIALIAS)
next = ImageTk.PhotoImage(next)
nextbtn=Button(root,image = next,bd=0,command=next_song)
nextbtn.place(x=553,y=643)

previous=Image.open("C:\\Users\\ASUS\\Downloads\\Programming\\Python_Project\\previous.png")
previous = previous.resize((80,80),Image.ANTIALIAS)
previous = ImageTk.PhotoImage(previous)
previousbtn=Button(root,image = previous,bd=0,command= previous_song)
previousbtn.place(x=297,y=644)
 

loadbtn =Button(root,text="Load Music",bg="#4539ed",padx=8,pady=4,fg="white",font="Helvetica 13 bold",bd=0)
loadbtn.place(x=1373,y=101)

my_music = PhotoImage(file="C:\\Users\\ASUS\\Downloads\\Programming\\Python_Project\\mlabel.png")
mlabel=Label(image = my_music,bd=0)
mlabel.place(x=954,y=87)


play_frame = Frame(root, height =600, width = 578, background ="#9ba4e8",bd=0)
play_frame.place(x=938,y=169)

scroll =Scrollbar(play_frame)
playlist = Listbox(play_frame, height = 25, width = 50, bg ="#000000", font = "Helvetica ",fg = "white",yscrollcommand=scroll.set)
scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT,fill=Y)
playlist.pack(fill=BOTH)
playlist.bind('<Double-1>',play_song)


open_folder()

root.mainloop()

