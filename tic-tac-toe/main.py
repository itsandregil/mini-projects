def print_board(board: list[list[str]]):
    print("\n".join(map(lambda row: " | ".join(row), board)))


def map_position(position: int) -> tuple[int, int]:
    row = (position - 1) // 3
    col = (position - 1) % 3
    return row, col


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = players[0]
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
    has_winner = False
    is_draw = False

    while True:
        # Print the board
        print_board(board)

        # Get player input
        user_input = int(input(f"Player {current_player}, choose a position: "))
        row, col = map_position(user_input)

        # Update board
        if board[row][col] == " ":
            board[row][col] = current_player

        # Check for winner or draw
        for case in winning_cases:
            count_symbol = 0
            for index in case:
                row, col = map_position(index)
                if board[row][col] == current_player:
                    count_symbol += 1

            if count_symbol == 3:
                has_winner = True

        num_not_empty_cells = 0
        for row in board:
            for value in row:
                if value != " ":
                    num_not_empty_cells += 1

        if num_not_empty_cells == 9:
            is_draw = True

        if has_winner:
            print(f"Player {current_player} wins!")
            break

        if is_draw:
            print("It is a draw!")
            break

        # Change turn
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    main()
