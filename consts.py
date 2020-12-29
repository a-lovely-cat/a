"""
name: connection_creator.py
this contains all the consts for this
"""

PROTOCOL_VERSION = 1


class SocketCommunication:
    """
    this class contains all the socket communication constants
    """

    MAX_RECEIVE_AMOUNT = 21000

    CONNECTION_PORT = 8300
    LISTEN_IP = '0.0.0.0'

    MAX_RECEIVED_CLIENTS = 1


class MessageTypes:
    """
    this class contains all the message type names
    """

    INVITE_GAME_MESSAGE_NAME = 'invite_game'
    INVITE_GAME_MESSAGE_CODE = 1

    ACCEPT_GAME_MESSAGE_NAME = 'accept_game'
    ACCEPT_GAME_MESSAGE_CODE = 2
