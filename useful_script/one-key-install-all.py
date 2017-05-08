# -*- coding: utf-8 -*-
"""
一键安装当前目录的python安装包
指支持当前目录。
"""

import argparse
import os
import subprocess
import glob

class CommandWorker(object):
    cmd_pattern = ['pip install {}', ]

    def __init__(self):
        parser = argparse.ArgumentParser(description='one key to install current directory.')

        # self.args_dict = vars(parser.parse_args())
        self.all_files = self.get_all_file()

    def run(self, arg_lists):
        for one in arg_lists:
            subprocess.call(one)

    def make_commands(self):
        for file in self.all_files:
            cmd1 = CommandWorker.cmd_pattern[0].format(file).split()
            yield cmd1

    def get_all_file(self):
        whl_file = glob.glob('*.whl')
        source_file = glob.glob('*.tar.gz')
        files = whl_file + source_file
        return files


if __name__ == '__main__':
    commander = CommandWorker()
    commands = list(commander.make_commands())
    commander.run(commands)
