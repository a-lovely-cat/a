"""
name: response_parser.py
this concentrates all the possible response parsers into one object
"""
from consts import MessageTypes, MessagePrintFormats
from response_parsers import InviteMessageParser, AcceptMessageParser, TurnMessageParser


class ResponseParser:
    """
    this class contains all of the different response parsers and functions to get
    readable parsed messages
    """

    def __init__(self):
        """
        the constructor initiates a dict containing the names of the messages that point
        to the response parse functions
        """

        self.parsers = {MessageTypes.INVITE_GAME_MESSAGE_NAME: InviteMessageParser.get_parsed_message,
                        MessageTypes.ACCEPT_GAME_MESSAGE_NAME: AcceptMessageParser.get_parsed_message,
                        MessageTypes.TURN_MESSAGE_NAME: TurnMessageParser.get_parsed_message}

    def get_turn_message_info(self, message):
        """
        this function makes returns the given turn message in a readable format
        :param message: the message we parse
        :return: the readable and parsed message
        """

        message_formatted_info = ''
        message_raw_info = self.parsers[MessageTypes.TURN_MESSAGE_NAME](message)
        if message_raw_info is None:
            return MessagePrintFormats.MESSAGE_FORMAT_FAILED_MESSAGE

        for i in range(len(MessagePrintFormats.TURN_MESSAGE_FORMAT)):
            message_formatted_info = f'{message_formatted_info}{MessagePrintFormats.TURN_MESSAGE_FORMAT[i]}' \
                                     f'{message_raw_info[i]}\n'
        return message_formatted_info
