import time
import datetime
import fstrings
import MenuClass
import GameClass
import GameData
import PlayerClass

from tkinter import *
from tkinter import ttk
from tkinter import font


#This simulator will essentially be a simulator/clicker. Here's how it works

"""

    The player will have a "Calories Burned" counter and a "Happiness" meter.
    To raise the "Calories Burned" counter, the player has to do excercises and burn calories
    However, this diminishes the Happiness meter, and it needs to not hit 0 at all!
    To raise the "Happiness" meter, the player has to use the Calories Burned in order to "Buy" snacks and food!
    However, they come at the cost of Calories!
    The goal of the game is to raise the calorie count and also keep the happiness at bay for as long as possible
    Go out there an get fit!


    Design Change 1:
        Happiness will diminish over time rather than be proportional to the amount
        of exercise that the player does.
"""





#Start of the application
app = MenuClass.StartingMenu()
game = GameClass.GameWindow()
game.gameWindow.withdraw()
#Window Configurations
allWindowsTitle = "Workout Simulator"
app.root.resizable(0,0)
game.gameWindow.resizable(0,0)
app.root.title(allWindowsTitle)
game.gameWindow.title(allWindowsTitle)
app.playButton.config( command = lambda : app.switchToGame(game.gameWindow, game.startGame))
game.backButton.config( command = lambda : app.switchToMenu(game.gameWindow))


# Uncomment this later to test out the new time idea
# game.gameClock()
#Make a specific method to switch to the game window AND call the "game clock" method there once it is switched.

# Print out all the font families
# print(font.families())



app.root.mainloop()
# print("The program has not yet run!")