"""
name: submarine_client.py
this provides the client itself that exports the game functions
"""
from communication_manager import CommunicationManager
from message_formatter import MessageFormatter
from consts import MessageTypes


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
            self.message_formatter.formatters[MessageTypes.INVITE_GAME_MESSAGE_NAME])
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
            self.message_formatter.formatters[MessageTypes.INVITE_GAME_MESSAGE_NAME])

    def send_placing_confirmation(self):
        pass

    def print_opponent_placing_confirmation(self):
        pass

    def guess_turn(self):
        pass

    def print_opponent_guess_turn(self):
        pass

    def send_opponent_turn_result(self):
        pass

    def send_placement_inform_message(self):
        pass

    def print_opponent_placement_inform_message(self):
        pass
