from board import Board
from player import Player

def main():
    board = Board()
    player = Player("Player1", "X")

    while True:
        try:
            board.display()
            move = player.make_move()
            board.update(move, player.symbol)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
