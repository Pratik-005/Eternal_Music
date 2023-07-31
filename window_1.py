from tkinter import *
import time


def main_win1():
    root = Tk()
    root.geometry("1920x1080")
    root.title("Eternal Music")

    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    print(f"{width}x{height}")

    photo= PhotoImage(file= "C:\\Users\\ASUS\\Downloads\\Programming\\Python_Project\\intro.png")
    l1= Label( image = photo)
    l1.pack()

    time.sleep(3)
    root.after(3000,root.destroy)

    root.mainloop()









