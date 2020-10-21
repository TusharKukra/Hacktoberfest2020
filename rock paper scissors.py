import random

def result(your_score,comp_score):
    if your_score>comp_score:
        print("Congratulations! You won the match.  Play again!")
    elif your_score == comp_score:
        print("The match is a tie!  Play again!")
    else :
        print("Opps! You lost the  match.  Try again!")

def win(your_score):
    print("Yay! You won.")
    your_score+=1
    return(your_score)


def lose(comp_score):
    print("Oops! You loose.")
    comp_score+=1
    return(comp_score)
    

rule= {
    1: 'Rock',
    2: 'Paper',
    3: 'Scissors'
}
name= input("Hello there! What's your name? ")
print(f'Welcome to the game {name}!')
your_score=0
comp_score=0

for i in range(0,3):
    choice= int(input("Choose your play: 1-Rock, 2-Paper, 3-Scissors   "))
    computer= random.randint(1, 3)

    if choice == 1 or 2 or 3:
        print(f'You choose {rule[choice]}')
    else:
        print("Please enter a valid number.")

    print(f'Computer choose {rule[computer]}')
    
    if computer==1 :
        if choice==2:
            win(your_score)
        elif choice==3:
            lose(comp_score)
        else :
            print("It's a tie!")

    elif computer==2:
        if choice==3:
            win(your_score)
        elif choice==1:
            lose(comp_score)
        else :
            print("It's a tie!")

    else :
        if choice==1:
            win(your_score)
        elif choice==2:
            lose(comp_score)
        else :
            print("It's a tie!")

    print(f'''    Your score : {your_score}
    Computer's score: {comp_score}''')

result(your_score,comp_score)