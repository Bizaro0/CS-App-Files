import random

a = random.randrange(1,15)

count = 0

print("Number Guessing Game By Adi Pat")

(userGuess) = input("Guess the number between 1 and 15: ")
while int(userGuess) != a:  
    if(int(userGuess) > a):
        count+=1
        print("Too high of a guess!")
        (userGuess) = input("Guess the number between 1 and 15: ")
    else:   
        print("Too low of a guess")
        count+=1
        (userGuess) = input("Guess the number between 1 and 15: ")
    #if(int(userGuess) >= 15):
    #    print("Must be lower than 15")
   # if(int(userGuess) <= 1):
   #      print("Guess must be greater than 1")
    if(int(userGuess) == a):
        count+=1
        print("Nice! You got the value in " + str(count) + " tries!")
        break
    
