"""
name: message_formatter.py
this concentrates all the possible message formatters into one object
"""
from consts import MessageTypes
from message_formatters import InviteMessageFormatter, AcceptMessageFormatter, PlacingInformMessageFormatter, \
    TurnMessageFormatter, TurnResultMessageFormatter, PlacementInformMessageFormatter


class MessageFormatter:
    """
    this class contains all of the different message formatters
    """

    def __init__(self):
        """
        the constructor initiates a dict containing the names of the messages that point
        to the message format function
        """
        self.formatters = {MessageTypes.INVITE_GAME_MESSAGE_NAME: InviteMessageFormatter.get_formatted_message,
                           MessageTypes.ACCEPT_GAME_MESSAGE_NAME: AcceptMessageFormatter.get_formatted_message,
                           MessageTypes.PLACING_INFORM_MESSAGE_NAME:
                               PlacingInformMessageFormatter.get_formatted_message,
                           MessageTypes.TURN_MESSAGE_NAME: TurnMessageFormatter.get_formatted_message,
                           MessageTypes.TURN_RESULT_MESSAGE_NAME: TurnResultMessageFormatter.get_formatted_message,
                           MessageTypes.PLACEMENT_INFORM_MESSAGE_NAME:
                               PlacementInformMessageFormatter.get_formatted_message}
