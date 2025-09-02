from board import Board
from player import Player

def make_move(board: Board, player: Player):
    row, col = player.get_move()
    if board.grid[row][col] != " ":
        raise Exception("Invalid position, try again.")    
    board.grid[row][col] = player.symbol

def main():
    board = Board()
    player1 = Player("Player1", "X")
    player2 = Player("Player2", "O")

    while True:
        if board.is_full():
            break
        
        for player in (player1, player2):
            try:
                board.display()
                make_move(board, player)
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    main()
