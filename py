import random

num=random.randint(1,100)

diff_choice= input(" Welcome to the number guessing game! \n I'm thinking of a number between 1 and 100. \n Choose a difficulty. Type 'easy' or 'hard' :")

def mode(diff_choice):
    if diff_choice == 'easy':
        
        return 10
    elif diff_choice == 'hard':
        return 5
    else:
        return 0
    
attempts = mode(diff_choice)    

while(attempts!=0):
    print(f"You have {attempts} chances remaining to guess the number.\n")
    guess = int(input("Make a guess : "))
    if guess > num:
        print("Too high! \n Guess again")
    elif guess < num:
        print("Too low !")    
    elif guess==num:
        print(f"Congratulations! You have guessed the number {num} ")
        break
    attempts-=1
print("Sorry you failed!")



