import secrets


class Game:
    def __init__(self):
        self.players = ['x','o'] if secrets.SystemRandom().randint(0,1) == 0 else ['o','x']
        self.turn = 1
        self.board = [ ['_' for i in range(3)]
                                for i in range(3)]

    def play_move(self,x,y):
        if(self.board[x][y] != '_'):
            print("Cell already filled. Try again")
            return self.play_move(x,y)
        else:
            self.board[x][y] = self.players[self.turn-1]
            self.print_board()

    def is_board_full(self):
        for row in self.board:
            if '_' in row:
                return False
        return True

    def check_winner(self,x,y):
        # check diagonal
        if x == y and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return True
        elif x == 2 - y and self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return True
        # check vertical and horizontal
        elif self.board[x][0] == self.board[x][1] == self.board[x][2] or self.board[0][y] == self.board[1][y] == self.board[2][y]:
            return True
        
        self.turn = 1 if self.turn == 2 else 2
        return False

    def print_board(self):
        for i in range(3):
            for j in range(3):
                print(self.board[i][j], end = " ")
            print()
        print()
