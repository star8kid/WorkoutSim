


class Player:
    #
    #   View the article on incremental game design and decide between two mechanisms
    #


    #
    #   Consider maybe using Component based organization? 
    #   (https://gamedevelopment.tutsplus.com/tutorials/avoiding-the-blob-antipattern-a-pragmatic-approach-to-entity-composition--gamedev-1113)
    #


    #
    # Make these private
    #
    caloriesBurned = 0
    happinessAmount = 100.0
    maxHappiness = 100.0
    
    @staticmethod
    def doExercise(exercise):
        Player.caloriesBurned += exercise["calGain"]

    @staticmethod
    # def doSnack(snack):
    #     if(Player.caloriesBurned - snack["calCost"] < 0):
    #         print("The player doesn't have enough calories!")
    #         return False

    #     elif(Player.happinessAmount + snack["joyPower"] > Player.maxHappiness):
    #         Player.caloriesBurned -= snack["calCost"]
    #         Player.happinessAmount = Player.maxHappiness
    #     else:
    #         Player.caloriesBurned -= snack["calCost"]
    #         Player.happinessAmount += snack["joyPower"]

    def doSnack(snack):
        if(Player.caloriesBurned - snack["calCost"] >= 0):
            Player.caloriesBurned -= snack["calCost"]
            if(Player.happinessAmount + snack["joyPower"] > Player.maxHappiness):
                Player.happinessAmount = Player.maxHappiness
            else:
                Player.happinessAmount += snack["joyPower"]
            return True
        else:
            print("NOT ENOUGH CALORIES DETECTED ! !")
            return False