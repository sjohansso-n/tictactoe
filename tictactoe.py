

def new_game():
    board = [' ']*9 
    player = player_choice()
    return board,player

def player_choice():
    player = ''
    while player not in ['X','O']:
        player = input('Do you want to play as X or O? ').upper()
    print('You have choosen to play as {}.'.format(player))
    return player

def place_marker(board,player):
    square = ''
    while square not in range(1,10) or not check_space(board,square):
        try:
            square = int(input('Where do you want to place your marker? Write a number between 1 and 9. '))
        except:
            pass
    index = square-1
    board[index] = player
    return board

def check_space(board,square):
    index = square-1
    if not board[index] == ' ':
        print('That square is already taken. Try again.')
    return board[index] == ' '

def display_board(board):
    zipped_board = list(zip(board[::3],board[1::3],board[2::3]))[::-1]
    row = ' {} | {} | {}  '
    line = '-----------'
    for a,b,c in zipped_board[:2]:
        print(row.format(a,b,c))
        print(line)
    for a,b,c in zipped_board[2:3]:
        print(row.format(a,b,c))

def switch_player(player):
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
    return player

def check_win(board):
    winner_rows = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a,b,c in winner_rows:
        if board[a] != ' ' and board[a] == board[b] == board[c]:
            return True
        else:
            continue
    return False

def check_lock(board):
    winner_rows = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    counter = len(winner_rows)
    for a,b,c in winner_rows:
        markers = ['X','O']
        for x in a,b,c:
            try:
                markers.remove(board[x])
            except:
                pass
        if len(markers) == 0:
            counter -= 1
    if counter == 0:
        return True
    return False

def start_over():
    start_again = ''
    while start_again not in ('y','n'):
        start_again = input("Do you want to play again? [y/n] ").lower()
    return start_again == 'y'

def start_game():

    board,player = new_game()
    
    while True:
        while True:
            board = place_marker(board,player)
            display_board(board)
            win = check_win(board)
            lock = check_lock(board)
            
            if not win and not lock:
                player = switch_player(player)
            else:
                if win:
                    print("\nCongratulations {}! You've won!".format(player))
                else:
                    print("\nThe board is crowded. No one can win!")
                break
        if not start_over():
            break
        board,player = new_game()

    print('Thank you for a good game!')

def main():
    start_game()

if __name__ == '__main__':
    main()









