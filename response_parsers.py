"""
name: response_parsers
this provides all the response parsers
"""
import struct


class InviteMessageParser:
    """
    this class is in charge of parsing the invite message
    """

    @staticmethod
    def get_parsed_message(message):
        try:
            parsed_message = struct.unpack('ii', message)
            return parsed_message
        except struct.error:
            return False


class AcceptMessageParser:
    """
    this class is in charge of parsing the accept message
    """

    @staticmethod
    def get_parsed_message(message):
        try:
            parsed_message = struct.unpack('ii', message)
            return parsed_message
        except struct.error:
            return False


class PlacingInformMessageParser:
    """
    this class is in charge of parsing the placing inform message
    """

    @staticmethod
    def get_parsed_message(placing_hash):
        formatted_message = struct.pack('ii', PROTOCOL_VERSION, MessageTypes.PLACING_INFORM_MESSAGE_CODE)
        formatted_message += placing_hash
        return formatted_message


class TurnMessageParser:
    """
    this class is in charge of parsing the turn message
    """

    @staticmethod
    def get_parsed_message(message):
        try:
            parsed_message = struct.unpack('iii', message)
            return parsed_message
        except struct.error:
            return False


class TurnResultMessageParser:
    """
    this class is in charge of parsing the turn result message
    """

    @staticmethod
    def get_parsed_message(did_hit, sunken_ship):
        formatted_message = struct.pack('ii', PROTOCOL_VERSION, MessageTypes.TURN_RESULT_MESSAGE_CODE)
        formatted_message += struct.pack('?', did_hit)
        formatted_message += struct.pack('i', sunken_ship)
        return formatted_message


class PlacementInformMessageParser:
    """
    this class is in charge of parsing the placement inform message
    """

    @staticmethod
    def get_parsed_message(submarine1, submarine2, submarine3, submarine4, submarine5):
        formatted_message = struct.pack('ii', PROTOCOL_VERSION, MessageTypes.PLACEMENT_INFORM_MESSAGE_CODE)
        formatted_message += struct.pack('i?', submarine1.get_submarine_block_hash(), submarine1.submarine_angle)
        formatted_message += struct.pack('i?', submarine2.get_submarine_block_hash(), submarine2.submarine_angle)
        formatted_message += struct.pack('i?', submarine3.get_submarine_block_hash(), submarine3.submarine_angle)
        formatted_message += struct.pack('i?', submarine4.get_submarine_block_hash(), submarine4.submarine_angle)
        formatted_message += struct.pack('i?', submarine5.get_submarine_block_hash(), submarine5.submarine_angle)
        return formatted_message
