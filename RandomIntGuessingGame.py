# random guessing game with computer
import random

def game_session():
    gameOn = True
    myRandomInt = random.randint(1,10)
    
    while(gameOn):
        print("Guess an INT number between 1 and 10")
        
        try:
            userGuess = int(input("Your guess: "))
        except:
            print("Your value cannot convert to int\nTry again!")
            continue
        
        if userGuess == myRandomInt:
            print(f"{userGuess} was correct!")
            gameOn = False
        elif userGuess > myRandomInt:
            print("Too high!")
        else:
            print("Too low!")
            
game_session()