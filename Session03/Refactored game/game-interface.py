from random import randint
from game import Game

def tictactoe():
    game = Game()
    print("Player 1 is", game.players[0])
    print("Player 2 is", game.players[1])
    print()
    
    while(not game.is_board_full()):
        print("Player",game.turn, "Turn")
        x,y = input("Enter cell coordinates:").split()
        x = int(x)
        y = int(y)
        game.play_move(x,y)
        if(game.check_winner(x,y)):
            print("Player 1 won." if game.turn == 1 else "Player 2 won.")
            return
    print("Match is a draw")

if __name__ == "__main__":
    tictactoe()