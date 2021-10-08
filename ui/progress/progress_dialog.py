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
## Class MyDialogProgress
###########################################################################

class MyDialogProgress ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"轰炸进度", pos = wx.DefaultPosition, size = wx.Size( 352,87 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer_dialog_progress = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"执行进度：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		bSizer_dialog_progress.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_gauge = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge.SetValue( 0 )
		bSizer_dialog_progress.Add( self.m_gauge, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText_gauge = wx.StaticText( self, wx.ID_ANY, u"0/0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_gauge.Wrap( -1 )

		bSizer_dialog_progress.Add( self.m_staticText_gauge, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.SetSizer( bSizer_dialog_progress )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_ACTIVATE, self.on_activate )
		self.Bind( wx.EVT_ACTIVATE_APP, self.on_activate_app )
		self.Bind( wx.EVT_SHOW, self.on_show )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def on_activate( self, event ):
		event.Skip()

	def on_activate_app( self, event ):
		event.Skip()

	def on_show( self, event ):
		event.Skip()


