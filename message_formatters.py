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
