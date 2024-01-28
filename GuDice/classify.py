# -*- encoding:utf-8 -*-

from GuDice.event import Event, MessageData, NoticeData


class Classify:
    type: str = None

    def __init__(self, data: dict):
        self.data = data
        print(data)
        if data['post_type'] == "message":
            if data['message_type'] == "private":
                self.private_message()
                self.type = "private_message"
            elif data['message_type'] == "group":
                self.group_message()
                self.type = "group_message"
        elif data['post_type'] == "notice":
            if data['sub_type'] == "poke":
                self.poke()
                self.type = "poke"

    def private_message(self):
        data = MessageData()
        data.user_id = self.data["user_id"]
        data.user_nick = self.data["sender"]["nickname"]
        data.sub_type = self.data["sub_type"]
        data.type = self.data["message"][0]["type"]
        data.message = self.data["raw_message"]
        self.data = data
        print("私聊消息 QQ：{} 昵称：{} 内容：{}".format(data.user_id, data.user_nick, data.message))

    def group_message(self):
        data = MessageData()
        data.user_id = self.data["user_id"]
        data.user_nick = self.data["sender"]["nickname"]
        data.group_id = self.data["group_id"]
        data.sub_type = self.data["sub_type"]
        data.type = self.data["message"][0]["type"]
        data.message = self.data["raw_message"]
        self.data = data
        print("群聊消息 QQ：{} 群昵称：{} 内容：{}".format(data.user_id, data.user_nick, data.message))

    def poke(self):
        data = NoticeData()

    def result(self):
        return [self.type, self.data]
