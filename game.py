import random
import os
import sys

MAX_INT = sys.maxsize
randomNumber = random.randint(1,100)

numberOfGuess = 0
userGuess = int(input("Enter the number: "))
numberOfGuess += 1 

while(userGuess != randomNumber):

    if(userGuess > randomNumber):
        print("Enter a smaller number!")
    else:
        print("Enter a larger number!")
    
    userGuess = int(input("Enter the number: "))
    numberOfGuess += 1

print(f"Yaay! you have won in {numberOfGuess} guesses!!!")

if os.stat("highScore.txt").st_size == 0:
    highScore = MAX_INT
    
else:
    with open("highScore.txt", "r") as f:
        highScore = int(f.read())
    

if(numberOfGuess < highScore):
    print("Congratulations!! You have set the high score.")
    with open("highScore.txt", "w") as f:
        f.write(str(numberOfGuess))

       
