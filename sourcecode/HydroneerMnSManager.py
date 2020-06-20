# -*- coding: utf-8 -*-

###########################################################################
## Hydroneer MOD & SAVE Manager
## written by Raziel23x
## 
## Copyright 2020
###########################################################################

import pathlib
import os
import sys
import subprocess
import wx
import wx.adv
import wx.xrc
import wx.dataview
import ctypes


from sys import exit
from pathlib import Path

wx.ID_ModList = 1000
wx.ID_SaveFiles = 1001
wx.ID_FileExit = 1002
wx.ID_ToolsAssetEditor = 1003
wx.ID_ToolsHydroneerSaveEditor = 1004
wx.ID_HelpAbout = 1005

###########################################################################
## Class FrameMain
###########################################################################

class FrameMain ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Hydroneer MOD & Save Manager by Raziel23x", pos = wx.DefaultPosition, size = wx.Size( 844,641 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizerFrameMain = wx.BoxSizer( wx.VERTICAL )

		bSizerMainFrame = wx.BoxSizer( wx.VERTICAL )

		self.panelMain = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizerTabs = wx.BoxSizer( wx.VERTICAL )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.notebookModSaves = wx.Notebook( self.panelMain, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.panelMods = wx.Panel( self.notebookModSaves, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panelMods.SetToolTip( u"List of Mods installed" )

		bSizerMods = wx.BoxSizer( wx.VERTICAL )

		bSizerModDir = wx.BoxSizer( wx.VERTICAL )

		self.dataViewListCtrlMods = wx.dataview.DataViewListCtrl( self.panelMods, wx.ID_ModList, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerModDir.Add( self.dataViewListCtrlMods, 0, wx.ALL|wx.EXPAND, 0 )


		bSizerMods.Add( bSizerModDir, 0, wx.ALL|wx.EXPAND, 0 )


		self.panelMods.SetSizer( bSizerMods )
		self.panelMods.Layout()
		bSizerMods.Fit( self.panelMods )
		self.notebookModSaves.AddPage( self.panelMods, u"Mod List", False )
		self.panelSaves = wx.Panel( self.notebookModSaves, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panelSaves.SetToolTip( u"List of Save files" )

		bSizerSaves = wx.BoxSizer( wx.VERTICAL )

		bSizerSaveDir = wx.BoxSizer( wx.VERTICAL )

		self.dataViewListCtrlSaves = wx.dataview.DataViewListCtrl( self.panelSaves, wx.ID_SaveFiles, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerSaveDir.Add( self.dataViewListCtrlSaves, 0, wx.ALL|wx.EXPAND, 0 )


		bSizerSaves.Add( bSizerSaveDir, 0, wx.ALL|wx.EXPAND, 0 )


		self.panelSaves.SetSizer( bSizerSaves )
		self.panelSaves.Layout()
		bSizerSaves.Fit( self.panelSaves )
		self.notebookModSaves.AddPage( self.panelSaves, u"Save Files", True )

		bSizer4.Add( self.notebookModSaves, 0, wx.EXPAND |wx.ALL, 0 )


		bSizerTabs.Add( bSizer4, 0, wx.ALL|wx.EXPAND, 0 )


		self.panelMain.SetSizer( bSizerTabs )
		self.panelMain.Layout()
		bSizerTabs.Fit( self.panelMain )
		bSizerMainFrame.Add( self.panelMain, 0, wx.EXPAND |wx.ALL, 0 )


		bSizerFrameMain.Add( bSizerMainFrame, 0, wx.ALL|wx.EXPAND, 0 )


		self.SetSizer( bSizerFrameMain )
		self.Layout()
		self.menubarMain = wx.MenuBar( 0 )
		self.menuFile = wx.Menu()
		self.menuItemFileExit = wx.MenuItem( self.menuFile, wx.ID_FileExit, u"Exit"+ u"\t" + u"Alt+f4", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuFile.Append( self.menuItemFileExit )

		self.menubarMain.Append( self.menuFile, u"File" )

		self.menuTools = wx.Menu()
		self.menuItemToolsAssetEditor = wx.MenuItem( self.menuTools, wx.ID_ToolsAssetEditor, u"Asset Editor", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuTools.Append( self.menuItemToolsAssetEditor )

		self.menuItemToolsHydroneerSaveEditor = wx.MenuItem( self.menuTools, wx.ID_ToolsHydroneerSaveEditor, u"Hydroneer Save Editor", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuTools.Append( self.menuItemToolsHydroneerSaveEditor )

		self.menubarMain.Append( self.menuTools, u"Tools" )

		self.menuHelp = wx.Menu()
		self.menuItemHelpAbout = wx.MenuItem( self.menuHelp, wx.ID_HelpAbout, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuHelp.Append( self.menuItemHelpAbout )

		self.menubarMain.Append( self.menuHelp, u"Help" )

		self.SetMenuBar( self.menubarMain )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.menuItemFileExitOnMenuSelection, id = self.menuItemFileExit.GetId() )
		self.Bind( wx.EVT_MENU, self.menuItemToolsAssetEditorOnMenuSelection, id = self.menuItemToolsAssetEditor.GetId() )
		self.Bind( wx.EVT_MENU, self.menuItemToolsHydroneerSaveEditorOnMenuSelection, id = self.menuItemToolsHydroneerSaveEditor.GetId() )
		self.Bind( wx.EVT_MENU, self.menuItemHelpAboutOnMenuSelection, id = self.menuItemHelpAbout.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def menuItemFileExitOnMenuSelection( self, event ):
		 sys.exit() 

	def menuItemToolsAssetEditorOnMenuSelection( self, event ):
		os.startfile('Tools\\Asset Editor.exe')

	def menuItemToolsHydroneerSaveEditorOnMenuSelection( self, event ):
		os.startfile('Tools\\HydroneerSaveEdit.exe')

	def menuItemHelpAboutOnMenuSelection( self, event ):
		wx.MessageBox('Hydroneer MOD & SAVE Manager \n Written By \n Raziel23x', 'About', wx.OK | wx.ICON_INFORMATION)
		

class MainApp (wx.App) :
        def OnInit(self):
                mainFrame = FrameMain(None)
                mainFrame.Show(True)
                return True
if __name__ == '__main__':
        app = MainApp()
        app.MainLoop()

