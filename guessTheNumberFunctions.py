
#main function - is this the preferred way in python to declare main?
def Main():

    #imports for function
    import random
    import sys

    def sysexit():
        print("Game is exiting.")
        sys.exit()

    #function to accept user input
    def userInput():
        return input("Type here:")
        
    def playGame():

        print("Would you like to play the number game? yes/no")
        yesNo = userInput()

       #beginning logic for starting the game
        if yesNo == "yes":
            print("Great! Lets continue...")
        elif yesNo == "no":
            print("Maybe next time!")
            sysexit()
        else:
            print("input unexpected.")
            print(yesNo)
            sysexit()

        #gather lower limit number
        print("Please enter a lower number in the range you wish to guess from.")
        lowerNumber = userInput()
        lowerNumber = int(lowerNumber) #convert to int - maybe not necessary

        #gather upper limit number
        print("Please enter a high number in the range you wish to guess from.")
        upperNumber = userInput()
        upperNumber = int(upperNumber) #convert to int - maybe not necessary

        #prints range for user and generates random number
        print("Your range is: ", lowerNumber, " to ", upperNumber)
        numberToGuess = random.randint(lowerNumber, upperNumber)
        numberToGuess = int(numberToGuess)

        #attempt number control variables 
        attemptNum = int(1)
        attemptNumLimit = int(5)

        #guess variable is populated based off first input
        print("You get ", attemptNumLimit, " guesses. Good Luck!")
        print("What number would you like to guess first?")
        guess = userInput()
        guess = int(guess)

        #while loop for attempt limit - not sure if this could be done better
        while attemptNum != attemptNumLimit:
            if guess > numberToGuess:
                print("The number is lower than ", guess)
                guess = input("What number would you like to guess?: ")
                guess = int(guess)
                attemptNum = attemptNum + 1
            elif guess < numberToGuess:
                print("The number is highter than ", guess)
                guess = input("What number would you like to guess?: ")
                guess = int(guess)
                attemptNum = attemptNum + 1
            elif guess == numberToGuess:
                print("Success! Number to guess was:", numberToGuess)
                print("You've won the game!")
                print("Congrats!")
                print("See you next time!")
                sysexit() 

        if attemptNum == attemptNumLimit:
            print("You've tried too many times. You lose.")
            print("The number was:", numberToGuess)
            sysexit()

    #run playGame Function
    playGame()

#run Main
Main()


