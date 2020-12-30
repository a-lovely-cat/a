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
    def get_parsed_message(message):
        try:
            parsed_message = struct.pack('ii', message)
            return parsed_message
        except struct.error:
            return False


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
    def get_parsed_message(message):
        try:
            parsed_message = struct.unpack('ii?i', message)
            return parsed_message
        except struct.error:
            return False


class PlacementInformMessageParser:
    """
    this class is in charge of parsing the placement inform message
    """

    @staticmethod
    def get_parsed_message(message):
        try:
            parsed_message = struct.unpack('iii?i?i?i?i?', message)
            return parsed_message
        except struct.error:
            return False
