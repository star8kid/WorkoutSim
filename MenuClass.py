from tkinter import *
from tkinter import ttk
from tkinter import font



class StartingMenu:
    def __init__ (self):


        self.root = Tk()
        self.menuFrame = ttk.Frame(self.root, padding = "120 50 120 50")
        self.menuFrame.grid(column = 0, row = 0, sticky = (N, W, E, S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.menuButtonWidth = 20
        self.quitButtonStyle = ttk.Style()
        self.quitButtonStyle.configure("QuitButtonStyle.TButton", foreground = "red")

        self.menuLabel = ttk.Label(self.menuFrame, text = "Workout Simulator")
        self.menuLabel.grid( column = 1 , row = 1 )
        self.playButton = ttk.Button(self.menuFrame, text = "Play" , width = self.menuButtonWidth)
        self.playButton.grid( column = 1 , row = 2 )
        self.quitButton = ttk.Button(self.menuFrame, text = "Quit" , style = "QuitButtonStyle.TButton", width = self.menuButtonWidth, command = lambda : self.root.quit())
        self.quitButton.grid (column = 1 , row = 3 )

        self.menuFrame.pack()

    def switchToWindow(self,targetWindow):
        self.root.withdraw()
        targetWindow.deiconify()
        
    def switchToGame(self,gameWindow,startGameFunction):
        self.root.withdraw()
        gameWindow.deiconify()
        startGameFunction()

    def switchToMenu(self,targetWindow):
        self.root.deiconify()
        targetWindow.withdraw()
    