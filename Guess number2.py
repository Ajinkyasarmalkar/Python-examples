SC_number = 18
guesses = 5
while (guesses<5) :
    guess = int(input("enter a number:"))
    if guess != SC_number:
        print("Try again")
    else:
        print("Yoe won!, number of guesses left", guesses)
        break
    guesses = guesses + 1 
if guesses > 5:
    print("Game Over")    
       
    