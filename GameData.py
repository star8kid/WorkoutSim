import json

#For this part, view the article regarding the different ways to create game objects

#For the Snack and Exercise classes, they should be counted as Type Objects: Classes that dictate the 
#type of values and functions for each instance created
# https://gameprogrammingpatterns.com/type-object.html
# Go to the `The Pattern` heading to read how to create these classes


# Figure out the file path to read the JSON files

# with open("Snacks.json","r") as SnackDataFile:
#     SnackData = json.load(SnackDataFile)
# SnackDataFile.close()
with open("C:/Users/Anthony/workspace/code_workspace/Python/Game_Codes/WorkoutSimTK/JSON_Files/Snacks.json","r") as SnackDataFile:
    SnackData = json.load(SnackDataFile)
SnackDataFile.close()

with open("C:/Users/Anthony/workspace/code_workspace/Python/Game_Codes/WorkoutSimTK/JSON_Files/Exercises.json","r") as ExerciseDataFile:
    ExerciseData = json.load(ExerciseDataFile)
ExerciseDataFile.close()


class Snack:
    def __init__(self, snackName, snackDesc, calCost, joyPower):
        self.snackName = snackName
        self.snackDesc = snackDesc
        self.calCost = calCost
        self.joyPower = joyPower

snackOne = Snack("Orange", "A healthy, round citrus fruit. Yummy!", 10, 2.0)

class SnackUpgrade(Snack):

    upgradePreviewMessage = "This snack has not been unlocked yet"

    def __init__(self, snackName, snackDesc, calCost, joyPower, unlockCost):
        self.snackName = snackName
        self.snackDesc = snackDesc
        self.calCost = calCost
        self.joyPower = joyPower
        self.unlockCost = unlockCost



snackTwo = SnackUpgrade("Banana", "A tropical fruit. \nTastier than an orange!", 20, 5.0, 100)


class Exercise:
    def __init__(self, exerciseName, exerciseDesc, calGain):
        self.exerciseName = exerciseName
        self.exerciseDesc = exerciseDesc
        self.calGain = calGain


exerciseOne = Exercise("Running", "You already know how to \nwalk, so that doesn't count...", 1)




"""

The simulator will have three difficulties:

Level One-Easy:
    The player is able to freely exercise and eat snacks at their leisure. Though the time is counting down, it will
    decrease at a constant speed / increase only slightly every minute or so.
Level Two-Normal:
    The player must have to concentrate a bit in order to win. The time will increase the rate at which happiness decays
    every thirty seconds and will be greater than that of Level One.

"""
class GameDifficulty:

    #Make proper getters and setters for each variable in order to actually change them in WorkoutSimulator.py

    __difficultyLevel = 1
    # The value the the Happiness Meter will decrement by
    __happinessDegredation = 0
    # The value that the decrement value increased by
    __happinessDegRateIncrement = 0
    # The time between each increment of the decrement in seconds
    __happinessDegInterval = 0
    
    @staticmethod
    def setGameDifficulty():
        if (GameDifficulty.getDifficultyLevel() == 1):
            print("GAME DIFFICULTY SET!!")
            GameDifficulty.setHappinessDegredation(0.1)
            GameDifficulty.setDegRateIncrement(0.2)
            GameDifficulty.setDegInterval(30.0)
    @staticmethod
    def getDifficultyLevel():
        return GameDifficulty.__difficultyLevel
    @staticmethod
    def setDifficultyLevel(value):
        GameDifficulty.__difficultyLevel = value
    @staticmethod
    def getDegInterval():
        return GameDifficulty.__happinessDegInterval
    @staticmethod
    def setDegInterval(value):
        GameDifficulty.__happinessDegInterval = value
    @staticmethod
    def getHappinessDegredation():
        return GameDifficulty.__happinessDegredation
    @staticmethod
    def setHappinessDegredation(value):
        GameDifficulty.__happinessDegredation = value
    @staticmethod
    def getDegRateIncrement():
        return GameDifficulty.__happinessDegRateIncrement
    @staticmethod
    def setDegRateIncrement(value):
        GameDifficulty.__happinessDegRateIncrement = value
    @staticmethod
    def incrementDegredation():
        GameDifficulty.setHappinessDegredation(GameDifficulty.getHappinessDegredation() + GameDifficulty.getDegRateIncrement())

    

