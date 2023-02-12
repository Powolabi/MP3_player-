from pygame import mixer
from tkinter import *
import tkinter.font as font
from tkinter import filedialog
from player_functions import Play, Pause, Stop, Resume, Previous, Next, addsongs, deletesong

root = Tk()
root.title('Peter Owolabi Music Player Application')
mixer.init()

songs_list = Listbox(root, selectmode=SINGLE, bg="black", fg="white", font=('arial', 15), height=12, width=47, selectbackground="gray", selectforeground="black")
songs_list.grid(columnspan=9)

defined_font = font.Font(family='Helvetica')

#Play
play_button=Button(root, text="Play", width=7, command=Play)
play_button['font']=defined_font
play_button.grid(row=1, column=0)

#Pause
pause_button = Button(root, text="Pause", width=7, command=Pause)
pause_button['font']=defined_font
pause_button.grid(row=1, column=1)

#stop
stop_button = Button(root, text="Stop", width=7, command=Stop)
stop_button['font']=defined_font
stop_button.grid(row=1, column=2)

#Resume
Resume_button = Button(root, text="Resume", width =7, command=Resume)
Resume_button['font']=defined_font
Resume_button.grid(row=1,column=3)

#previous
previous_button=Button(root, text="Prev", width =7, command=Previous)
previous_button['font']=defined_font
previous_button.grid(row=1, column=4)

#Next
next_button = Button(root, text="Next", width =7, command=Next)
next_button['font']=defined_font
next_button.grid(row=1, column=5)

#menu
my_menu = Menu(root)
root.config(menu = my_menu)
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Menu", menu=add_song_menu)
add_song_menu.add_command(label="Add songs", command=addsongs)
add_song_menu.add_command(label="Delete song", command=deletesong)


mainloop()

