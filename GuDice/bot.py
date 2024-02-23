# -*- encoding:utf-8 -*-
from GuDice import API


class Bot(API):
    bot_result = {}

    def __init__(self, host: str, port: int):
        super().__init__(host, port)

    def reply(self, message):
        self.bot_result = {
            "reply": message,
            "auto_escape": False,
            "auto_reply": False
        }

    def result(self):
        result = self.bot_result
        self.bot_result = {}
        return result
