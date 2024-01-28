# -*- encoding:utf-8 -*-
from GuDice.api import API
from GuDice.dice import Dice


class Event:
    def __init__(self, data):
        self.bot_api = API("127.0.0.1", 5700)
        self.data = data
        if self.data[0] == "group_message":
            self.group_message()

    def private_message(self):
        pass

    def group_message(self):
        data = self.data[1]
        if data.message == ".d" or data.message.startswith(
                ".d") or data.message == "。d" or data.message.startswith("。d"):
            r2d10 = Dice(1, 100)
            self.bot_api.send_group_msg(str(data.group_id), r2d10.dice_result_text()["result_text"])
        if data.message == (".bot") or data.message.startswith(
                ".bot") or data.message == "。bot" or data.message.startswith("。bot"):
            self.bot_api.send_group_msg(str(data.group_id), "GuDice By Baigugu\nVer. 0.0.1dev(24)\n一只测试姬")


class MessageData:
    user_id: int
    group_id: int
    user_nick: str
    sub_type: str
    type: str
    message: str


class NoticeData:
    user_id: int
    group_id: int
    user_nick: str
