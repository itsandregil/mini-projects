class Board:
    def __init__(self):
        self.grid = [[" " for _ in range(3)] for _ in range(3)]

    def display(self) -> None:
        """Displays the board into the console"""
        for row in self.grid:
            print(f"| {' | '.join(row)} |")

    def is_full(self) -> bool:
        is_full_grid = True

        for row in self.grid:
            for col in row:
                if col == " ":
                    is_full_grid = False
        return is_full_grid
    