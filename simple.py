
import random

device_guess = random.randint(1,10)

limit = 0
score = 0

while limit <3:
    try:
        user_guess = int(input("Guess a number bellow 10: "))
        if user_guess > 10 or user_guess < 0 :
            print("Try again.")
            continue

    except:
        print("Your input is wrong.")

    if device_guess == user_guess:
        if limit == 0:
            score += 15
        elif limit == 1: 
            score += 10  
        elif limit == 2: 
            score += 5       
        else:
            score == score 
    elif device_guess > user_guess:
        print("Your guess number is lower than my number.")            
    else:
        print("Your guess number is upper than my number.")    
    limit += 1
if limit > 2:
    print("You tried many times.")
    print("My number was {}".format(device_guess))

else:
    print("Wow! Your Score is {}".format(score))
