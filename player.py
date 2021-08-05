from tkinter import *
import pygame
from tkinter import filedialog
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk

root = Tk()
root.title("Music PLayer")
root.iconbitmap("")
# ADD ICON
root.geometry("500x400")
# Initializes Pygame Mixer
pygame.mixer.init()


# Song Length Information
def play_time():
    # Elapsed time
    current_time = pygame.mixer.music.get_pos() / 1000

    # Temp Label
    # slider_label.config(text=f'Slider: {int(my_slider.get())} and Song Position: {int(current_time)}')

    # convert display format
    converted_time_format = time.strftime('%M:%S', time.gmtime(current_time))

    # get current song
    # currently_playing = music_box.curselection()
    # Get song title
    song = music_box.get(ACTIVE)
    # add dir structure and mp3 to song title
    song = f'C:/User/rohit/Desktop/Learning Projects/Music Player/audio/{song}.mp3'
    # load and get song length
    song_mutagen = MP3(song)

    global song_length
    song_length = song_mutagen.info.length

    converted_song_length_format = time.strftime('%M:%S', time.gmtime(song_length))

    current_time += 1

    if int(my_slider.get()) == int(song_length):
        # output to status bar
        status_bar.config(text=f'Time Elapsed: {converted_song_length_format}  of  {converted_song_length_format}  ')
    elif int(my_slider.get()) == int(current_time):
        # slider has not moved
        # Update to Position
        slider_position = int(song_length)
        my_slider.config(to=slider_position, value=int(current_time))
    else:
        # slider has moved
        # Update to Position
        slider_position = int(song_length)
        my_slider.config(to=slider_position, value=int(my_slider.get()))
        # convert display format
        converted_time_format = time.strftime('%M:%S', time.gmtime(int(my_slider.get())))
        # output to status bar
        status_bar.config(text=f'Time Elapsed: {converted_time_format}  of  {converted_song_length_format}  ')
        # Move along by one second
        next_time = int(my_slider.get()) + 1
        my_slider.config(value=next_time)

    # output to status bar
    # status_bar.config(text=f'Time Elapsed: {converted_time_format}  of  {converted_song_length_format}  ')
    # update slider position to current song position
    # my_slider.config(value=int(current_time))
    # update time
    status_bar.after(1000, play_time)


# Function to add songs
def add_song():
    song = filedialog.askopenfilename(initialdir='audio/', title="Choose Song", filetypes=(("mp3 Files", "*.mp3"), ))
    # strip dir info and .mp3 extension from name
    song = song.replace("C:/User/rohit/Desktop/Learning Projects/Music Player/audio/", "")
    song = song.replace(".mp3", "")
    # add song
    music_box.insert(END, song)


def add_multiple_songs():
    songs = filedialog.askopenfilenames(initialdir='audio/', title="Choose Song", filetypes=(("mp3 Files", "*.mp3"), ))
    # loop through songs
    for song in songs:
        song = song.replace("C:/User/rohit/Desktop/Learning Projects/Music Player/audio/", "")
        song = song.replace(".mp3", "")
        # add song
        music_box.insert(END, songs)


# Play function
def play():
    song = music_box.get(ACTIVE)
    song = f'C:/User/rohit/Desktop/Learning Projects/Music Player/audio/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    # Call play_time()
    play_time()

    # Update slider position
    # slider_position = int(song_length)
    # my_slider.config(to=slider_position, value=0)


# Global pause variable
global paused
paused = False


# Pause Function
def pause(is_paused):
    global paused
    paused = is_paused

    if paused:
        # unpause
        pygame.mixer.music.unpause()
        paused = False
    else:
        # pause
        pygame.mixer.music.pause()
        paused = True


# Stop Function
def stop():
    pygame.mixer.music.stop()
    music_box.select_clear(ACTIVE)
    # clear status bar
    status_bar.config(text='')


# Backward Function
def back():
    # current song tuple number
    current_song = music_box.curselection()
    # add one to current song tuple number
    current_song = current_song[0]-1
    # Get song title
    song = music_box.get(current_song)
    # add dir structure and mp3 to song title
    song = f'C:/User/rohit/Desktop/Learning Projects/Music Player/audio/{song}.mp3'
    # load and play song
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)


# Forward Song Function
def forward():
    # current song tuple number
    current_song = music_box.curselection()
    # add one to current song tuple number
    current_song = current_song[0]+1
    # Get song title
    song = music_box.get(current_song)
    # add dir structure and mp3 to song title
    song = f'C:/User/rohit/Desktop/Learning Projects/Music Player/audio/{song}.mp3'
    # load and play song
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # Move active bar in player
    music_box.selection_clear(0, END)
    music_box.activate(current_song)
    music_box.select_set(current_song, last=None)


# Remove a song
def remove_song():
    music_box.delete(ANCHOR)
    # Stops music if playing
    pygame.mixer.music.stop()


# Remove all songs
def remove_all_songs():
    music_box.delete(0, END)
    # Stops music if playing
    pygame.mixer.music.stop()


# slider function
def slide():
    # slider_label.config(text=f'{int(my_slider.get())} of {int(song_length)}')
    song = music_box.get(ACTIVE)
    song = f'C:/User/rohit/Desktop/Learning Projects/Music Player/audio/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0, start=int(my_slider.get()))


music_box = Listbox(root, bg="white", fg="black", width=60, selectbackground="white", selectforeground="black")
music_box.pack(pady=20)

# Control Frame
control_frame = Frame(root)
control_frame.pack()

# Button Controls
pause_img = PhotoImage(file="images/pause.png")
play_img = PhotoImage(file="images/Play.png")
stop_img = PhotoImage(file="images/stop.png")
back_img = PhotoImage(file="images/backward.png")
forward_img = PhotoImage(file="images/forward.png")

# Player buttons
pause_btn = Button(control_frame, image=pause_img, borderwidth=0, command=lambda: pause(paused))
play_btn = Button(control_frame, image=play_img, borderwidth=0, command=play)
stop_btn = Button(control_frame, image=stop_img, borderwidth=0, command=stop)
back_btn = Button(control_frame, image=back_img, borderwidth=0, command=back)
forward_btn = Button(control_frame, image=forward_img, borderwidth=0, command=forward)

pause_btn.grid(row=0, column=0, padx=5)
play_btn.grid(row=0, column=1, padx=5)
stop_btn.grid(row=0, column=2, padx=5)
back_btn.grid(row=0, column=3, padx=5)
forward_btn.grid(row=0, column=4, padx=5)

# menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add Song Menu
add_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Song", menu=add_menu)
add_menu.add_command(label="Add One Song", command=add_song)
# Add multiple songs to playlist
add_multiple_songs.add_command(label="Add Multiple Songs", command=add_multiple_songs)

# Remove Song Menu
remove_menu = Menu(my_menu)
my_menu.add_cascade(label="Remove Songs", menu=remove_menu)
remove_menu.add_command(label="Remove Song from Playlist", command=remove_song)
remove_menu.add_command(label="Remove Song from Playlist", command=remove_all_songs)

# Status Bar
status_bar = Label(root, text='', bd=1, relief=GROOVE, anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=2)

# Create Slider
my_slider = ttk.Scale(root, from_=0, to=100, orient=HORIZONTAL, value=0, command=slide, length=350)
my_slider.pack(pady=30)

# Temporary Label
# slider_label = Label(root, text="0")
# slider_label.pack(pady=10)

root.mainloop()
