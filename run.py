#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-08-13 14:44
# @Author  : jiale
# @Site    :
# @File    : run.py
# @Software: PyCharm
"""
启动类
"""
import wx
from ui import main
from loguru import logger

if __name__ == '__main__':
    """
    程序入口
    """
    logger.add('out.log')
    app = wx.App(False)
    frame = main.Main(None)
    frame.Show(True)
    try:
        # 检测更新
        # upgradespider.check()
        app.MainLoop()

    except Exception as err:
        logger.error('程序发生异常: {}', err)
        raise