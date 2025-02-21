'''1. Gambler
a. Desc -> Simulates a gambler who start with $stake and place fair $1 bets until
he/she goes broke (i.e. has no money) or reach $goal. Keeps track of the number of
times he/she wins and the number of bets he/she makes. Run the experiment N
times, averages the results, and prints them out.
b. I/P -> $Stake, $Goal and Number of times
c. Logic -> Play till the gambler is broke or has won
d. O/P -> Print Number of Wins and Percentage of Win and Loss.'''

import random


def play_round(stake, goal):
    bets = 0
    while stake > 0 and stake < goal:
        bets += 1
      
        if random.random() < 0.5: 
            stake += 1 
        else:
            stake -= 1  
    return stake == goal, bets  


def gambler_simulation(stake, goal, trials):
    wins = 0
    total_bets = 0

    for _ in range(trials):
        won, bets = play_round(stake, goal)
        total_bets += bets
        if won:
            wins += 1

    
    win_percentage = (wins / trials) * 100
    loss_percentage = 100 - win_percentage

    print(f"Total Wins: {wins}")
    print(f"Total Bets Made: {total_bets}")
    print(f"Win Percentage: {win_percentage:.2f}%")
    print(f"Loss Percentage: {loss_percentage:.2f}%")


if __name__ == "__main__":
    stake = int(input("Enter the initial stake: "))
    goal = int(input("Enter the goal amount: "))
    trials = int(input("Enter the number of times to play: "))

    gambler_simulation(stake, goal, trials)
