'''Title : Rock Paper Scissors
   Author : Nivedita Pagar
   Date : 08/04/2018
   Details : This code, takes input from the user and gives a decision based on who won the game.
             Rock crushes Scissors
             Scissors Cut Paper
             Paper covers Rock '''

user_continue = True
while user_continue:
    # Ask user for input
    user1 = input('What do you choose for user 1 ? ').lower()   # Make sure that you don't get a false due to cases
    user2 = input('What so you choose for user 2 ? ').lower()
    if user1 == 'rock' and user2 == 'paper':
        print('The winner is user 2')
    elif user1 == 'rock' and user2 == 'scissors':
        print('The winner is user 1')
    elif user1 == 'paper' and user2 == 'rock':
        print('The winner is user 1')
    elif user1 == 'paper' and user2 == 'scissors':
        print('The winner is user 2')
    elif user1 == 'scissors' and user2 == 'rock':
        print('The winner is user 2')
    elif user1 == 'scissors' and user2 == 'paper':
        print('The winner is user 1')
    else:
        print('Something went wrong')
    yes_no = input('Press Y to continue and any other key to exit : ')
    if yes_no.lower() == 'y':
        continue    # Go to the top of closest enclosing loop (while) and repeat the steps
    else:
        break   #Break out of the closest enclosing loop and end the program






