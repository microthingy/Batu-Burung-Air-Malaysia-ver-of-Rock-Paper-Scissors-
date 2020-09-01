from random import randint, choice

def rock_paper_scissors():
    player_input = input('Batu, Burung or Air: ').casefold()
    options = ['batu', 'burung', 'air']
    computer = choice(options)

    if player_input == 'batu' and computer == 'burung':
        print(f'Player: {player_input}\nComputer: {computer}')
        print('You win!')
    elif player_input == 'burung' and computer == 'air':
        print(f'Player: {player_input}\nComputer: {computer}')
        print('You win!')
    elif player_input == 'air' and computer == 'batu':
        print(f'Player: {player_input}\nComputer: {computer}')
        print('You win!')
    elif player_input == computer:
        print(f'Player: {player_input}\nComputer: {computer}')
        print('Tie!')
    else:
        print(f'Player: {player_input}\nComputer: {computer}')
        print('You lose')


rock_paper_scissors()