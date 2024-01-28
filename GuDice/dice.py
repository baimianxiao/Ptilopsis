# -*- encoding:utf-8 -*-

from random import randint


class Dice:
    result = {
        "result_number": 0,
        "result_list": [],
        "result_text": "",
    }

    def __init__(self, number: int, face: int):
        self.number = number
        self.face = face

    def dice_result(self):
        result_list = []
        for i in range(self.number):
            result_list.append(randint(1, self.face))
            self.result["result_number"] = sum(result_list)
            self.result["result_list"] = result_list
        return self.result

    def dice_result_text(self):
        result = self.dice_result()
        text = str(result["result_list"][0])
        for i in result["result_list"][1:]:
            text = text + "+" + str(i)
        result["result_text"] = "{}d{} {}={}".format(self.number, self.face, text, result["result_number"])
        return result


if __name__ == "__main__":
    print(Dice(3, 6).dice_result_text())
