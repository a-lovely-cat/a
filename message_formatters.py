"""
name: message_formatters.py
this file has all the message formatters
"""
import struct
from consts import MessageTypes, PROTOCOL_VERSION


class InviteMessageFormatter:
    """
    this class is in charge of formatting the invite message
    """

    @staticmethod
    def get_formatted_message():
        return struct.pack('ii', PROTOCOL_VERSION, MessageTypes.INVITE_GAME_MESSAGE_CODE)


class AcceptMessageFormatter:
    """
    this class is in charge of formatting the accept message
    """

    @staticmethod
    def get_formatted_message():
        return struct.pack('ii', PROTOCOL_VERSION, MessageTypes.ACCEPT_GAME_MESSAGE_CODE)


class PlacingInformMessageFormatter:
    """
    this class is in charge of formatting the placing inform message
    """

    @staticmethod
    def get_formatted_message(placing_hash):
        formatted_message = struct.pack('ii', PROTOCOL_VERSION, MessageTypes.PLACING_INFORM_MESSAGE_CODE)
        formatted_message += placing_hash
        return formatted_message


class TurnMessageFormatter:
    """
    this class is in charge of formatting the turn message
    """

    @staticmethod
    def get_formatted_message(block_column, block_row):
        block_hash = block_column + (10 * block_row)
        formatted_message = struct.pack('iii', PROTOCOL_VERSION, MessageTypes.TURN_MESSAGE_CODE, block_hash)
        return formatted_message


class TurnResultMessageFormatter:
    """
    this class is in charge of formatting the turn result message
    """

    @staticmethod
    def get_formatted_message(did_hit, sunken_ship):
        formatted_message = struct.pack('ii', PROTOCOL_VERSION, MessageTypes.TURN_RESULT_MESSAGE_CODE)
        formatted_message += struct.pack('?', did_hit)
        formatted_message += struct.pack('i', sunken_ship)
        return formatted_message
