#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-09-29 14:52
# @Author  : tangjiale
# @Desc    : 
# @File    : progress.py
# @Software: PyCharm
import wx
import time
import random
import pyperclip
import pyautogui

from ui.progress import progress_dialog


class Progress(progress_dialog.MyDialogProgress):
    def __init__(self, parent, lines, sleep_seconds):
        progress_dialog.MyDialogProgress.__init__(self, parent)
        self.count = 0
        self.lines = lines
        self.sleep_seconds = sleep_seconds
        self.m_gauge.Range = len(lines)
        self.m_gauge.Bind(wx.EVT_IDLE, self.OnIdle)
        self.update_process(len(lines), 0)

    # 更新进度条值
    def OnIdle(self, event):
        self.m_gauge.SetValue(self.count)

    # 更新标签进度值
    def update_process(self, total, current_num):
        self.m_staticText_gauge.LabelText = ("%d/%d" % (current_num, total))
        print(self.m_staticText_gauge.LabelText)

    def on_activate(self, event):
        print("on_activate")
        time.sleep(5)
        print("on_activate2")


    def on_activate_app(self, event):
        print("on_activate_app")

    def on_show(self, event):
        print("on_show")
        # self.execute()

    def execute(self):
        length = len(self.lines)
        for i in range(length):
            # 使用剪贴板复制粘贴变通实现
            # 复制中文句子内容
            pyperclip.copy(random.choice(self.lines))
            # Ctrl+v粘贴
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press("enter")
            self.update_process(total=length, current_num=i + 1)
            # self.count += 1
            time.sleep(self.sleep_seconds)
