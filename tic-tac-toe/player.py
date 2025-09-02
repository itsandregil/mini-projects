from typing import Literal

Move = tuple[int, int]

class Player:
    def __init__(self, name: str, symbol: Literal["X", "O"]):
        self.name = name
        self.symbol = symbol

    def get_move(self) -> Move:
        raw_input = input("Make your move (row, col): ").split(",")
    
        if len(raw_input) > 2:
            raise Exception("Too many values, please enter (row, col)")
        
        row, col = map(lambda s: int(s.strip()) - 1, raw_input)

        if row < 0 or row > 2 or col < 0 or col > 2:
            raise Exception("Values in (row, col) should be between 1 and 3")

        return row, col