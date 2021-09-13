## Checklist


#### Game Mechanics

- ✅ Create a timer that will constantly decrease the happiness bar
- ✅ Make the info frame say the player doesn't have enough calories 
- 🟩 Make the default hunger increase so that the game finishes in a quick amount of time despites one's best    efforts at clicking (three minutes)

#### Game Design / Looks

- ✅ Create a small frame beneath the game window to give the action's cost or gain values
- ✅ ***Whim*** Make each snack / exercise have a description and show it in the message frame
- ✅ Remove the user's ability to edit the window's size inorder to make the game unbreakable
- 🟩 Make it so that if the player closes a window of the game that is *not* the Main Menu, that the root is ended so the code can be properly built again
    - Move the Tk() root to the WorkoutSimulator.py (So the other classes can build on top of it instead of MenuClass)
    - Replace the root window that was in MenuClass with a toplevel

#### Features

- ✅ Make unlockable buttons and upgrades
- 🟩 When the player loses, show a splash screen with the total time and also allow them to play again
- 🟩 ***Whim*** Add music to play in the app; Make it muteable as well
- 🟩 ***Whim*** Add a highscores button and window to display the top ten highscores **Note**: This will require that you know how to save data to files in order for the highscores to show up.

