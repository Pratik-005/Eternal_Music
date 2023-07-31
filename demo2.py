from tkinter import *

root = Tk()
root.geometry("1920x1080")
root.title("Eternal Music")




frame_img = Frame(root, relief=SUNKEN, height=600, width=200)
frame_img.pack(side=LEFT)
frame_img.config(background="black")


def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x,y=y)

frame_img.bind("<Button-1>",drag_start)
frame_img.bind("<B1-Motion>",drag_motion)









root.mainloop()
