import random, sys

print('ROCK, PAPER, SCISSORS')

# These variables keep track of wins/losses/ties

wins = 0
losses = 0
ties = 0


while True:
    # Main Loop
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True:
        # Player input loop
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            # Correct input received, breaking
            break

    # Display what the player chose
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')

    # Display what the computer chose
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')

    # Display and record results
    if playerMove == computerMove:
        print('It is a tie!')
        ties += 1
    elif playerMove == 'r' and computerMove == 's':
        print('You Win!')
        wins += 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You Win!')
        wins += 1
    elif playerMove == 's' and computerMove == 'p':
        print('You Win!')
        wins += 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1

