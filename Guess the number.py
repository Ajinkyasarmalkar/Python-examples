import random
num = random.randint(0, 20)
chances = 0
while chances < 5:
    guess = int(input("Enter a number: "))
    if guess > num:
        print("Guess is too high")
    elif guess < num:
        print("Guess is too low")
    else:
        print("Congrats you won!") 
        break   
    chances = chances + 1
print("Good Bye!")    
if not chances < 5:
    print("Opps! out of Moves")            


