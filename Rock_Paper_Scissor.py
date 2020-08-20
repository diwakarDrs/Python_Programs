import random

def number_name (number):
    # This function will take a number and convert it to it's string value
    if number == 1:
        return 'rock'
    if number == 2:
        return 'paper'
    if number == 3:
        return 'scissor'
    else:
        return 'Invalid Number'

def name_number (name):
    # This function will take a name and convert it to it's number value
    if name == 'rock':
        return 1
    if name == 'paper':
        return 2
    if name == 'scissor':
        return 3
    else:
        return 'Invalid Name'

def rock_paper_scissor():
    # Get user input
    user = input("Do you want to choose rock, paper, scissor: ")
    user_number = name_number(user)

    # Get computer input
    comp_number = random.randint(1,3)
    comp = number_name(comp_number)

    # results of the game
    result = (user_number - comp_number)%3

    # Set string with winner name
    if result == 1:
        winner = 'winner is Player'
    elif result == 2:
        winner = 'winner is Computer'
    elif result == 0:
        winner = 'winner is Tie'
    else:
        winner = 'Invalid winner'

    # Print the result
    print("Player chooses : ", user)
    print("Computer chooses : ", comp)
    print("Result: ",winner)

    r =input("Press ENTER to continue or press Q to quit :")
    if r=='q':
        return
    else:
        rock_paper_scissor()


rock_paper_scissor()




    
    
