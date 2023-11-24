import secrets

def board_filled(board):
    for row in board:
        if '_' in row:
            return False
    return True

def check_winner(board,x,y):
    # check diagonal
    if x == y and board[0][0] == board[1][1] == board[2][2]:
        return True
    elif x == 2 - y and board[0][2] == board[1][1] == board[2][0]:
        return True
    # check vertical and horizontal
    elif board[x][0] == board[x][1] == board[x][2] or board[0][y] == board[1][y] == board[2][y]:
        return True
    
    return False

def print_board(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j], end = " ")
        print()
    print()

def game():
    player1 = 'x' if secrets.SystemRandom().randint(0,1) == 0 else 'o' # set x and o as player 1 or player 2
    player2 = 'x' if player1 == 'o' else 'o'
    print("Player 1 is", player1)
    print("Player 2 is", player2)
    print()
    board = [ ['_' for i in range(3)]
            for i in range(3)]

    turn = 1
    while(not board_filled(board)):
        print("Player",turn, "Turn")
        x,y = input("Enter cell coordinates:").split()
        x = int(x)
        y = int(y)
        if(board[x][y] != '_'):
            print("Cell already filled. Try again")
            continue
        else:
            board[x][y] = player1 if turn == 1 else player2
            print_board(board)
        
        if(check_winner(board,x,y)):
            print("Player 1 won." if turn == 1 else "Player 2 won.")
            return
        turn = 1 if turn == 2 else 2
    print("Match is a draw")

if __name__ == "__main__":
    game()
