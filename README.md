# Music-Player
Python Tkinter GUI Music Player


Challenges:
A majority of the challeneges with this project were set around the timing and position of each song that was playing in relation to the slider shown below the buttons. One example of this is the slider moving exponentially faster when mulitple songs are played. The program updates the status bar every second in the play_time() function in order to output the accurate time for a song but when a second or third song is played, another loop seemed to be created. The solution that I found was the addition of an if statement that returns nothing if the song is stopped, breaking out of the function and preventing a second loop being started.
