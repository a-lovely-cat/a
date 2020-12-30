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
        formatted_message = struct.pack('ii', PROTOCOL_VERSION, MessageTypes.PLACING_INFORM_MESSAGE_CODE, placing_hash)
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
    def get_formatted_message(did_hit, sunken_submarine):
        formatted_message = struct.pack('ii?i', PROTOCOL_VERSION, MessageTypes.TURN_RESULT_MESSAGE_CODE, did_hit,
                                        sunken_submarine)
        return formatted_message


class PlacementInformMessageFormatter:
    """
    this class is in charge of formatting the placement inform message
    """

    @staticmethod
    def get_formatted_message(submarine1, submarine2, submarine3, submarine4, submarine5):
        formatted_message = struct.pack('iii?i?i?i?i?', PROTOCOL_VERSION, MessageTypes.PLACEMENT_INFORM_MESSAGE_CODE,
                                        submarine1.get_submarine_block_hash(), submarine1.submarine_angle,
                                        submarine2.get_submarine_block_hash(), submarine2.submarine_angle,
                                        submarine3.get_submarine_block_hash(), submarine3.submarine_angle,
                                        submarine4.get_submarine_block_hash(), submarine4.submarine_angle,
                                        submarine5.get_submarine_block_hash(), submarine5.submarine_angle)
        return formatted_message
