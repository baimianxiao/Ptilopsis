# -*- encoding:utf-8 -*-
from Ptilopsis import API


class Bot(API):
    bot_result = {}

    def __init__(self, host: str, port: int):
        super().__init__(host, port)
        self.event = None

    def reply(self, message):
        self.bot_result = {
            "reply": message,
            "auto_escape": False,
            "auto_reply": False
        }

    def event(self, event):
        self.event = event

    def result(self):
        result = self.bot_result
        self.bot_result = {}
        return result
