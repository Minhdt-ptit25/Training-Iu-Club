import random
options = ("rock", "paper", "scissors")
gameRunning = True

while gameRunning:
    
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice(rock, paper, scissors): ")

    print(f'Player: {player}')
    print(f'Computer: {computer}')


    if player == computer:
        print('It\'s a tie')
        player = input("Enter a choice(rock, paper, scissors): ")
    else:
        if player == 'rock' and computer == 'scissors':
            print("YOU WIN")
            
        elif player == 'rock' and computer == 'paper':
            print("YOU LOSE")
            
        elif player == 'scissors' and computer == 'paper':
            print("YOU WIN")
            
        elif player == 'scissors' and computer == 'rock':
            print("YOU LOSE")
            
        elif player == 'paper' and computer == 'rock':
            print('YOU WIN')
            
        elif player == 'paper' and computer == 'scissors':
            print('YOU LOSE')
            

