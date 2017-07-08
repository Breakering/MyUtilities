#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Breakering"
# Date: 2017/7/7
import os


def parse_path(path, depth=0):
    """解析路径并生成目录结构"""
    for i in os.listdir(path):
        if i == "__pycache__":
            continue
        print("%s├── %s" % ("│   " * depth, i))
        new_path = os.path.join(path, i)
        if not os.path.isfile(new_path):
            parse_path(new_path, depth+1)

if __name__ == '__main__':
    path = "day13\MyStrongHold"  # 填入你想要解析的目录
    parse_path(path)