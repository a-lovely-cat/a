"""
name: connection_creator.py
this provides the communication manager for this
"""
import socket
from connection_creator import ConnectionCreator
from message_sender import MessageSender
from message_reciever import MessageReceiver


class CommunicationManager:

    def __init__(self):
        """
        this is the class constructor
        it only makes the initial player's socket
        """

        self.player_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.opponent_socket = None
        self.message_sender = None
        self.message_receiver = None

    def create_connection(self):
        """
        this function creates the connection and initiates our message sender and receiver
        it also adds the opponent socket as we are the host this time
        """

        self.opponent_socket = ConnectionCreator.create_connection(self.player_socket)
        self.message_sender = MessageSender(self.opponent_socket)
        self.message_receiver = MessageReceiver(self.opponent_socket)

    def connect_to_game(self, opponent_ip):
        """
        this function creates the connection and initiates our message sender and receiver
        """

        ConnectionCreator.connect_to_game(self.player_socket, opponent_ip)
        self.message_sender = MessageSender(self.opponent_socket)
        self.message_receiver = MessageReceiver(self.opponent_socket)

    def send_message(self, message):
        """
        this function wraps the message sender send
        :param message: the message we send
        """

        self.message_sender.send_message(message)

    def get_received_message(self):
        """
        this function wraps the receive message from the message receiver
        """

        return self.message_receiver.get_received_message()

    def close_connection(self):
        """
        this function closes all the available sockets
        """

        self.player_socket.close()
        if self.opponent_socket is not None:
            self.opponent_socket.close()
