print()
print("Welcome to Rock, Paper, Scissors. Good luck!")
print("(Enter 'exit' to finish)")
print()

wins = 0
losses = 0
draws = 0
x = 0
games = 0

import random

while True:
    playerItem = input("rock, paper, or scissors: ")
    if playerItem not in {"rock", "paper", "scissors", "exit"}:
        print("Invalid input.")
        print("Please enter 'rock', 'paper', or 'scissors'.")
        print()
        continue
    if playerItem == "exit":
        break
    
    games += 1

    x = random.randint(1,3)
    if x == 1:
        myItem = "rock"
    if x == 2:
        myItem = "paper"
    if x == 3:
        myItem = "scissors"
    
    if playerItem == myItem:
        print("Computer Plays", myItem)
        print("Draw!")
        print()
        print()
        draws += 1
        continue
    if playerItem == "rock":
        if myItem == "scissors":
            result = "You Won!"
        else:
            result = "You Lost!"
    elif playerItem == "paper":
        if myItem == "rock":
            result = "You Won!"
        else:
            result = "You Lost!"
    elif playerItem == "scissors":
        if myItem == "paper":
            result = "You Won!"
        else:
            result = "You Lost!"
    if result == "You Won!":
        wins += 1
    elif result == "You Lost!":
        losses += 1


    print("Computer plays", myItem)
    print(result)
    print()
    print()

winRate = wins/games
lossRate = losses/games
drawRate = draws/games

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

    
