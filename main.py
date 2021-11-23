#Program that runs a math game. Goal is to answer the most questions in a minute

from Game import MathGame

class startGame: #for loading all the modules
    
    def main():

        print("Hi there! This is a basic math game that deals in multiplication, division, addition, and subtraction\n(Note that only ints are valid answers. For divisons below 0, type 0)\n")
        play = input("Would you like to play this game?(type yes or no) ")

        if (play.strip().lower() == "no" or "n"): #Closes program if user doesn't want to play
            return
        
        print("Excellant! Lets get started.\n")
        results = MathGame.game() #Loads game
        MathGame.gameMarks(results) #Loads results from your run
        
        return "Game has finished"


startGame.main() #Starts the game
input("\nPress anything to close the program")
