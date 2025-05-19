import random

class StockDominoes:
    """ Represents stock of dominoes from which the pieces are drawn by players. """

    def __init__(self):
        """ Build the pool of domino pieces. The pieces are built, and then the elements are shuffled. """
        stock_pieces_result = []
        for i in range(7):
            for j in range(7):
                temp_list = [i, j]
                random.shuffle(temp_list)
                if temp_list not in stock_pieces_result and temp_list[::-1] not in stock_pieces_result:
                    stock_pieces_result.append(temp_list)

        random.shuffle(stock_pieces_result)

        self.pieces = stock_pieces_result


    def draw_dominoes(self, how_many=7):
        result = []
        for x in range(how_many):
            index = random.randint(0, len(self.pieces) - 1)
            result.append(self.pieces.pop(index))

        return result

    def __repr__(self):
        return f"StockDominoes: pieces={self.pieces}"
