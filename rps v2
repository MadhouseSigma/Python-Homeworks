# import libraries
import random
import os

# wall of text
def text_wall(text):
    print('=' * 45)
    print(f"\n{text}\n")
    print('=' * 45)


# defining the whole program into a function
def rps():
    os.system('cls')
    text_wall(" Let's play Rock, Paper, Scissors!\n Made by: Masoud Ghasemi")

    # number of points
    points = input('Enter Number of Points to Win:')
    while not points.isnumeric():
        print('Wrong Input, Try Again')
        points = input('Enter Number of Points to Win:')
    player_Points = 0
    computer_Points = 0
    total_Ties = 0

    # make dict with possible inputs
    possibleInputs = dict.fromkeys(['1', 'rock', 'r', 'sang', 's', 1], 'rock')
    possibleInputs.update(dict.fromkeys(['2', 'paper', 'p', 'kaghaz', 'k', 2], 'paper'))
    possibleInputs.update(dict.fromkeys(['3', 'scissors', 's', 'gheichi', 'g', 3], 'scissors'))

    os.system('cls')
    text_wall(f" OK! We are playing until {points} points\n Current Points:\n Player: {player_Points}\n "
              f"Computer: {computer_Points}\n Ties: {total_Ties}")

    # game mechanics into a function
    def game(totalTies, playerPoints, computerPoints):
        while True:
            # take user input and process it
            userAction = input('Enter a choice (1.rock, 2.paper, 3.scissors): ')
            while userAction.lower() not in possibleInputs:
                print('Wrong Input, Try Again')
                userAction = input('Enter a choice (1.rock, 2.paper, 3.scissors): ')
            userAction = possibleInputs[userAction.lower()]

            # computer chooses random option
            computerAction = possibleInputs[random.randint(1, 3)]

            os.system('cls')

            # both choices are processed and the results is printed
            if userAction == computerAction:
                totalTies += 1
                print(f"Both players selected {userAction}. It's a tie!\n")
            elif userAction == 'rock':
                if computerAction == 'scissors':
                    playerPoints += 1
                    print('You: Rock > AI: Scissors! You win!\n')
                else:
                    computerPoints += 1
                    print('AI: Paper > You: Rock! You lose.\n')
            elif userAction == 'paper':
                if computerAction == 'rock':
                    playerPoints += 1
                    print('You: Paper > AI: Rock! You win!\n')
                else:
                    computerPoints += 1
                    print('AI: Scissors > You: Paper! You lose.\n')
            elif userAction == 'scissors':
                if computerAction == 'paper':
                    playerPoints += 1
                    print('You: Scissors > AI: Paper! You win!\n')
                else:
                    computerPoints += 1
                    print('AI: Rock > You: Scissors! You lose.\n')

            # scoreboard
            text_wall(
                f" We are playing until {points} points\n Current Points:\n Player: {playerPoints}\n "
                f"Computer: {computerPoints}\n Ties: {totalTies}")

            if playerPoints == int(points):
                text_wall(
                    f" YOU WIN!\n You got {points} and won the game.\n "
                    f"Computer Points: {computerPoints}\n Ties: {totalTies}")
                break
            elif computerPoints == int(points):
                text_wall(
                    f" YOU LOSE!\n Computer got {points} and won the game.\n "
                    f"Your Points: {playerPoints}\n Ties: {totalTies}")
                break

    game(total_Ties, player_Points, computer_Points)

    # repeating it if user want to play again
    repeatGame = input("Would you Like to Play Again? (Y/N)")
    repeatAnswer = dict.fromkeys(['y', 'yes'], 'Yes')
    repeatAnswer.update(dict.fromkeys(['n', 'no'], 'No'))
    while repeatGame.lower() not in repeatAnswer:
        print('Wrong Input, Try Again')
        repeatGame = input("Would you Like to Play Again? (Y/N)")
    if not repeatAnswer[repeatGame.lower()] == 'Yes':
        text_wall("Thank You For Playing!")
        os.system('pause')
        quit()
    else:
        rps()


# running the whole program
rps()
