#imports required for exit and math
import sys
import random

print("Welcome to the number game!")
print("Would you like to play?")
answer = input("Please answer (yes) or (no):")

#beginning logic for starting the game
if answer == "yes":
    print("Great! Lets continue...")
elif answer == "no":
    print("Maybe next time! Exiting...")
    sys.exit()
else:
    sys.exit("Command not found. Exiting...")

print("game starting...")

#not sure if i need to initialize the variables....
lowerNumber = input("Please enter the lower number of the range you wish to guess from:")
upperNumber = input("Please enter the high number of the range you wish to guess from:")
lowerNumber = int(lowerNumber)
upperNumber = int(upperNumber)

#this print was made when i didn't initialize the variables
print("Your range is: ", lowerNumber, " to ", upperNumber)
numberToGuess = random.randint(lowerNumber, upperNumber)
numberToGuess = int(numberToGuess)

#attempt number control variables 
attemptNum = int(1)
attemptNumLimit = int(5)

print("You get ", attemptNum, " guesses. Good Luck!")
guess = input("What number would you like to guess?: ")
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
        sys.exit()  #are these proper exits?

if attemptNum == attemptNumLimit:
    print("You've tried too many times. You lose.")
    print("The number was:", numberToGuess)

#not sure if i can end the program  in a better way
print("Game Exiting...")
sys.exit()

