"""
name: game_board.py
this provides the game board, it basically handles the offline part of the game
"""
from consts import BoardParameters, Submarines

#this class also calculates the placement hash
class GameBoard:

    def __init__(self):
        """
        the constructor makes an empty board and resets all the submarines as None
        """

        self.board = [[0 for _ in range(BoardParameters.BOARD_LENGTH)] for _ in range(BoardParameters.BOARD_LENGTH)]
        self.submarine1 = None
        self.submarine2 = None
        self.submarine3 = None
        self.submarine4 = None
        self.submarine5 = None

    def get_board_printable(self):
        """
        this function prints the board in a nice format
        """

        formatted_board = ''
        for row in self.board:
            for block in row:
                formatted_board = f'{formatted_board}{block} '
            formatted_board = f'{formatted_board}\n'
        return formatted_board

    def check_add_submarine_parameters(self, submarine_identifier, submarine_column, submarine_row, submarine_angle):
        """
        this function makes sure to raise an exception in any case when the given parameters are invalid
        it makes sure that the submarine is in a place that wont throw it off the map and that the parameters
        are valid
        :param submarine_identifier: the submarine identifier
        :param submarine_column: the column we start adding in
        :param submarine_row: the row we start adding in
        :param submarine_angle: the angle we place the submarine in
        """
        if (submarine_angle != Submarines.IS_HORIZONTAL) and (submarine_angle != Submarines.IS_VERTICAL):
            raise ValueError(Submarines.INVALID_ANGLE_ERROR)
        if submarine_angle == Submarines.IS_HORIZONTAL:
            if (submarine_column <= BoardParameters.MINIMUM_BORDER_BLOCK + Submarines.SUBMARINE_LENGTHS[
                submarine_identifier] or submarine_column > BoardParameters.MAXIMUM_BOARDER_BLOCK) or (
                    submarine_row < BoardParameters.MINIMUM_BORDER_BLOCK or submarine_row >
                    BoardParameters.MAXIMUM_BOARDER_BLOCK):
                raise ValueError(Submarines.INVALID_PLACEMENT_ERROR)
        else:
            if (
                    submarine_column < BoardParameters.MINIMUM_BORDER_BLOCK or submarine_column >
                    BoardParameters.MAXIMUM_BOARDER_BLOCK) or (
                    submarine_row <= BoardParameters.MINIMUM_BORDER_BLOCK +
                    Submarines.SUBMARINE_LENGTHS[submarine_identifier]
                    or submarine_row > BoardParameters.MAXIMUM_BOARDER_BLOCK):
                raise ValueError(Submarines.INVALID_PLACEMENT_ERROR)
        if not (Submarines.FIVE_LONG_SUBMARINE <= submarine_identifier <= Submarines.TWO_LONG_SUBMARINE):
            raise ValueError(Submarines.INVALID_SUBMARINE_IDENTIFIER_ERROR)

    def add_submarine(self, submarine_identifier, submarine_column, submarine_row, submarine_angle):
        """
        this function palces the submarine according to the given parameters and saves it as a new member
        :param submarine_identifier: the identifier of the submarine
        :param submarine_column: the column we place it
        :param submarine_row: the row we place it
        :param submarine_angle: the angle it is places in
        """

        self.check_add_submarine_parameters(submarine_identifier, submarine_column, submarine_row, submarine_angle)
        #I didnt finish this, what happens here is that it places the submarine according to the angle with the
        #known length, I also wanted to save the submarine so it could be used for the protocol


    def add_block(self, submarine_identifier, block_column, block_row):
        """
        this function adds a submarine to the given block if there are no other submarines around it
        :param submarine_identifier: the submarine we add
        :param block_column: the column we add in
        :param block_row: the row we add in
        :except ValueError: in the case when there are other submarines around the submarine/in the block
        """

        # this is a rather disgusting if statement that simply checks if there are any other submarines
        #  in the outer ring of the block (or in it)
        if ((self.board[block_row][block_column] != 0) or (
                self.board[block_row + 1][block_column] != 0 and self.board[block_row + 1][
            block_column] != submarine_identifier) or (
                self.board[block_row - 1][block_column] != 0 and self.board[block_row - 1][
            block_column] != submarine_identifier) or (
                self.board[block_row][block_column + 1] != 0 and self.board[block_row][
            block_column + 1] != submarine_identifier) or (
                self.board[block_row][block_column - 1] != 0 and self.board[block_row][
            block_column - 1] != submarine_identifier) or (
                self.board[block_row + 1][block_column + 1] != 0) or (
                self.board[block_row + 1][block_column - 1] != 0) or (
                self.board[block_row - 1][block_column + 1] != 0) or (
                self.board[block_row - 1][block_column - 1] != 0)):
            raise ValueError(Submarines.INVALID_PLACEMENT_ERROR)
        self.board[block_row][block_column] = submarine_identifier
