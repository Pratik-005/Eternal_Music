import tkinter as tk
from ttkthemes import themed_tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import filedialog
from mutagen.mp3 import MP3
import os
import time
import pygame




def win4():
    def drag_start(event):
        widget = event.widget
        widget.startX = event.x
        widget.startY = event.y

    def drag_motion(event):
        widget = event.widget
        x = widget.winfo_x() - widget.startX + event.x
        y = widget.winfo_y() - widget.startY + event.y
        widget.place(x=x, y=y)
        print(x, y)

    def play_song():
        global music_length
        global directory_list
        progress_scale['value'] = 0
        time_elapsed_label['text'] = "00:00"

        song_name = songs_list.get('active')
        status.config(text=f"Playing : {song_name} Song : {songs_list.index('active')} of "
                           f"{songs_list.size()}")
        directory_path = None
        for dictio in directory_list:
            if dictio['song'] == song_name:
                directory_path = dictio['path']

        song_with_path = f'{directory_path}/{song_name}'
        music_data = MP3(song_with_path)
        music_length = int(music_data.info.length)
        music_duration_label['text'] = time.strftime('%M:%S', time.gmtime(music_length))

        progress_scale['to'] = music_length
        play_button.config(image=pause_icon)
        pygame.mixer.music.load(song_with_path)
        pygame.mixer.music.play()
        scale_update()

    def scale_update():
        global songs_to_play
        global updater
        global music_length
        if progress_scale['value'] < music_length:
            progress_scale['value'] += 1

            time_elapsed_label['text'] = time.strftime('%M:%S', time.gmtime(progress_scale.get()))

            updater = root.after(1000, scale_update)
        else:
            progress_scale['value'] = 0
            time_elapsed_label['text'] = "00:00"
            play_button.config(image=play_icon)
            songs_to_play = []

    def check_play_pause():
        global updater
        global songs_to_play
        songs_to_play.append(songs_list.get('active'))

        length = len(songs_to_play)

        if len(songs_to_play) == 1:
            play_song()

        elif songs_to_play[length - 1] != songs_to_play[length - 2]:
            root.after_cancel(updater)
            play_song()

        else:
            pause_unpause()

    def pause_unpause():
        global pause
        global updater
        if not pause:
            root.after_cancel(updater)
            play_button.config(image=play_icon)
            pause = True

            status.config(
                text=f"Paused : {songs_list.get('active')} {songs_list.index('active') + 1} of {songs_list.size()}")
            pygame.mixer.music.pause()
        else:
            pause = False
            play_button.config(image=pause_icon)
            status.config(
                text=f"Playing : {songs_list.get('active')} {songs_list.index('active') + 1} of {songs_list.size()}")

            pygame.mixer.music.unpause()
            scale_update()

    def next_song():
        global updater
        root.after_cancel(updater)
        song_index = songs_list.index('active')
        songs_list.selection_clear('active')

        list_length = songs_list.size()

        if list_length - 1 == song_index:
            songs_list.selection_set(0)
            songs_list.activate(0)
            play_song()
        else:
            songs_list.selection_set(song_index + 1)
            songs_list.activate(song_index + 1)
            play_song()

    def next_song():
        global updater
        root.after_cancel(updater)
        song_index = songs_list.index('active')
        songs_list.selection_clear('active')

        list_length = songs_list.size()

        if list_length - 1 == song_index:
            songs_list.selection_set(0)
            songs_list.activate(0)
            play_song()
        else:
            songs_list.selection_set(song_index + 1)
            songs_list.activate(song_index + 1)
            play_song()

    def progress_scale_moved(x):
        global updater
        root.after_cancel(updater)
        global directory_list
        scale_at = progress_scale.get()

        song_name = songs_list.get('active')
        directory_path = None

        for dictio in directory_list:
            if dictio['song'] == song_name:
                directory_path = dictio['path']

        pygame.mixer.music.load(f"{directory_path}/{song_name}")

        pygame.mixer.music.play(0, scale_at)
        scale_update()

    def previous_song():
        global updater
        root.after_cancel(updater)
        song_index = songs_list.index('active')
        songs_list.selection_clear('active')

        list_length = songs_list.size()

        if song_index == 0:
            songs_list.selection_set(list_length - 1)
            songs_list.activate(list_length - 1)
            play_song()
        else:
            songs_list.selection_set(song_index - 1)
            songs_list.activate(song_index - 1)
            play_song()

    def add_songs():
        global directory_list
        songs = filedialog.askopenfilenames(title="Select Music Folder", filetypes=(('mp3 files', '*.mp3'),))
        for song in songs:
            song_name = os.path.basename(song)
            directory_path = song.replace(song_name, "")
            directory_list.append({'path': directory_path, 'song': song_name})
            songs_list.insert('end', song_name)

        songs_list.select_set('0')

    window = themed_tk.ThemedTk()
    pygame.init()
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    window.title("Music Player")
    window.geometry(f"{width}x{height}")
    style = ttk.Style()
    style.theme_use("breeze")
    background = "grey"
    style.configure("TScale", background=background)
    # root = prac1.move_to_win3()
    root = window
    root.configure(bg="black")
    auto_icon = Image.open('C:\\Users\ASUS\\Downloads\\Programming\\Python_Project\\win4_Img\\circle.png')
    # auto_icon = auto_icon.resize((300, 300), Image.ANTIALIAS)
    auto_icon = ImageTk.PhotoImage(auto_icon)

    music_image = Image.open('C:\\Users\\ASUS\\Downloads\\Programming\\Python_Project\\win4_Img\\bg.jpg')
    music_image = music_image.resize((370, 300), Image.ANTIALIAS)
    music_image = ImageTk.PhotoImage(music_image)

    repeat_icon = Image.open('C:\\Users\\ASUS\\Downloads\\Programming\\Python_Project\\win4_Img\\repeat.png')
    repeat_icon = repeat_icon.resize((55, 55), Image.ANTIALIAS)
    repeat_icon = ImageTk.PhotoImage(repeat_icon)

    repeat1_icon = Image.open('C:\\Users\\ASUS\\Downloads\\Programming\\Python_Project\\win4_Img\\repeat1.png')
    repeat1_icon = repeat1_icon.resize((40, 40), Image.ANTIALIAS)
    repeat1_icon = ImageTk.PhotoImage(repeat1_icon)

    play_icon = Image.open('C:\\Users\\ASUS\\Downloads\\Programming\\Python_Project\\win4_Img\\play.png')
    play_icon = play_icon.resize((55, 55), Image.ANTIALIAS)
    play_icon = ImageTk.PhotoImage(play_icon)

    pause_icon = Image.open('C:\\Users\\ASUS\\Downloads\\Programming\\Python_Project\\win4_Img\\pause.png')
    pause_icon = pause_icon.resize((55, 55), Image.ANTIALIAS)
    pause_icon = ImageTk.PhotoImage(pause_icon)

    next_icon = Image.open('C:\\Users\\ASUS\\Downloads\\Programming\\Python_Project\\win4_Img\\next.png')
    next_icon = next_icon.resize((55, 55), Image.ANTIALIAS)
    next_icon = ImageTk.PhotoImage(next_icon)

    previous_icon = Image.open('C:\\Users\\ASUS\\Downloads\\Programming\\Python_Project\\win4_Img\\previous.png')
    previous_icon = previous_icon.resize((55, 55), Image.ANTIALIAS)
    previous_icon = ImageTk.PhotoImage(previous_icon)

    stop_icon = Image.open('C:\\Users\\ASUS\\Downloads\\Programming\\Python_Project\\win4_Img\\stop.png')
    stop_icon = stop_icon.resize((55, 55), Image.ANTIALIAS)
    stop_icon = ImageTk.PhotoImage(stop_icon)

    speaker_icon = Image.open('C:\\Users\\ASUS\\Downloads\\Programming\\Python_Project\\win4_Img\\speaker.png')
    speaker_icon = speaker_icon.resize((30, 30), Image.ANTIALIAS)
    speaker_icon = ImageTk.PhotoImage(speaker_icon)

    # mute_icon = Image.open('images/mute.png')
    # mute_icon = mute_icon.resize((30, 30), Image.ANTIALIAS)
    # mute_icon = ImageTk.PhotoImage(mute_icon)

    delete_icon = Image.open('C:\\Users\\ASUS\\Downloads\\Programming\\Python_Project\\win4_Img\\delete.png')
    delete_icon = delete_icon.resize((30, 30), Image.ANTIALIAS)
    delete_icon = ImageTk.PhotoImage(delete_icon)

    delete_all_icon = Image.open('C:\\Users\\ASUS\\Downloads\\Programming\\Python_Project\\win4_Img\\delete2.png')
    delete_all_icon = delete_all_icon.resize((30, 30), Image.ANTIALIAS)
    delete_all_icon = ImageTk.PhotoImage(delete_all_icon)

    add_song_icon = Image.open('C:\\Users\\ASUS\\Downloads\\Programming\\Python_Project\\win4_Img\\song.png')
    add_song_icon = add_song_icon.resize((30, 30), Image.ANTIALIAS)
    add_song_icon = ImageTk.PhotoImage(add_song_icon)

    multiple_song_icon = Image.open('C:\\Users\\ASUS\\Downloads\\Programming\\Python_Project\\win4_Img\\song2.png')
    multiple_song_icon = multiple_song_icon.resize((30, 30), Image.ANTIALIAS)
    multiple_song_icon = ImageTk.PhotoImage(multiple_song_icon)

    shuffle_icon = Image.open('C:\\Users\\ASUS\\Downloads\\Programming\\Python_Project\\win4_Img\\shuffle.png')
    shuffle_icon = shuffle_icon.resize((40, 40), Image.ANTIALIAS)
    shuffle_icon = ImageTk.PhotoImage(shuffle_icon)

    auto_play_icon = Image.open('C:\\Users\\ASUS\\Downloads\\Programming\\Python_Project\\win4_Img\\auto_play.png')
    auto_play_icon = auto_play_icon.resize((55, 55), Image.ANTIALIAS)
    auto_play_icon = ImageTk.PhotoImage(auto_play_icon)

    auto_play_not_icon = Image.open('C:\\Users\\ASUS\\Downloads\\Programming\\Python_Project\\win4_Img\\auto_play_not.png')
    auto_play_not_icon = auto_play_not_icon.resize((40, 40), Image.ANTIALIAS)
    auto_play_not_icon = ImageTk.PhotoImage(auto_play_not_icon)

    song_photo = tk.Label(root, text="", image=music_image, bd=0)
    song_photo.place(x=80, y=78)
    song_photo.bind("<Button-1>", drag_start)
    song_photo.bind("<B1-Motion>", drag_motion)

    # heading = tk.Label(root, bg="black",text="Music Player",font="lucida 40 bold",fg="#F4B81A")
    # heading.place(x=0,y=2,relwidth=1)

    tk.Label(root, text="", background=background, height=7, width=window.winfo_screenwidth()).place(x=7, y=500)

    songs_list = tk.Listbox(root, width=10, height=10, bg="black", fg="blue", bd=0,
                            selectbackground="grey")
    songs_list.place(x=1020, y=199)

    time_elapsed_label = tk.Label(root, text="00:00", fg="black", background=background,
                                  activebackground=background, padx=5)
    time_elapsed_label.place(x=45, y=539)

    music_duration_label = tk.Label(root, text="00:00", fg="black", background=background,
                                    activebackground=background, padx=15)
    music_duration_label.place(x=1033, y=539)

    progress_scale = ttk.Scale(root, orient="horizontal", style='TScale', from_=0, length=950,
                               command=progress_scale_moved, cursor='hand2')
    progress_scale.place(x=91, y=539)
    # music_duration_label.bind("<Button-1>", drag_start)
    # music_duration_label.bind("<B1-Motion>", drag_motion)

    # shuffle_button = tk.Button(root, image=shuffle_icon, command="command", cursor='hand2', bd=0,background=background, activebackground=background)
    # shuffle_button.place(x=10, y=425)
    vol_scale = ttk.Scale(root, from_=0, to=100, orient="vertical", command="simple", cursor="hand2")
    vol_scale.place(x=1214, y=508)
    auto = tk.Label(root, image=auto_icon, cursor='hand2', bd=0)
    auto.place(x=843, y=88)
    # auto.bind("<Button-1>",drag_start)
    # auto.bind("<B1-Motion>",drag_motion)

    status = tk.Label(root, text="Playing : ---------- Song : 0 of 0", fg="black", anchor="w",
                      background="#27537d", font="lucida 9 bold", bd=0)
    status.place(x=22, y=574, relwidth=0.5)
    songs_list.bind("<Button-1>", drag_start)
    songs_list.bind("<B1-Motion>", drag_motion)

    menu = tk.Menu(root)
    root.configure(menu=menu)

    m1 = tk.Menu(menu, background="grey", tearoff=False, bd=0, activebackground="black")
    menu.add_cascade(label="Actions", menu=m1)

    m1.add_command(label="Add Song", command=add_songs, image=add_song_icon, compound="left")
    m1.add_command(label="Add Multiple Songs", command=add_songs, image=multiple_song_icon,
                   compound="left")

    m2 = tk.Menu(menu, background="grey", tearoff=False, bd=0, activebackground="black")
    menu.add_cascade(label="Delete", menu=m2)

    m2.add_command(label="Delete", command="command", image=delete_icon, compound="left")
    m2.add_command(label="Delete All", command="command", image=delete_all_icon, compound="left")
    play_button = tk.Button(root, image=play_icon, command=check_play_pause, cursor='hand2',
                            bd=0, background=background, activebackground=background)
    play_button.place(x=1006, y=232)
    next_button = tk.Button(root, image=next_icon, command=next_song, cursor='hand2', bd=0,
                            background=background, activebackground=background)
    next_button.place(x=1086, y=232)
    previous_button = tk.Button(root, image=previous_icon, command=previous_song,
                                cursor='hand2', bd=0, background=background, activebackground=background)
    previous_button.place(x=923, y=232)
    previous_button.bind("<Button-1>", drag_start)
    previous_button.bind("<B1-Motion>", drag_motion)
    stop_button = tk.Button(root, image=stop_icon, command=pause_unpause, cursor='hand2',
                            bd=0,
                            background=background, activebackground=background)
    stop_button.place(x=1007, y=151)

    # auto_play_button = tk.Button(root, image=auto_play_icon, command="command", cursor='hand2', bd=0, background=background, activebackground=background)
    # auto_play_button.place(x=9, y=290)
    repeat_button = tk.Button(root, image=repeat_icon, command="command", cursor='hand2', bd=0,
                              background=background, activebackground=background)
    repeat_button.place(x=1007, y=311)
    speaker_button = tk.Button(root, image=speaker_icon, command="command", cursor='hand2', bd=0,
                               background=background, activebackground=background)
    speaker_button.place(x=1175, y=576)
    # previous_button.bind("<Button-1>", drag_start)
    # previous_button.bind("<B1-Motion>", drag_motion)

    directory_list = []
    pause = False
    songs_to_play = []
    music_length = 0

    window.mainloop()

