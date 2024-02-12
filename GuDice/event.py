# -*- encoding:utf-8 -*-

class Event:
    def private_message(self, data, bot):
        pass

    def group_message(self, data, bot):
        pass


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
