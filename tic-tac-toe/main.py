import random

Board = list[list[str]]
Move = tuple[int, int]
Player = str


def print_board(board: Board):
    print("\n".join(map(lambda row: " | ".join(row), board)))


def map_position(position: int) -> tuple[int, int]:
    row = (position - 1) // 3
    col = (position - 1) % 3
    return row, col


def get_position(position: int, board: Board):
    row, col = map_position(position)
    return board[row][col]


def switch_turn(current_player: Player) -> str:
    return "X" if current_player == "O" else "O"


def check_winner(board: Board, player: Player) -> bool:
    winning_cases = [
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        (1, 4, 7),
        (2, 5, 8),
        (3, 6, 9),
        (1, 5, 9),
        (3, 5, 7),
    ]

    return any(
        all(
            value == player for value in map(lambda pos: get_position(pos, board), case)
        )
        for case in winning_cases
    )


def check_draw(num_moves: int) -> bool:
    return num_moves == 9


def validate_move(position: int, board: Board) -> None:
    if position < 1 or position > 9:
        raise Exception("Invalid move. Positions should be between 1 - 9")
    if get_position(position, board) != " ":
        raise Exception("Invalid move. Position is already taken.")
    return


def make_move(board: Board, player: Player) -> Board:
    while True:
        try:
            player_input = int(input(f"Player {player}, choose a position: "))
            validate_move(player_input, board)

            # If nothing is raised we update the board
            row, col = map_position(player_input)
            board[row][col] = player
            return board
        except Exception as e:
            print(f"Error: {e}")


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = random.choice(["X", "O"])
    moves_count = 0

    while True:
        print_board(board)
        board = make_move(board, current_player)
        moves_count += 1

        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break

        if check_draw(moves_count):
            print("It is a draw!")
            break

        current_player = switch_turn(current_player)


if __name__ == "__main__":
    main()
