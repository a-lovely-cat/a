"""
name: submarine_client.py
this provides the client itself that exports the game functions
"""
from communication_manager import CommunicationManager
from message_formatter import MessageFormatter
from response_parser import ResponseParser
from consts import MessageTypes, PROTOCOL_VERSION


class SubmarineClient:

    def __init__(self):
        """
        this is the client class constructor
        """

        self.communication_manager = CommunicationManager()
        self.message_formatter = MessageFormatter()
        self.response_parser = ResponseParser()

    def close_connection(self):
        """
        this function wraps closing the connection
        """

        self.communication_manager.close_connection()

    def create_game_connection(self):
        """
        this function creates the connection and handles the game inviting and accepting
        """

        self.communication_manager.create_connection()
        self.communication_manager.send_message(
            self.message_formatter.formatters[MessageTypes.INVITE_GAME_MESSAGE_NAME]())
        guest_accept_message = self.communication_manager.get_received_message()
        parsed_accept_message = self.response_parser.parsers[MessageTypes.ACCEPT_GAME_MESSAGE_NAME](
            guest_accept_message)

        if (parsed_accept_message is None) or (parsed_accept_message[0] != PROTOCOL_VERSION) or (
                parsed_accept_message[1] != MessageTypes.ACCEPT_GAME_MESSAGE_CODE):
            self.close_connection()

    def connect_to_game(self, opponent_ip):
        """
        this function connects to the host and handles the game inviting and accepting
        :param opponent_ip: the opponent's ip
        """

        self.communication_manager.connect_to_game(opponent_ip)
        host_invite_message = self.communication_manager.get_received_message()
        parsed_invite_message = self.response_parser.parsers[MessageTypes.INVITE_GAME_MESSAGE_NAME](
            host_invite_message)

        if (parsed_invite_message is None) or (parsed_invite_message[0] != PROTOCOL_VERSION) or (
                parsed_invite_message[1] != MessageTypes.INVITE_GAME_MESSAGE_CODE):
            self.close_connection()

        else:
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
        """
        this function prints out the givne guess turn message in a readable format
        it will print None if it is in the wrong format
        """

        guess_turn_message = self.communication_manager.get_received_message()
        print(self.response_parser.get_turn_message_info(guess_turn_message))

    def send_opponent_turn_result(self, did_hit, sunken_ship):
        """
        this function sends the turn result to the opponent
        :param did_hit: whether the opponent has hit a submarine
        :param sunken_ship: the sunken ship code, it is 0 if the ship did not sink
        """

        self.communication_manager.send_message(
            self.message_formatter.formatters[MessageTypes.TURN_RESULT_MESSAGE_NAME](did_hit, sunken_ship))

    def print_opponent_turn_result(self):
        pass

    def send_placement_inform_message(self, submarine1, submarine2, submarine3, submarine4, submarine5):
        """
        this function sends the placement inform to the opponent
        :param submarine1: the first submarine
        :param submarine2: the second submarine
        :param submarine3: the third submarine
        :param submarine4: the forth submarine
        :param submarine5: the fifth submarine
        """

        self.communication_manager.send_message(
            self.message_formatter.formatters[MessageTypes.PLACEMENT_INFORM_MESSAGE_NAME](submarine1, submarine2,
                                                                                          submarine3,
                                                                                          submarine4, submarine5))

    def print_opponent_placement_inform_message(self):
        pass
