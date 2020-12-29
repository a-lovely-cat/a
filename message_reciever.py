"""
name: connection_creator.py
this handles receiving messages here
"""
from consts import SocketCommunication


class MessageReceiver:
    """
    this class is responsible for receiving messages from the given client using the
    socket it is given in the constructor
    """

    def __init__(self, player_socket):
        """
        this is the constructor for this class
        :param player_socket: the players socket
        """

        self.player_socket = player_socket

    def get_received_message(self):
        """
        this function returns the message from the other player
        """

        return self.player_socket.recv(SocketCommunication.MAX_RECEIVE_AMOUNT)
