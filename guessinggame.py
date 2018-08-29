from random import randint
theNum = randint(1,100)
print("Welcome to the Guessing Game! \nWe've chosen a number between 1 and 100 inclusive. \nYour goal is to guess the number. \nWe'll tell you you're warm if you get within 10, \nand warmer if you're getting closer. \nKeep guessing until you get the number!")
notFound = True
diffs = []
numGuesses = 0 
while notFound == True:
    guessStr = input("What's your guess?")
    guess = int(guessStr)
    diff = abs(guess-theNum)
    if guess == theNum: #found case
        print(f"You got it! It took {numGuesses+1} tries!")
        notFound = False
    elif diff <=10 and numGuesses==0: #first loop
            print ("WARM! You're within 10!")
    elif diff >10 and numGuesses==0: #also first loop
            print("COLD!")
    else:
        if diff <= diffs[numGuesses-1]:
            print('WARMER :)')
        else:
            print('COLDER :(')      
    numGuesses +=1
    diffs += [diff]