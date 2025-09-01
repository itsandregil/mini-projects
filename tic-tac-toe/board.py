class Board:
    def __init__(self):
        self.grid = [[" " for _ in range(3)] for _ in range(3)]

    def display(self) -> None:
        for row in self.grid:
            print(f"| {' | '.join(row)} |")

    def update(self, position: tuple[int, int], symbol: str) -> None:
        self.grid[position[0]][position[1]] = symbol

    def is_full(self) -> bool:
        return