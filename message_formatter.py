"""
name: connection_creator.py
this concentrates all the possible message formatters into one object
"""
from consts import MessageTypes
from message_formatters import InviteMessageFormatter, AcceptMessageFormatter


class MessageFormatter:

    def __init__(self):
        self.formatters = {MessageTypes.INVITE_GAME_MESSAGE_NAME: InviteMessageFormatter.get_formatted_message,
                           MessageTypes.ACCEPT_GAME_MESSAGE_NAME: AcceptMessageFormatter.get_formatted_message}
