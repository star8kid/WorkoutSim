from tkinter import *
from tkinter import ttk
from tkinter import font

import time
import GameData
import PlayerClass


class GameWindow:
    def __init__(self):

        #Game Window code 

        self.gameWindow = Toplevel()
        self.gameWindow.grid_rowconfigure(0, weight = 1, uniform = "x")
        self.gameWindow.grid_rowconfigure(1, weight = 1, uniform = "x")

        self.gameFrameStyle = ttk.Style()
        self.gameFrame = ttk.Frame(self.gameWindow, padding = "150 20 150 20", relief = SUNKEN)
        self.gameFrame.grid( column = 0, row = 0, sticky = (N, W, E, S))
        self.gameWindow.columnconfigure(0, weight=1)
        self.gameWindow.rowconfigure(0, weight=1)
        self.gameWindow.maxsize(580, 480)
        self.backButtonWidth = 18
        self.backButton = ttk.Button(self.gameFrame, text = "Back to Main Menu", width = self.backButtonWidth)
        self.backButton.grid( column = 2, row = 9 )

        
        self.verticalButtonPad = 5
        self.buttonWidth = 12
    

        #This section of code will dictate how the game will run based on a timer that starts 
        #when the window is opened. The timer will continue until the player closes the window
        #or until they lose
        self.gameInitTime = 0
        # self.gamePlayTime = time.mktime(time.gmtime) - self.gameInitTime
        self.gameClockLabel = ttk.Label(self.gameFrame)
        self.gameClockLabel.grid( column = 2, row = 8)


        # This section of the GameWindow class will store all the buttons.
        # New buttons will be unlocked as the time of the 'workout' goes on
        # (Which is why some of them aren't named yet)

        self.snackLabel = Label(self.gameFrame, text = "Snacks")
        self.snackLabel.grid( column = 1 , row = 2 )

        self.snackAct1 = ttk.Button(self.gameFrame, text = GameData.SnackData["snackOne"]["snackName"], width = self.buttonWidth)
        self.snackAct1['command'] = lambda : self.snackButtonCommand(GameData.SnackData["snackOne"])
        self.snackAct1.grid( column = 1, row = 3, pady = self.verticalButtonPad )
        self.snackAct1.bind('<Enter>', lambda e, snack = GameData.SnackData["snackOne"]: self.snackEnterBind(snack))
        self.snackAct1.bind('<Leave>', lambda e: self.actionLeaveBind())

        self.snackAct2 = ttk.Button(self.gameFrame, text = "???", width = self.buttonWidth)
        self.snackAct2['command'] = lambda snackButton = self.snackAct2 : self.actionUpgrade(GameData.SnackData["snackTwo"], snackButton, "Snack")
        self.snackAct2.grid( column = 1, row = 4, pady = self.verticalButtonPad )
        self.snackAct2.bind('<Enter>', lambda e, snack = GameData.SnackData["snackTwo"] : self.actionUpgradeEnterBind(snack))
        self.snackAct2.bind('<Leave>', lambda e: self.actionLeaveBind())

        self.snackAct3 = ttk.Button(self.gameFrame, text = "???", width = self.buttonWidth)
        self.snackAct3['command'] = lambda snackButton = self.snackAct3 : self.actionUpgrade(GameData.SnackData["snackThree"], snackButton, "Snack")
        self.snackAct3.grid( column = 1, row = 5, pady = self.verticalButtonPad )
        self.snackAct3.bind('<Enter>', lambda e, snack = GameData.SnackData["snackThree"] : self.actionUpgradeEnterBind(snack))
        self.snackAct3.bind('<Leave>', lambda e: self.actionLeaveBind())

        self.excerciseLabel = Label(self.gameFrame, text = "Excercises")
        self.excerciseLabel.grid ( column = 4,  row = 2 )

        self.excerciseAct1 = ttk.Button(self.gameFrame, text = GameData.ExerciseData["exerciseOne"]["exerciseName"], width = self.buttonWidth)
        self.excerciseAct1['command'] = lambda : self.exerciseButtonCommand(GameData.ExerciseData["exerciseOne"])
        self.excerciseAct1.grid( column = 4, row = 3, pady = self.verticalButtonPad )
        self.excerciseAct1.bind('<Enter>', lambda e, exercise = GameData.ExerciseData["exerciseOne"] : self.exerciseEnterBind(exercise))
        self.excerciseAct1.bind('<Leave>', lambda e: self.actionLeaveBind())

        self.excerciseAct2 = ttk.Button(self.gameFrame, text = "???", width = self.buttonWidth)
        self.excerciseAct2['command'] = lambda exerciseButton = self.excerciseAct2 : self.actionUpgrade(GameData.ExerciseData["exerciseTwo"], exerciseButton, "Exercise")
        self.excerciseAct2.grid( column = 4, row = 4, pady = self.verticalButtonPad )
        self.excerciseAct2.bind('<Enter>', lambda e, exercise = GameData.ExerciseData["exerciseTwo"] : self.actionUpgradeEnterBind(exercise))
        self.excerciseAct2.bind('<Leave>', lambda e: self.actionLeaveBind())

        self.excerciseAct3 = ttk.Button(self.gameFrame, text = "???", width = self.buttonWidth)
        self.excerciseAct3.grid( column = 4, row = 5, pady = self.verticalButtonPad )
        self.excerciseAct3['command'] = lambda exerciseButton = self.excerciseAct3 : self.actionUpgrade(GameData.ExerciseData["exerciseThree"], exerciseButton, "Exercise")
        self.excerciseAct3.bind('<Enter>', lambda e, exercise = GameData.ExerciseData["exerciseThree"] : self.actionUpgradeEnterBind(exercise))
        self.excerciseAct3.bind('<Leave>', lambda e: self.actionLeaveBind())

        #This section is deticated for the different value bars
        #(Requires the installation of the fstrings library)
        self.calorieBurnedStyle = ttk.Style()
        self.calorieBurnedStyle.configure("Calorie.TLabel", background = "yellow")
        self.calBurnedLabel = ttk.Label(self.gameFrame, style = "Calorie.TLabel", text = f"Calories Burned: {PlayerClass.Player.caloriesBurned}", width = self.backButtonWidth)
        self.calBurnedLabel.grid( column = 2 , row = 6 )
        self.happinessStyle = ttk.Style()
        self.happinessStyle.configure("Happiness.TLabel", background = "lime green")
        self.happinessLabel = ttk.Label(self.gameFrame, style = "Happiness.TLabel", text = f"Happiness: {PlayerClass.Player.happinessAmount}", width = self.backButtonWidth)
        self.happinessLabel.grid( column = 2, row = 7 )

        #This section is for displaying the button values and
        #each snack and exercise's descriptions

        self.infoFrameStyle = ttk.Style()
        self.infoFrameStyle.configure("InfoFrameStyle.TFrame", background = "gray28")
        self.actionNameFont = font.Font( family = "Microsoft YaHei UI Light" , slant = "italic" , underline = True, size = 15) 
        self.actionNameStyle = ttk.Style()
        self.actionNameStyle.configure("ActionNameStyle.TLabel", font = self.actionNameFont, foreground = "ghost white", background = "gray28")
        # print(self.actionNameStyle.element_options("ActionNameStyle.TLabel"))
        self.actionDescFont = font.Font( family = "Microsoft YaHei UI", size = 12)
        self.actionDescStyle = ttk.Style()
        self.actionDescStyle.configure("ActionDescStyle.TLabel", font = self.actionDescFont, foreground = "ghost white", background = "gray28")
        self.actionGainStyle = ttk.Style()
        self.actionGainStyle.configure("ActionGainStyle.TLabel", font = self.actionDescFont, foreground = "lime", background = "gray28")
        self.actionCostStyle = ttk.Style()
        self.actionCostStyle.configure("ActionCostStyle.TLabel", font = self.actionDescFont, foreground = "red", background = "gray28")
        self.actionUpgradeCostStyle = ttk.Style()
        self.actionUpgradeCostStyle.configure("ActionUpgradeCostStyle.TLabel", font = self.actionDescFont, foreground = "aquamarine", background = "gray28")


        self.infoFrame = ttk.Frame(self.gameWindow, style = "InfoFrameStyle.TFrame", padding = "150 20 150 20", relief = RAISED)
        self.infoFrame.grid( column = 0 , row = 1 , sticky = (N,W,E,S))
        
        self.actionNameLabel = ttk.Label(self.infoFrame, style = "ActionNameStyle.TLabel")
        self.actionNameLabel.grid( column = 0 , row = 0, sticky = W)
        self.actionDescLabel = ttk.Label(self.infoFrame, style = "ActionDescStyle.TLabel", anchor = W)
        self.actionDescLabel.grid( column = 0 , row = 1, sticky = W)
        self.actionGainLabel = ttk.Label(self.infoFrame, style = "ActionGainStyle.TLabel")
        self.actionGainLabel.grid( column = 0 , row = 2, sticky = W)
        self.actionCostLabel = ttk.Label(self.infoFrame, style = "ActionCostStyle.TLabel")
        self.actionCostLabel.grid( column = 0 , row = 3, sticky = W)
        self.actionUpgradeCostLabel = ttk.Label(self.infoFrame, style = "ActionUpgradeCostStyle.TLabel")
        self.actionUpgradeCostLabel.grid( column = 0, row = 4, sticky = W)

    def snackEnterBind(self, snackKey):
        # print(snackKey["snackName"]) <-- Correct formatting for JSON files
        self.actionNameLabel['text'] = snackKey["snackName"]
        self.actionDescLabel['text'] = snackKey["snackDesc"]
        self.actionGainLabel['text'] = f"Joy Gain: {snackKey['joyPower']}"
        self.actionCostLabel['text'] = f"Calorie Cost: {snackKey['calCost']}"

    def exerciseEnterBind(self, exerciseKey):
        self.actionNameLabel['text'] = exerciseKey["exerciseName"]
        self.actionDescLabel['text'] = exerciseKey["exerciseDesc"]
        self.actionGainLabel['text'] = f"Calorie Gain: {exerciseKey['calGain']}"

    def actionUpgradeEnterBind(self, action):
        self.actionNameLabel['text'] = "???"
        self.actionDescLabel['text'] = action["unlockPreviewMessage"]
        self.actionUpgradeCostLabel['text'] = f"Unlock Cost: {action['unlockCost']}"

    def actionLeaveBind(self):
        self.actionNameLabel['text'] = ""
        self.actionDescLabel['text'] = ""
        self.actionGainLabel['text'] = ""
        self.actionCostLabel['text'] = ""
        self.actionUpgradeCostLabel['text'] = ""

    def updateWindow(self):
        self.calBurnedLabel['text'] = f"Calories Burned: {PlayerClass.Player.caloriesBurned}"
        self.happinessLabel['text'] = f"Happiness: {PlayerClass.Player.happinessAmount}"

    def snackButtonCommand(self, snack):
        PlayerClass.Player.doSnack(snack)
        self.updateWindow()

    def exerciseButtonCommand(self, exercise):
        PlayerClass.Player.doExercise(exercise)
        self.updateWindow()

    def actionUpgrade(self, action, actionButton, actionType):
        tempUpgradeCostVar = action["unlockCost"]
        if ((PlayerClass.Player.caloriesBurned >= action["unlockCost"]) and (actionType == "Snack")):
            PlayerClass.Player.caloriesBurned -= action["unlockCost"]
            actionButton['text'] = action["snackName"]
            actionButton['command'] = lambda : self.snackButtonCommand(action)
            print("The command has CHANGED!")
            self.actionUpgradeCostLabel['text'] = ""
            actionButton.bind('<Enter>', lambda e : self.snackEnterBind(action))
            self.snackEnterBind(action)
            self.updateWindow()
        elif ((PlayerClass.Player.caloriesBurned >= action["unlockCost"]) and (actionType == "Exercise")):
            PlayerClass.Player.caloriesBurned -= action["unlockCost"]
            actionButton['text'] = action["exerciseName"]
            actionButton['command'] = lambda : self.exerciseButtonCommand(action)
            print("The command has CHANGED!")
            self.actionUpgradeCostLabel['text'] = ""
            actionButton.bind('<Enter>', lambda e : self.exerciseEnterBind(action))
            self.exerciseEnterBind(action)
            self.updateWindow()
        else:
            self.actionUpgradeCostLabel['text'] = f"Unlock Cost: {tempUpgradeCostVar} \nYou don't have enough Calories!"
            #Figure out how to temp display this without using time.sleep





    def gameClock(self):

        #New Time Idea: Get the time when the game starts and the time when the player loses
        #Convert them both into rational seconds and then uses gmtime() to turn them into actual values, like with hours and minutes.

        self.gamePlayTime = time.mktime(time.gmtime()) - (self.gameInitTime)
        self.gameClockLabel['text'] = f"Total Time: {self.gamePlayTime}"
     
        if((self.gamePlayTime != 0) and ((self.gamePlayTime % GameData.GameDifficulty.getDegInterval()) == 0)):
            print("I ran!")
            GameData.GameDifficulty.incrementDegredation()
            GameData.GameDifficulty.setHappinessDegredation(round(GameData.GameDifficulty.getHappinessDegredation(),1))
            print("Current degredation is " + str(GameData.GameDifficulty.getHappinessDegredation()))
        # else:
            # print("I didn't run")
            # print("Current degredation is " + str(GameData.GameDifficulty.getHappinessDegredation()))
        if(self.gamePlayTime > 0):   
            PlayerClass.Player.happinessAmount = round(PlayerClass.Player.happinessAmount - GameData.GameDifficulty.getHappinessDegredation(),1)
        self.updateWindow()
        # print(Player.happinessAmount)
        self.gameClockLabel.after(1000, self.gameClock)
        
        #Figure out why the getDegInterval is immediately gotten from the class

        

    def startGame(self):
        # This method will start the game and run itself continuously
        print("The game should've started")
        self.gameInitTime = time.mktime(time.gmtime())
        GameData.GameDifficulty.setGameDifficulty()
        self.gameClock()
        # print(self.gamePlayTime)