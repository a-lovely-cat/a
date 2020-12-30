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

    SUBMARINE_LENGTHS = {FIVE_LONG_SUBMARINE: 5, FOUR_LONG_SUBMARINE: 4, FIRST_THREE_LONG_SUBMARINE: 3,
                         SECOND_THREE_LONG_SUBMARINE: 3, TWO_LONG_SUBMARINE: 2}

    IS_VERTICAL = 1
    IS_HORIZONTAL = 0

    INVALID_ANGLE_ERROR = 'invalid angle'
    INVALID_SUBMARINE_IDENTIFIER_ERROR = 'invalid submarine identifier'
    DUPLICATE_SUBMARINE_ERROR = 'this submarine is already on the board'
    INVALID_PLACEMENT_ERROR = 'invalid placement'


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
    PLACEMENT_INFORM_MESSAGE_FORMAT = (
        'version: ', 'message type: ', 'sub1 location: ', 'sub1 is horizontal: ', 'sub2 location: ',
        'sub2 is horizontal: ',
        'sub3 location: ', 'sub3 is horizontal: ', 'sub4 location: ', 'sub4 is horizontal: ', 'sub5 location: ',
        'sub5 is horizontal: ', 'nonce: ')
    TURN_RESULT_MESSAGE_FORMAT = ('version: ', 'message type: ', 'did hit: ', 'did sink: ')

    MESSAGE_FORMAT_FAILED_MESSAGE = 'the message has come is the wrong format'


class BoardParameters:
    """
    this class contains all the board constants
    """

    BOARD_LENGTH = 10
    MAXIMUM_BOARDER_BLOCK = 9
    MINIMUM_BORDER_BLOCK = 0

    NONCE_SIZE = 4
