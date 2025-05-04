class GameInterface:
    header_line = "=" * 70

    def __init__(self, stock_size, computer_pieces, snake_pieces, human_pieces_str):
        self.stock_size = stock_size
        self.computer_pieces = computer_pieces
        self.snake_string = self.pieces_to_str(snake_pieces)
        self.human_pieces_str = human_pieces_str

    def __str__(self):
        return (f"{self.header_line}\n"
                f"Stock size: {self.stock_size}\n"
                f"Computer pieces: {self.computer_pieces}\n\n"
                f"{self.snake_string}\n\nYour pieces:\n"
                f"{self.human_pieces_str}\n")

    @staticmethod
    def pieces_to_str(pieces):
        temp_str = ""
        for piece in pieces:
            temp_str += f"{piece}"

        return temp_str