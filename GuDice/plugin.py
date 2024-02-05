import os
import sys
import importlib
from os.path import abspath, dirname, join, exists


class PluginManager:
    plugin_dir = abspath('../plugin')
    plugin_list = []

    def __init__(self):
        if self.plugin_dir not in sys.path:
            sys.path.append(self.plugin_dir)
        self.test = None

    def plugin_registered(self):
        for item in os.scandir(self.plugin_dir):
            if item.is_dir():
                if (exists(join(self.plugin_dir, item.name, "config.toml"))
                        and exists(join(self.plugin_dir, item.name, "main.py"))):
                    self.test = importlib.import_module(item.name)
                else:
                    print(item.name + "缺失文件")

    def plugin_run(self):

        pass

    def plugin_test(self):
        pass


if __name__ == "__main__":
    Manager = PluginManager()
    Manager.plugin_registered()
    print(Manager.test.data)
