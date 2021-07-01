# import libraries
import random
import os

gameRunning = True


# wall of text
def text_wall(text):
    os.system('cls')
    print('=' * 45)
    print(f"\n{text}\n")
    print('=' * 45)


# defining the whole program
def rps():
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

    text_wall(
        f" OK! We are playing until {points} points\n Current Points:\n Player: {player_Points}\n Computer: {computer_Points}\n Ties: {total_Ties}")

    # game mechanics
    def game(totalTies, playerPoints, computerPoints):
        while True:
            userAction = input('Enter a choice (1.rock, 2.paper, 3.scissors): ')
            while userAction.lower() not in possibleInputs:
                print('Wrong Input, Try Again')
                userAction = input('Enter a choice (1.rock, 2.paper, 3.scissors): ')
            userAction = possibleInputs[userAction.lower()]
            computerAction = possibleInputs[random.randint(1, 3)]
            scoreboard = f" OK! We are playing until {points} points\n Current Points:\n Player: {playerPoints}\n Computer: {computerPoints}\n Ties: {totalTies}"
            print(f"\nYour choice {userAction}, computer's choice {computerAction}.\n")
            if userAction == computerAction:
                totalTies += 1
                text_wall(scoreboard)
                print(f"Both players selected {userAction}. It's a tie!\n")
            elif userAction == 'rock':
                if computerAction == 'scissors':
                    playerPoints += 1
                    text_wall(scoreboard)
                    print('Rock > scissors! You win!\n')
                else:
                    computerPoints += 1
                    text_wall(scoreboard)
                    print('Paper > rock! You lose.\n')
            elif userAction == 'paper':
                if computerAction == 'rock':
                    playerPoints += 1
                    text_wall(scoreboard)
                    print('Paper > rock! You win!\n')
                else:
                    computerPoints += 1
                    text_wall(scoreboard)
                    print('Scissors > paper! You lose.\n')
            elif userAction == 'scissors':
                if computerAction == 'paper':
                    playerPoints += 1
                    text_wall(scoreboard)
                    print('Scissors > paper! You win!\n')
                else:
                    computerPoints += 1
                    text_wall(scoreboard)
                    print('Rock > scissors! You lose.\n')

            if playerPoints == int(points):
                text_wall(
                    f" YOU WIN!\n You got {points} and won the game.\n Computer Points: {computerPoints}\n Ties: {totalTies}")
                break
            elif computerPoints == int(points):
                text_wall(
                    f" YOU LOSE!\n Computer got {points} and won the game.\n Your Points: {playerPoints}\n Ties: {totalTies}")
                break

    game(total_Ties, player_Points, computer_Points)

    # repeating it
    repeatGame = input("Would Like to Play Again? (Y/N)")
    repeatAnswer = dict.fromkeys(['y', 'yes'], 'Yes')
    repeatAnswer.update(dict.fromkeys(['n', 'no'], 'No'))
    while repeatGame.lower() not in repeatAnswer:
        print('Wrong Input, Try Again')
        repeatGame = input("Would Like to Play Again? (Y/N)")
    if not repeatAnswer[repeatGame.lower()] == 'Yes':
        text_wall("Thank You For Playing!")
        os.system('pause')
        quit()
    else:
        rps()


# running the whole program 
rps()
