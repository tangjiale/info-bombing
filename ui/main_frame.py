# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"消息轰炸器", pos = wx.DefaultPosition, size = wx.Size( 482,232 ), style = wx.DEFAULT_FRAME_STYLE|wx.RESIZE_BORDER|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer_main = wx.BoxSizer( wx.VERTICAL )

		sbSizer_path = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"路径选择" ), wx.HORIZONTAL )

		self.m_staticText_path_file = wx.StaticText( sbSizer_path.GetStaticBox(), wx.ID_ANY, u" 消息文件(txt)：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_path_file.Wrap( -1 )

		sbSizer_path.Add( self.m_staticText_path_file, 0, wx.ALL, 5 )

		self.m_filePicker_path_file = wx.FilePickerCtrl( sbSizer_path.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"选择消息文件", u"*.txt", wx.DefaultPosition, wx.Size( 350,-1 ), wx.FLP_DEFAULT_STYLE )
		sbSizer_path.Add( self.m_filePicker_path_file, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )


		bSizer_main.Add( sbSizer_path, 0, wx.EXPAND, 5 )

		sbSizer_config = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"配置" ), wx.HORIZONTAL )

		self.m_staticText_config_interval = wx.StaticText( sbSizer_config.GetStaticBox(), wx.ID_ANY, u"发送间隔(秒):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_config_interval.Wrap( -1 )

		sbSizer_config.Add( self.m_staticText_config_interval, 0, wx.ALL, 5 )

		self.m_spinCtrlDouble_config_interval = wx.SpinCtrlDouble( sbSizer_config.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.SP_ARROW_KEYS, 0, 100, 0.5, 1 )
		self.m_spinCtrlDouble_config_interval.SetDigits( 0 )
		sbSizer_config.Add( self.m_spinCtrlDouble_config_interval, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )

		self.m_staticText_config_order = wx.StaticText( sbSizer_config.GetStaticBox(), wx.ID_ANY, u"发送顺序：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_config_order.Wrap( -1 )

		sbSizer_config.Add( self.m_staticText_config_order, 0, wx.ALL, 5 )

		m_choice_config_orderChoices = [ u"顺序", u"倒序", u"随机", u"循环" ]
		self.m_choice_config_order = wx.Choice( sbSizer_config.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_config_orderChoices, 0 )
		self.m_choice_config_order.SetSelection( 0 )
		sbSizer_config.Add( self.m_choice_config_order, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )

		self.m_staticText_config_time = wx.StaticText( sbSizer_config.GetStaticBox(), wx.ID_ANY, u"轰炸时间(秒):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_config_time.Wrap( -1 )

		sbSizer_config.Add( self.m_staticText_config_time, 0, wx.ALL, 5 )

		self.m_spinCtrlDouble_config_time = wx.SpinCtrlDouble( sbSizer_config.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10000, 30, 1 )
		self.m_spinCtrlDouble_config_time.SetDigits( 0 )
		sbSizer_config.Add( self.m_spinCtrlDouble_config_time, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )


		bSizer_main.Add( sbSizer_config, 0, wx.EXPAND, 5 )

		sbSizer_start = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"启动" ), wx.HORIZONTAL )


		sbSizer_start.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText5 = wx.StaticText( sbSizer_start.GetStaticBox(), wx.ID_ANY, u"执行后", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		sbSizer_start.Add( self.m_staticText5, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )

		self.m_spinCtrlDouble_start = wx.SpinCtrlDouble( sbSizer_start.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.SP_ARROW_KEYS, 0, 100, 3, 1 )
		self.m_spinCtrlDouble_start.SetDigits( 0 )
		sbSizer_start.Add( self.m_spinCtrlDouble_start, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )

		self.m_staticText6 = wx.StaticText( sbSizer_start.GetStaticBox(), wx.ID_ANY, u"秒后开始启动", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		sbSizer_start.Add( self.m_staticText6, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )

		self.m_button_start = wx.Button( sbSizer_start.GetStaticBox(), wx.ID_ANY, u"执行", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		sbSizer_start.Add( self.m_button_start, 1, 0, 5 )


		sbSizer_start.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer_main.Add( sbSizer_start, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer_main )
		self.Layout()
		self.m_statusBar = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_filePicker_path_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_file_changed )
		self.m_button_start.Bind( wx.EVT_BUTTON, self.on_button_click_execute )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def on_file_changed( self, event ):
		event.Skip()

	def on_button_click_execute( self, event ):
		event.Skip()


