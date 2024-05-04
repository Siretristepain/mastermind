#_____________________________________ MASTERMIND ___________________________________________#


#=====
# IDEA
#=====

"""
This script is my first version of the mastermind game.

My idea is to replace the color in the standard game by number from 0 to 5. (there are 6 colors in the original game).
In the beggining of the game, a random combinaison of 4 numbers is selected by an "ai".

The goal for the player is to find these 4 numbers in the right order.

To do that, player have 10 tries.
Every try, player give 4 numbers.

If a number is good AND at the good place --> return "o"
If a number is good BUT NOT at the good place --> return "x"
If a number is not good --> return nothing

If the player find the answer before the end of his 10 tries, he win, otherwise, he loose.
"""

#========
# MODULES
#========

import random
import os


#___________ CODE ___________#

def start_game():
    """
    This function select randomly 4 numbers. This is the code that the player should find to win.

    Returns:
        code [list] : the code to find.
    """

    # Select 4 random numbers using a lambda function in a list comprehension
    obj = [(lambda x: random.randint(0,5))(x) for x in range(4)] 
    
    return obj


def comparaison(nb1 : list , nb2 : str):
    """
    This function is used to compare the number entered by the player and the code to find.

    Args:
        nb1 (list): this is the code to find.
        nb2 (int): this is the number entered by the player.

    Returns:
        nb2 (list) : the number given by the player in list format.
        good_number (int) : the number of good number in the player's code.
        good_position (int) : the number of good number at the good position in the player's code.
    """

    # Fisrt I convert the number of the player in a list
    nb2 = list(nb2)

    # Now I convert all items in this list in integer
    nb2 = [(lambda x: int(x))(x) for x in nb2]

    # I create a copy of the code to find because if I delete some number inside, the whole suite will move to the left.
    copy_nb1 = nb1.copy()

    # First I will check if the numbers are good, without taking care of the position
    good_number = 0 # variable which count the number of good numbers
    for number in nb2:
        if number in copy_nb1:
            good_number += 1
            copy_nb1.remove(number) # we have to remove the good number from the nb1_copy to not count twice a good number.

    # Now I want to count the number of good number AND at the good position
    ind_good_position = [] # I use this list to stock the index of the good numbers at the correct position
    good_position = 0
    for i in range(len(nb2)):
        if nb2[i] == nb1[i]:
            good_position +=1
            good_number -= 1 # Very important to retire one here to not count twice a number both in good and good+good_position (because good_number is already implicit in good_position)
            ind_good_position.append(i) # I add the index of the good number at the good position in my list
    
    # print(f"Good number : {good_number}")
    # print(f"Good position : {good_position}")

    return nb2, good_number, good_position


def print_board(attempts: list, good_number: int, good_position: int):
    """
    This function is used to print the board game.
    I want something like this :

    ********************
    _________________
    |   |   |   |   |
    | ? | ? | ? | ? |
    |___|___|___|___|

    x : (number)
    o : (number)

    *********************

    Where "?" are the numbers given by the player,
    "x" give the number of good number
    "o" give the number of good number at the good position 

    Args:
        attempt (list) : the code given by the player

    Returns:
        board [ ] : the board game.
    """

    print(f"_________________")
    print(f"|   |   |   |   |")
    for tries in attempts:
        print(f"| {tries[0]} | {tries[1]} | {tries[2]} | {tries[3]} |")
    print(f"|___|___|___|___|")
    print()
    print(f"x : {good_number}")
    print(f"o : {good_position}")

    return True 


if __name__ == '__main__':
    # start_game()
    # print(comparaison([1,2,3,4], '4213'))
    # print_board([1,2,3,4])

    # START GAME
    code = start_game()

    # PLAY 
    running = True
    life = 10
    old_attempts = []

    while running:
        choice = input("Try : ") # We take the player's choice

        choice, good_number, good_position = comparaison(code, choice)
        old_attempts.append(choice)

        # PRINT BOARD
        print_board(old_attempts, good_number=good_number, good_position=good_position)

        # VICTORY / LOOSE
        if good_position == 4:
            print(f"YOU WIN IN {10-life} shots.")
            running = False
        elif good_position != 4:
            life -= 1
            
        # CHECK PLAYER'S LIFE
        if life <= 0:
            print("YOU LOOSE...")
            running = False

    print("*** END ***")

# NOTES
"""
I have to add the number of "o" and "x" next to each line !
And maybe add a os.system('clear') in the print_board() function to clear the terminal each turn.
"""