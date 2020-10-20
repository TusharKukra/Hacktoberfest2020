import random

rule= {
    1: 'Rock',
    2: 'Paper',
    3: 'Scissors'
}
name= input("Hello there! What's your name? ")
print(f'Welcome to the game {name}!')
choice= int(input("Choose a number: 1-Rock, 2-Paper, 3-Scissors   "))
computer= random.randint(1, 3)
if choice == 1 or 2 or 3:
    print(f'You choose {rule[choice]}')
else :
    print("Please enter a valid number.")
print(f'Computer choose {rule[computer]}')
if computer==1 :
    if choice==2:
        print("Yay! You won. Play again!")
    elif choice==3:
        print("Oops! You loose. Try again!")
    else :
        print("It's a tie! Play again!")

elif computer==2:
    if choice==3:
        print("Yay! You won. Play again!")
    elif choice==1:
        print("Oops! You loose. Try again!")
    else :
        print("It's a tie! Play again!")

else :
    if choice==1:
        print("Yay! You won. Play again!")
    elif choice==2:
        print("Oops! You loose. Try again!")
    else :
        print("It's a tie! Play again!")