# The Peculiar Expedition

This is going to be an adventure game, where you can explore islands, collect treasures, trade with villagers, and so on.   
The goal is to find the Golden Pyramid on each map.

## About the game

The game is not graphical yet. All the visuals are represented in ASCII text art from these webpages:   
http://ascii.co.uk/art   
https://www.asciiart.eu   
The game is playable in terminal. Each command you give in the game must be executed by hitting 'ENTER'.   
The rest of the rules will be stated in the game while running.

```bash
move with 'w a s d': <'a' and hit enter> 
```

## How to run

make the files executable with: chmod +x filename   
Call the interpreter: python3 GAME.py  

## Note

The game is in an early stage, It's still under development.
The game consists of 6 files:  
  core_game.py -  Variables that are essential for almost all the functions in and outside of this file
                  Functions responsible for displaying the map, the inventory and for moving on the map (looping the game)
                  Function calls for starting the program
                  
  GAME_displays.py - includes the ASCII text art for visuals, and some character references 
  
  random_map_generator.py - includes: Variables and functions for generating a new, random map for the game.
  village_and_companions.py - includes: Dictionary variables holding the keys and values for 'companions' and vendor  merchandise
                                        Functions responsible for running the Village (trading,resting,hiring companions) ,   calculating the move cost in the
                                            aspect of having more companions, giving and taking away benefits of companions on hiring or loosing them

  passive_terrains.py: - includes: Functions for terrain types that have no interactive interface
  
  interactive_terrains: includes - Variables essential for the functions in this file
                                   TERRAIN Functions for terrain types that have an interactive interface, and FEATURE functions that are called in the terrain type functions if they meet the requirements.
                                   
Built with Python3.
