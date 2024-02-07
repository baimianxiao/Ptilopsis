# -*- encoding:utf-8 -*-

class Event:

    def private_message(self, event, bot):
        pass

    def group_message(self, event, bot):
        pass

    def main(self, data, bot):
        if data[1] == "private_message":
            self.private_message(data, bot)
        elif data[1] == "group_message":
            self.group_message(data, bot)


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
