import random 
import sys

# If no 'oracle' is supplied on the command line, choose machine plays
# randomly.  Otherwise use the supplied oracle.
HAS_ORACLE = ( len(sys.argv) > 1 )
if HAS_ORACLE: MACHINE_ORACLE = sys.argv[1]

# This is a global variable that indexes into the 'oracle' to select
# the next machine play.
machinePlayCounter = 0

def machinePlay ():
    """The machine chooses one of the three moves randomly,
    unless there's an oracle passed on the command line.  Then
    we choose machine plays from that."""
    global machinePlayCounter
    if HAS_ORACLE and machinePlayCounter < len(MACHINE_ORACLE):
        play = MACHINE_ORACLE[ machinePlayCounter ]
        machinePlayCounter += 1
    else:
        play = random.choice(["1", "2", "3"])
    return play

def gamePrint():
    print("Choose your play: ")
    print("Enter 1 for rock;")
    print("Enter 2 for paper;")
    print("Enter 3 for scissors;")
    print("Enter 4 to exit:", end=" ")

def endSession():
    print()
    print("--- End of Session ---")
    print("Games Completed: ", games)
    print()
    print("Wins:", wins)
    print("Win Rate:", format(winRate, "0.1%"))
    print()
    print("Losses: ", losses)
    print("Loss Rate: ", format(lossRate, "0.1%"))
    print()
    print("Draws: ", draws)
    print("Draw Rate: ", format(drawRate, "0.1%"))


print()
print("Welcome to a game of Rock, Paper, Scissors!")


wins = 0
losses = 0
draws = 0
x = 0
games = 0
win = "Congratulations, you won!"
loss = "Sorry, you lost!"
draw = "There's no winner. Try again!"
winRate = wins/games
lossRate = losses/games
drawRate = draws/games

import random

while True:
    
    gamePrint()
    playerItem = input()
    if playerItem not in {"1", "2", "3", "4"}:
        print("Illegal play entered. Try again!")
        print()
        continue
    if playerItem == "4":
        break
    
    games += 1

    ROCK = "1"
    PAPER = "2"
    SCISSORS = "3"

    myItem = machinePlay()
    if myItem == ROCK:
        myItemName = "rock"
    if myItem == PAPER:
        myItemName = "paper"
    if myItem == SCISSORS:
        myItemName = "scissors"

    
    if playerItem == myItem:
        result = draw
        draws += 1
        continue
    if playerItem == ROCK:
        playerItemName = "rock"
        if myItem == SCISSORS:
            result = win
        else:
            result = win
    elif playerItem == PAPER:
        playerItemName = "paper"
        if myItem == ROCK:
            result = loss
        else:
            result = loss
    elif playerItem == SCISSORS:
        playerItemName = "scissors"
        if myItem == PAPER:
            result = win
        else:
            result = loss
    if result == win:
        wins += 1
    elif result == loss:
        losses += 1


    print("You played", playerItemName + "; your opponent played", myItemName)
    print(result)
    print()


winRate = wins/games
lossRate = losses/games
drawRate = draws/games



endSession()

    
