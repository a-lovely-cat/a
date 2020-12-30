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


class Submarines:
    """
    this class contains all the submarine codes
    """

    NO_SUBMARINE = 0
    FIVE_LONG_SUBMARINE = 1
    FOUR_LONG_SUBMARINE = 2
    FIRST_THREE_LONG_SUBMARINE = 3
    SECOND_THREE_LONG_SUBMARINE = 4
    TWO_LONG_SUBMARINE = 5

    IS_VERTICAL = 1
    IS_HORIZONTAL = 0


class MessageTypes:
    """
    this class contains all the message type names
    """

    INVITE_GAME_MESSAGE_NAME = 'invite_game'
    INVITE_GAME_MESSAGE_CODE = 1

    ACCEPT_GAME_MESSAGE_NAME = 'accept_game'
    ACCEPT_GAME_MESSAGE_CODE = 2

    PLACING_INFORM_MESSAGE_NAME = 'placing_inform'
    PLACING_INFORM_MESSAGE_CODE = 3

    TURN_MESSAGE_NAME = 'turn'
    TURN_MESSAGE_CODE = 4

    TURN_RESULT_MESSAGE_NAME = 'turn_result'
    TURN_RESULT_MESSAGE_CODE = 5

    PLACEMENT_INFORM_MESSAGE_NAME = 'placement_inform'
    PLACEMENT_INFORM_MESSAGE_CODE = 6


class MessagePrintFormats:
    """
    this class contains the printout formats of all the messages
    """

    TURN_MESSAGE_FORMAT = ('version: ', 'message type: ', 'block hash: ')

    MESSAGE_FORMAT_FAILED_MESSAGE = 'the message has come is the wrong format'


