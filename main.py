'''Title : Cow Bull Game
   Author : Nivedita Pagar
   Date : 09/04/2018
   Details : The code generates a random 4 digit number and asks user to guess it
             1) If a digit in the number guessed by the user is in the randomly generated number, but at the wrong position,
                the code returns it as a 'COW'
             2) If a digit in the number guessed by the user is in the randomly generated number, and at the correct position,
                the code returns it as a 'BULL'
             3) This continues until the user guesses the correct number (4 Bulls)

             Example: Randomly generated number = 5678
             User guess: 5897
             Result: 1 BULL and 2 COW
             '''

import numpy.random

def comparison(a,b):
    for i in range(len(guess)):
        # If the digits of guess are in the number
        if guess[i] in number:
            # If the digits of guess are in the correct position
            if guess[i] == number[i]:
                cow_bull[1] += 1
            else:
                cow_bull[0] += 1
    return cow_bull

user_continue = True
while user_continue:
    equal = False
    while not equal:
        # Generate a random 4 digit number, make sure that the 4 digits are distinct and don't repeat
        rand = numpy.random.randint(1000,9999)
        num1 = list(str(rand))
        num2 = set(num1)
        number = list(num2)
        if num1 == number:
            equal = True

    print('Lets Play the Game of COW and BULL!! \nI have randomly generated a 4 digit number !!')
    guesses = 0
    right_wrong = True
    # While loop runs until the correct number is guessed
    while right_wrong:
        user_in = input('Can you guess the number ??')
        # Convert the user input to a list
        guess = list(str(user_in))
        # [cow, bull]
        cow_bull = [0, 0]
        # Call the comparison function to calculate the number of cows and bulls
        comparison(number,guess)
        if cow_bull[1] < 4:
            print(f'You have {cow_bull[0]} COW and {cow_bull[1]} BULL')
            guesses += 1
        else:
            print(f'Bingo !!!\nMy number was {rand} \nYou guessed {guesses} times \nYou Win !!')
            right_wrong = False
    # Ask the user if they want to continue the game or not
    cont = input('Press y to play another game or press any other key to exit')
    if cont.lower() == 'y':
        continue
    else:
        break












