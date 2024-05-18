import random

wordList = ["tomato", "peas", "carrot","cauliflower","onion", "spinach", "garlic","cabbage","broccoli"] 

a = len(wordList)

rand = random.randrange(0,a)

realWord = wordList[rand]


# add hints later on # 


for tries in range(0,12):
    guessStr = (input)("Enter a vegetable ")
    if(guessStr == (realWord)):
        tries+=1
        print("Nice Job! You got the word in " + (str)(tries) + " tries! ")
        break
    else:
        tries+=1
        print("Incorrect fruit! " + (str)(12-tries) + " tries left, you got this!")
    if(tries == 12):
        print("Ran out of guesses! THe correct word was " + (str)(realWord))
    if(tries == 6):
        print("Here's a small hint - the first and last letters of the vegetable is ' " + str(realWord[0]) + " ' " + str(realWord[len(realWord) - 1]) + " '")
    