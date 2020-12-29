"""
name: connection_creator.py
this creates the connection in both possible ways
"""
from consts import SocketCommunication


class ConnectionCreator:
    """
    this class holds the connection creating functions
    """

    @staticmethod
    def create_connection(creator_socket):
        """
        this function is responsible for listening out for the guest to join and
        return his socket
        :param creator_socket: our socket
        :return: the opponent's socket
        """

        creator_socket.bind((SocketCommunication.LISTEN_IP, SocketCommunication.CONNECTION_PORT))
        creator_socket.listen(SocketCommunication.MAX_RECEIVED_CLIENTS)
        opponent_socket, _ = creator_socket.accept()
        return opponent_socket

    @staticmethod
    def connect_to_game(player_socket, host_ip):
        """
        this function make sure to connect the player to the game host in the given ip
        :param player_socket: our socket
        :param host_ip: the host's ip
        """

        player_socket.connect((host_ip, SocketCommunication.CONNECTION_PORT))
