~THE PECULIAR EXPEDITION~
This is going to be an adventure game, where you can explore islands, collect treasures, trade with villagers, and so on.
The goal is to find the Golden Pyramid on each map.

~ABOUT THE GAME~
The game is not graphical yet. All the visuals are represented in ASCII text art from these webpages:
http://ascii.co.uk/art
https://www.asciiart.eu
The game is playable in terminal. Each command you give in the game must be executed by hitting 'ENTER'.
The rest of the rules will be stated in the game while running.

~HOW TO INSTALL~
on mac, linux:

Option 1: Call the interpreter
		python3 <filename>.py
Option 2: Let the script call the interpreter
		Make sure the first line of your file has #!/usr/bin/env python.
		Make it executable - chmod +x <filename>.py.
		And run it as ./<filename>.py

on windows: 

Exact steps for adding Python to the path on Windows 7+:
Computer -> System Properties (or Win+Break) -> Advanced System Settings
Click the Environment variables... button (in the Advanced tab)
Edit PATH and append ;C:\Python3 to the end (substitute your Python version)
Click OK. Note that changes to the PATH are only reflected in command prompts opened after the change took place.

NOTE: the game consists of 2 files: 
GAME.py 					- includes the vast majority of the code
GAME_displays.py 	- includes the ASCII text art for visuals, and some character references


Built with Python3.
