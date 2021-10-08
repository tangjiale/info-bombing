#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-09-29 10:35
# @Author  : tangjiale
# @Desc    : 
# @File    : main.py
# @Software: PyCharm
import wx
import time
from constant import constant
from ui import main_frame
from ui.progress.progress import Progress
from utils import pathutil


class Main(main_frame.MainFrame):
    def __init__(self, parent):
        main_frame.MainFrame.__init__(self, parent)
        self.icon = wx.Icon(
            pathutil.resource_path(constant.APP_BITMAP_TYPE_ICO),
            wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
        self.m_statusBar.SetFieldsCount(3)
        # self.m_statusBar.SetStatusWidths([-1, -2, -1])
        self.m_statusBar.SetStatusText('  软件版本：' + constant.APP_VERSION_STRING, 0)

    def on_file_changed(self, event):
        # # 文件路径
        # file_path = self.m_filePicker_path_file.GetPath()
        # # 读取文件
        # with open(file_path, 'r', encoding='u8') as f:
        #     lines = f.readlines()
        # self.SetStatusText("进度：0/%d" % len(lines), 2)
        pass

    def on_button_click_execute(self, event):
        # 文件路径
        file_path = self.m_filePicker_path_file.GetPath()
        if len(file_path) == 0:
            self.show_message("消息文件路径不能为空")
            return

        # 读取文件
        with open(file_path, 'r', encoding='u8') as f:
            lines = f.readlines()
        # 消息总条数
        length = len(lines)
        if length == 0:
            self.show_message("消息数据为空")
            return
        time.sleep(self.m_spinCtrlDouble_start.GetValue())
        # 获取间隔时间
        sleep_seconds = self.m_spinCtrlDouble_config_interval.GetValue()
        dlg = Progress(self, lines, sleep_seconds)
        # 初始化状态值
        # dlg.update_process(total=length, current_num=0)
        dlg.ShowModal()

    # 统一显示对话框
    # @param message (str): 对话框内容
    def show_message(self, message):
        wx.MessageDialog(self, message, '操作提醒', wx.OK).ShowModal()
