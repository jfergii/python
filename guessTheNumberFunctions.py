#imports for function
import random
import sys

#control variables 
attemptNumLimit = int(5)
attemptNum = int(1)

#sys_main function - is this the preferred way in python to declare sys_main?
def sys_main():

    def sys_exit():
        print("Game is exiting.")
        sys.exit()

    def user_input():
        return input("Type here:")
        
    def check_attempts(attemptNum):
        if attemptNum != attemptNumLimit:
            print("You have tried", attemptNum, "out of", attemptNumLimit, "times.")
            attemptNum = attemptNum + 1
            return (attemptNum)
        elif attemptNum == attemptNumLimit:
            print("You're out of attempts. Try again next time.")
            sys_exit()

    def check_guess(numGuess, numberToGuess):
        if numGuess > numberToGuess:
            print(numGuess, "is higher than the number.")
            return(False)
        elif numGuess < numberToGuess:
            print(numGuess, "is lower than the number.")
            return(False)
        elif numGuess == numberToGuess:
            print("Success! Number to guess was:", numberToGuess)
            sys_exit()

    def get_upper_limit():
        print("Please enter a high number in the range you wish to guess from.")
        upperNumber = user_input()
        upperNumber = int(upperNumber)
        return(upperNumber)

    def get_lower_limit():
        print("Please enter a lower number in the range you wish to guess from.")
        lowerNumber = user_input()
        lowerNumber = int(lowerNumber)
        return(lowerNumber)

    def generate_randNum():
        lowerNumber = get_lower_limit()
        upperNumber = get_upper_limit()
        numberToGuess = random.randint(lowerNumber, upperNumber)
        numberToGuess = int(numberToGuess)
        return numberToGuess

    def get_guess(): 
        print("What number would you like to guess first?")
        numGuess = user_input()
        numGuess = int(numGuess)
        return numGuess

    def play_game():
        print("Would you like to play the number game? yes/no")
        yesNo = user_input()

        if yesNo == "yes":
            print("Great! Lets continue...")
            return(True)
        elif yesNo == "no":
            print("Maybe next time!")
            sys_exit()
        else:
            print("input unexpected.")
            print(yesNo)
            sys_exit()

######################################################################################
#being running functions
    if play_game() == True :
        attemptNum = int(1)
        numberToGuess = generate_randNum()
        print("You get ", attemptNumLimit, " guesses. Good Luck!")

        while attemptNum != attemptNumLimit:
            numGuess = get_guess()
            check_guess(numGuess, numberToGuess)
            attemptNum = check_attempts(attemptNum)

#run sys_main
sys_main()


