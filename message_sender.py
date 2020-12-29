"""
name: connection_creator.py
this handles sending messages here
"""


class MessageSender:
    """
    this class is responsible for sending out messages to the given client using the
    socket it is given in the constructor
    """

    def __init__(self, player_socket):
        """
        this is the constructor for this class
        :param player_socket: the players socket
        """

        self.player_socket = player_socket

    def send_message(self, message):
        """
        this function sends the given message to the other player
        :param message: the message we send
        """

        self.player_socket.send(message)
