# -*- encoding:utf-8 -*-
import ctypes
import os, sys
import json
from os.path import join
from gevent import monkey, pywsgi

monkey.patch_all()  # 打上猴子补丁

from Ptilopsis import Bot, Classify, Event, PluginManager
from Ptilopsis.util import log_output
from flask import Flask, request, Response, make_response, send_file

app = Flask(__name__)

main_dir = os.getcwd()


# 根目录
@app.route('/', methods=['POST', 'GET'])
def bot():
    data = request.data.decode('utf-8')
    data_json = json.loads(data)
    # 把区获取到的数据转为JSON格式。
    event = Classify(data_json).result()
    result = Manager.plugin_event(event, bot)
    return result


@app.route("/data/<path:imageId>", methods=['POST', 'GET'])
def plugin_image(imageId):
    try:
        response = make_response(send_file(join(main_dir, "data", imageId)))
        response.headers["Content-Type"] = "image/jpeg"
        return response
    except BaseException as error:
        return {"code": '503', "data": str(error), "message": "图片不存在"}


def server_start(mode="", host="127.0.0.1", port=5900):
    if mode == "debug":
        app.run(debug=True)
        log_output("测试环境")
    else:
        try:
            server = pywsgi.WSGIServer((host, port), app, log=None)
            log_output("post服务器已启动：http://" + host + ":" + str(port))
            server.serve_forever()
        except OSError:
            log_output("端口被占用，请修改端口", "WARNING")
            input("回车关闭")


if __name__ == "__main__":
    version = "version:0.0.7(7)"
    log_output(version)
    ctypes.windll.kernel32.SetConsoleTitleW("Ptilopsis " + version)
    Manager = PluginManager()
    Manager.plugin_registered()
    bot = Bot("127.0.0.1", 5700)
    server_start()
