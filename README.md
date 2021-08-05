# Music-Player

**Description**</br>
Python Tkinter GUI Music Player</br>
This project is a simple MP3 music player interface. The interface contains basic controls needed to play and shuffle through music such as a volume slider, song position slider, pause and play buttons, and forward and backward buttons. The interface also requires the user to create their own playlist that is displayed by adding a single song at a time or multiple songs at once. Users can also remove a single song or all of the songs that were added at once. The learning curve for this project was pretty steep as it was my first time using Tkinter. In order to complete this project, I researched various aspects of Tkinter and learned concepts which can be applied to future development of Python GUIs.


**Installation**</br>
Installation and use of this project requires the user to accurately input the file path of the location of their music in the places where specified (Commented in program: "*FILE PATH BEFORE SONG TITLE*"). If correctly done, there should be no other edits that need to be made to the project.


**Challenges**</br>
Although there were a multiple of challenges throughout this project, a majority of them were set around the timing and position of each song that was playing in relation to the slider shown below the buttons. One example of this is the slider moving exponentially faster when mulitple songs are played. The program updates the status bar every second in the play_time() function in order to output the accurate time for a song but when a second or third song is played, another loop seemed to be created. The solution that I found was the addition of an if statement that returns nothing if the song is stopped, breaking out of the function and preventing a second loop being started. Other challenges included positioning of slider based on user action (i.e. if the user stops the song, the slider shifts to the front) and the accurate selection (highlighting) of the song that is playing.
