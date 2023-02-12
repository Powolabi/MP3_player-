def addsongs():
    temp_song = filedialog.askopenfilenames(initialdir="Music/", title="Choose a song",
                                            filetypes=(("mp3 Files", "*.mp3"),))


for s in temp_song:
        s=s.replace("C:/Users/DataFlair/python-mp3-music-player/","")
songs_list.insert(END,s)

def deletesong():
    curr_song=songs_list.curselection()
    songs_list.delete(curr_song[0])

def Play():
    song=songs_list.get(ACTIVE)
    song=f'C:/Users\pettr\Music/{song}'
    mixer.music.load(song)
    mixer.music.play()

def Pause():
    mixer.music.pause()

def Stop():
    mixer.music.stop()
    songs_list.selection_clear(ACTIVE)


def Resume():
    mixer.music.unpause()



def Previous():
    #to get the selected song index
    previous_one=songs_list.curselection()
    #to get the previous song index
    previous_one=previous_one[0]-1
    #to get the previous song
    temp2=songs_list.get(previous_one)
    temp2=f'C:/Users/DataFlair/python-mp3-music-player/{temp2}'
    mixer.music.load(temp2)
    mixer.music.play()
    songs_list.selection_clear(0,END)
    #activate new song
    songs_list.activate(previous_one)
    #set the next song
    songs_list.selection_set(previous_one)



def Next():
    #to get the selected song index
    next_one=songs_list.curselection()
    #to get the next song index
    next_one=next_one[0]+1
    #to get the next song
    temp=songs_list.get(next_one)
    temp=f'C:/Users/DataFlair/python-mp3-music-player/{temp}'
    mixer.music.load(temp)
    mixer.music.play()
    songs_list.selection_clear(0,END)
    #activate newsong
    songs_list.activate(next_one)
     #set the next song
    songs_list.selection_set(next_one)