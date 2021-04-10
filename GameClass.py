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

        self.gameFrameStyle = ttk.Style()
        self.gameFrame = ttk.Frame(self.gameWindow, padding = "150 20 150 20", relief = SUNKEN)
        self.gameFrame.grid( column = 0, row = 0, sticky = (N, W, E, S))
        self.gameWindow.columnconfigure(0, weight=1)
        self.gameWindow.rowconfigure(0, weight=1)
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

        self.snackAct1 = ttk.Button(self.gameFrame, text = GameData.snackOne.snackName, width = self.buttonWidth)
        self.snackAct1['command'] = lambda : self.snackButtonCommand(GameData.snackOne)
        self.snackAct1.grid( column = 1, row = 3, pady = self.verticalButtonPad )
        self.snackAct1.bind('<Enter>', lambda e, snack = GameData.SnackData["snackOne"]: self.snackEnterBind(snack))
        self.snackAct1.bind('<Leave>', lambda e: self.actionLeaveBind())

        self.snackAct2 = ttk.Button(self.gameFrame, text = "???", width = self.buttonWidth)
        self.snackAct2['command'] = lambda : self.snackUpgrade(GameData.SnackData["snackTwo"])
        self.snackAct2.grid( column = 1, row = 4, pady = self.verticalButtonPad )
        self.snackAct2.bind('<Enter>', lambda e, snack = GameData.snackTwo: self.snackUpgradeEnterBind(snack))
        self.snackAct2.bind('<Leave>', lambda e: self.actionLeaveBind())

        self.snackAct3 = ttk.Button(self.gameFrame, text = "???", width = self.buttonWidth)
        self.snackAct3.grid( column = 1, row = 5, pady = self.verticalButtonPad )

        self.excerciseLabel = Label(self.gameFrame, text = "Excercises")
        self.excerciseLabel.grid ( column = 4,  row = 2 )
        self.excerciseAct1 = ttk.Button(self.gameFrame, text = GameData.exerciseOne.exerciseName, width = self.buttonWidth)
        self.excerciseAct1['command'] = lambda : self.exerciseButtonCommand(GameData.exerciseOne)
        self.excerciseAct1.grid( column = 4, row = 3, pady = self.verticalButtonPad )
        self.excerciseAct1.bind('<Enter>', lambda e, exercise = GameData.ExerciseData["exerciseOne"] : self.exerciseEnterBind(exercise))
        self.excerciseAct1.bind('<Leave>', lambda e: self.actionLeaveBind())

        self.excerciseAct2 = ttk.Button(self.gameFrame, text = "???", width = self.buttonWidth)
        self.excerciseAct2.grid( column = 4, row = 4, pady = self.verticalButtonPad )
        self.excerciseAct3 = ttk.Button(self.gameFrame, text = "???", width = self.buttonWidth)
        self.excerciseAct3.grid( column = 4, row = 5, pady = self.verticalButtonPad )

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
        self.actionNameFont = font.Font( family = "Microsoft YaHei UI Light" , slant = "italic" , underline = True) 
        self.actionNameStyle = ttk.Style()
        self.actionNameStyle.configure("ActionNameStyle.TLabel", font = self.actionNameFont, foreground = "ghost white", background = "gray28")
        self.actionDescFont = font.Font( family = "Microsoft YaHei UI")
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

    # def snackEnterBind(self,snack):
    #     self.actionNameLabel['text'] = snack.snackName
    #     self.actionDescLabel['text'] = snack.snackDesc
    #     self.actionGainLabel['text'] = f"Joy Gain: {snack.joyPower}"
    #     self.actionCostLabel['text'] = f"Calorie Cost: {snack.calCost}"

    def snackEnterBind(self, snackKey):
        # print(snackKey["snackName"]) <-- Correct formatting for JSON files
        self.actionNameLabel['text'] = snackKey["snackName"]
        self.actionDescLabel['text'] = snackKey["snackDesc"]
        self.actionGainLabel['text'] = f"Joy Gain: {snackKey['joyPower']}"
        self.actionCostLabel['text'] = f"Calorie Cost: {snackKey['calCost']}"

    def snackUpgradeEnterBind(self, snack):
        self.actionNameLabel['text'] = "???"
        self.actionDescLabel['text'] = GameData.SnackUpgrade.upgradePreviewMessage
        self.actionUpgradeCostLabel['text'] = f"Unlock Cost: {snack.unlockCost}"

    def exerciseEnterBind(self, exerciseKey):
        self.actionNameLabel['text'] = exerciseKey["exerciseName"]
        self.actionDescLabel['text'] = exerciseKey["exerciseDesc"]
        self.actionGainLabel['text'] = f"Calorie Gain: {exerciseKey['calGain']}"
        # self.actionNameLabel['text'] = exercise.exerciseName
        # self.actionDescLabel['text'] = exercise.exerciseDesc
        # self.actionGainLabel['text'] = f"Calorie Gain: {exercise.calGain}"

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

    #Snack Upgrade function

    def snackUpgrade(self, snack):
        tempUpgradeCostVar = snack["unlockCost"]
        if (PlayerClass.Player.caloriesBurned >= snack["unlockCost"]):
            #Do the stuff to change said button into a snack button
            print("The snack has been unlocked in theory!")
        else:
            self.actionUpgradeCostLabel['text'] = f"Unlock Cost: {tempUpgradeCostVar} \n You don't have enough Calories!"
            #Figure out how to temp display this without using time.sleep

    def exerciseButtonCommand(self, exercise):
        PlayerClass.Player.doExercise(exercise)
        self.updateWindow()

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

