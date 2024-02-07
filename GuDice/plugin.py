# -*- encoding:utf-8 -*-
import os
import sys
import importlib
from os.path import abspath, join, exists, dirname

file_dir = dirname(abspath(__file__))


class PluginManager:
    plugin_dir = abspath(join(file_dir, '../plugin'))
    plugin_list = []

    def __init__(self):
        if self.plugin_dir not in sys.path:
            sys.path.append(self.plugin_dir)
        print("插件管理器加载成功")
        self.test = None

    def plugin_registered(self):
        for item in os.scandir(self.plugin_dir):
            if item.is_dir():
                if (exists(join(self.plugin_dir, item.name, "config.toml"))
                        and exists(join(self.plugin_dir, item.name, "main.py"))):
                    plugin_object = importlib.import_module(item.name)
                    self.plugin_list.append(plugin_object)
                else:
                    print(item.name + "缺失文件")

    def plugin_event(self, data, bot):
        for plugin_object in self.plugin_list:
            plugin_object.main.PluginEvent().main(data, bot)

    def plugin_test(self):
        pass


if __name__ == "__main__":
    Manager = PluginManager()
    Manager.plugin_registered()
    print(Manager.test.data)
    print(Manager.plugin_dir)
