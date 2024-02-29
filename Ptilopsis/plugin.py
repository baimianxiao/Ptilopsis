# -*- encoding:utf-8 -*-
from os import getcwd, scandir
import sys
import importlib
from os.path import abspath, join, exists, dirname
from Ptilopsis import Event, API

# 常用库导入
import sqlite3
import onedice


class PluginManager:
    main_dir = getcwd()
    plugin_dir = join(main_dir, 'plugin')
    plugin_list = []

    def __init__(self):
        if self.plugin_dir not in sys.path:
            sys.path.append(self.plugin_dir)
        print("插件管理器加载成功")
        self.test = None

    def plugin_registered(self):
        for item in scandir(self.plugin_dir):
            if item.is_dir():
                if (exists(join(self.plugin_dir, item.name, "config.toml"))
                        and exists(join(self.plugin_dir, item.name, "main.py"))):
                    plugin_object = importlib.import_module(item.name)
                    plugin_object = plugin_object.main.PluginEvent()
                    plugin_object.init()
                    self.plugin_list.append(plugin_object)
                else:
                    print(item.name + "缺失文件")

    def plugin_event(self, event, bot):
        plugin_result = {}
        for plugin_object in self.plugin_list:
            plugin_result = plugin_object.main(event, bot)
        return plugin_result

    def plugin_hot_reload(self):
        pass

    def plugin_test(self):
        pass


# 插件基类
class Plugin(Event):
    def __init__(self):
        self.bot = None

    def init(self):
        pass

    def main(self, event, bot):
        self.bot = bot
        if event['type'] == "private_message":
            self.private_message(event['data'], self.bot)
        elif event['type'] == "group_message":
            self.group_message(event['data'], self.bot)
        elif event['type'] == "group_poke":
            self.group_poke(event['data'], self.bot)
        return self.bot.result()


if __name__ == "__main__":
    Manager = PluginManager()
    Manager.plugin_registered()
    print(Manager.test.data)
    print(Manager.plugin_dir)
