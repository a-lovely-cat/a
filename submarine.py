"""
name: submarine.py
this provides a class that handles a single submarine
"""


class Submarine:
    """
    this class represents a single submarine
    """

    def __init__(self, block_column, block_row, submarine_angle, submarine_identifier):
        """
        this is the class constructor
        :param block_column: the submarines starting block column
        :param block_row: the submarines starting block row
        :param submarine_angle: the submarine's angle
        :param submarine_identifier: the submarine's identifier
        """

        self.block_column = block_column
        self.block_row = block_row
        self.submarine_angle = submarine_angle
        self.submarine_identifier = submarine_identifier

    def get_submarine_block_hash(self):
        """
        this function returns the submarine's block hash
        :return: the full block hash of the submarine
        """

        return self.block_column + (10 * self.block_row)
