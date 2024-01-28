# -*- encoding:utf-8 -*-
import json
from GuDice import Classify, API, Event

from flask import Flask, request
from gevent import pywsgi

app = Flask(__name__)


# 根目录
@app.route('/', methods=['POST', 'GET'])
def arknights_draw():
    student = request.data.decode('utf-8')
    # 获取到POST过来的数据，因为我这里传过来的数据需要转换一下编码。根据晶具体情况而定
    student_json = json.loads(student)
    # 把区获取到的数据转为JSON格式。
    data = Classify(student_json).result()
    Event(data)
    return {"status": "ok", "retcode": 0}


def server_start(mode="", host="127.0.0.1", port=5900):
    if mode == "debug":
        app.run(debug=True)
        print("测试环境")
    else:
        try:
            server = pywsgi.WSGIServer((host, port), app)
            print("图片服务器已启动：http://" + host + ":" + str(port))
            server.serve_forever()
        except OSError:
            print("端口被占用，请修改端口")
            input("回车关闭")


if __name__ == "__main__":
    server_start()
