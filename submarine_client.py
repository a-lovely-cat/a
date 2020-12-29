"""
name: submarine_client.py
this provides the client itself that exports the game functions
"""
from communication_manager import CommunicationManager
from message_formatter import MessageFormatter
from consts import MessageTypes


# TODO finish all the formatters and then make the parsers and change the formatters if anything doesnt work

class SubmarineClient:

    def __init__(self):
        """
        this is the client class constructor
        """

        self.communication_manager = CommunicationManager()
        self.message_formatter = MessageFormatter()

    def create_game_connection(self):
        """
        this function creates the connection and handles the game inviting and accepting
        """

        self.communication_manager.create_connection()
        self.communication_manager.send_message(
            self.message_formatter.formatters[MessageTypes.INVITE_GAME_MESSAGE_NAME]())
        guest_accept_message = self.communication_manager.get_received_message()
        # TODO check the accept message

    def connect_to_game(self, opponent_ip):
        """
        this function connects to the host and handles the game inviting and accepting
        """

        self.communication_manager.connect_to_game(opponent_ip)
        guest_accept_message = self.communication_manager.get_received_message()
        # TODO check the accept message
        self.communication_manager.send_message(
            self.message_formatter.formatters[MessageTypes.INVITE_GAME_MESSAGE_NAME]())

    def send_placing_confirmation(self, placing_hash):
        """
        this function sends the placing confirmation hash message to the opponent
        :param placing_hash: the placing hash we send
        """

        self.communication_manager.send_message(
            self.message_formatter.formatters[MessageTypes.PLACING_INFORM_MESSAGE_NAME](placing_hash))

    def print_opponent_placing_confirmation(self):
        pass

    def send_guess_turn(self, block_column, block_row):
        """
        this function sends the guess turn message to the opponent
        :param block_column: the column of the guess block
        :param block_row: the row of the guess block
        """

        self.communication_manager.send_message(
            self.message_formatter.formatters[MessageTypes.TURN_MESSAGE_NAME](block_column, block_column))

    def print_opponent_guess_turn(self):
        pass

    def send_opponent_turn_result(self, did_hit, sunken_ship):
        """
        this function sends the turn result to the opponent
        :param did_hit: whether the opponent has hit a submarine
        :param sunken_ship: the sunken ship code, it is 0 if the ship did not sink
        """

        self.communication_manager.send_message(
            self.message_formatter.formatters[MessageTypes.TURN_RESULT_MESSAGE_NAME](did_hit, sunken_ship))

    def send_placement_inform_message(self):
        pass

    def print_opponent_placement_inform_message(self):
        pass
