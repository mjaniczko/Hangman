
def new_game():
    play = input('Would you like to play again? (y/n):  ')
    return play

def guess():
    guess = input("What is your guess? \n")
    return guess

def welcome_screen():
    print('''        WELCOME


Are you ready to awoid beeing hung?
          
Remember you got 5 life's, every incorrect char guess cost you -1 point,
every incorrect word guess cost you -2 points.
So take care but don't forget time is ticking \n''')
