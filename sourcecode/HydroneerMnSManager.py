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
import wx.dataview
import ctypes


from sys import exit
from pathlib import Path

wx.ID_MODLIST = 1000
wx.ID_MODLISTENABLEDISABLE = 1001
wx.ID_MODLISTBACKUP = 1002
wx.ID_SAVEFILESDELETE = 1003
wx.ID_SAVEFILESBACKUP = 1004
wx.ID_SAVEFILES = 1005
wx.ID_FileExit = 1006
wx.ID_ToolsAssetEditor = 1007
wx.ID_ToolsBlender = 1008
wx.ID_ToolsHydroneerSaveEditor = 1009
wx.ID_HelpAbout = 1010

###########################################################################
## Class FrameMain
###########################################################################

class FrameMain ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Hydroneer MOD & Save Manager by Raziel23x", pos = wx.DefaultPosition, size = wx.Size( 844,641 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizerFrameMain = wx.BoxSizer( wx.VERTICAL )

		bSizerMainFrame = wx.BoxSizer( wx.VERTICAL )

		self.notebookSAVEFILESMODS = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.panelMODLIST = wx.Panel( self.notebookSAVEFILESMODS, wx.ID_MODLIST, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizerLISTMODBUTTONS = wx.BoxSizer( wx.VERTICAL )

		bSizerMODLISTBUTTONS = wx.BoxSizer( wx.HORIZONTAL )

		self.toggleBtnMODLISTENABLEDISABLE = wx.ToggleButton( self.panelMODLIST, wx.ID_MODLISTENABLEDISABLE, u"Enable/Disable", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerMODLISTBUTTONS.Add( self.toggleBtnMODLISTENABLEDISABLE, 0, wx.ALL, 0 )

		self.toggleBtnMODLISTBACKUP = wx.ToggleButton( self.panelMODLIST, wx.ID_MODLISTBACKUP, u"Backup", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.toggleBtnMODLISTBACKUP.SetValue( True )
		bSizerMODLISTBUTTONS.Add( self.toggleBtnMODLISTBACKUP, 0, wx.ALL, 0 )


		bSizerLISTMODBUTTONS.Add( bSizerMODLISTBUTTONS, 0, wx.ALL|wx.EXPAND, 0 )

		bSizerMODLISTFOLDER = wx.BoxSizer( wx.VERTICAL )

		checkListMODLISTChoices = []
		self.checkListMODLIST = wx.CheckListBox( self.panelMODLIST, wx.ID_MODLIST, wx.DefaultPosition, wx.DefaultSize, checkListMODLISTChoices, 0 )
		bSizerMODLISTFOLDER.Add( self.checkListMODLIST, 0, wx.ALL|wx.EXPAND, 0 )


		bSizerLISTMODBUTTONS.Add( bSizerMODLISTFOLDER, 0, wx.ALL|wx.EXPAND, 0 )


		self.panelMODLIST.SetSizer( bSizerLISTMODBUTTONS )
		self.panelMODLIST.Layout()
		bSizerLISTMODBUTTONS.Fit( self.panelMODLIST )
		self.notebookSAVEFILESMODS.AddPage( self.panelMODLIST, u"MOD LIST", False )
		self.panelSAVEFILES = wx.Panel( self.notebookSAVEFILESMODS, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizerFILESSAVEBUTTONS = wx.BoxSizer( wx.VERTICAL )

		bSizerSAVEFILESBUTTONS = wx.BoxSizer( wx.HORIZONTAL )

		self.toggleBtnSAVEFILESDELETE = wx.ToggleButton( self.panelSAVEFILES, wx.ID_SAVEFILESDELETE, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerSAVEFILESBUTTONS.Add( self.toggleBtnSAVEFILESDELETE, 0, wx.ALL, 0 )

		self.toggleBtnSAVEFILESBACKUP = wx.ToggleButton( self.panelSAVEFILES, wx.ID_SAVEFILESBACKUP, u"Backup", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.toggleBtnSAVEFILESBACKUP.SetValue( True )
		bSizerSAVEFILESBUTTONS.Add( self.toggleBtnSAVEFILESBACKUP, 0, wx.ALL, 0 )


		bSizerFILESSAVEBUTTONS.Add( bSizerSAVEFILESBUTTONS, 0, wx.ALL|wx.EXPAND, 0 )

		bSizerSAVEFILESFOLDER = wx.BoxSizer( wx.VERTICAL )

		checkListSAVEFILESChoices = []
		self.checkListSAVEFILES = wx.CheckListBox( self.panelSAVEFILES, wx.ID_SAVEFILES, wx.DefaultPosition, wx.DefaultSize, checkListSAVEFILESChoices, 0 )
		bSizerSAVEFILESFOLDER.Add( self.checkListSAVEFILES, 0, wx.ALL|wx.EXPAND, 0 )


		bSizerFILESSAVEBUTTONS.Add( bSizerSAVEFILESFOLDER, 1, wx.ALL|wx.EXPAND, 5 )


		self.panelSAVEFILES.SetSizer( bSizerFILESSAVEBUTTONS )
		self.panelSAVEFILES.Layout()
		bSizerFILESSAVEBUTTONS.Fit( self.panelSAVEFILES )
		self.notebookSAVEFILESMODS.AddPage( self.panelSAVEFILES, u"SAVE FILES", True )

		bSizerMainFrame.Add( self.notebookSAVEFILESMODS, 0, wx.EXPAND |wx.ALL, 0 )


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

		self.menuItemToolsBlender = wx.MenuItem( self.menuTools, wx.ID_ToolsBlender, u"Blender", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuTools.Append( self.menuItemToolsBlender )

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
		self.toggleBtnMODLISTENABLEDISABLE.Bind( wx.EVT_TOGGLEBUTTON, self.toggleBtnMODLISTENABLEDISABLEOnToggleButton )
		self.toggleBtnMODLISTBACKUP.Bind( wx.EVT_TOGGLEBUTTON, self.toggleBtnMODLISTBACKUPOnToggleButton )
		self.checkListMODLIST.Bind( wx.EVT_RIGHT_DCLICK, self.checkListMODLISTOnRightDClick )
		self.toggleBtnSAVEFILESDELETE.Bind( wx.EVT_TOGGLEBUTTON, self.toggleBtnSAVEFILESDELETEOnToggleButton )
		self.toggleBtnSAVEFILESBACKUP.Bind( wx.EVT_TOGGLEBUTTON, self.toggleBtnSAVEFILESBACKUPOnToggleButton )
		self.checkListSAVEFILES.Bind( wx.EVT_RIGHT_DCLICK, self.checkListSAVEFILESOnRightDClick )
		self.Bind( wx.EVT_MENU, self.menuItemFileExitOnMenuSelection, id = self.menuItemFileExit.GetId() )
		self.Bind( wx.EVT_MENU, self.menuItemToolsAssetEditorOnMenuSelection, id = self.menuItemToolsAssetEditor.GetId() )
		self.Bind( wx.EVT_MENU, self.menuItemToolsBlenderOnMenuSelection, id = self.menuItemToolsBlender.GetId() )
		self.Bind( wx.EVT_MENU, self.menuItemToolsHydroneerSaveEditorOnMenuSelection, id = self.menuItemToolsHydroneerSaveEditor.GetId() )
		self.Bind( wx.EVT_MENU, self.menuItemHelpAboutOnMenuSelection, id = self.menuItemHelpAbout.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def toggleBtnMODLISTENABLEDISABLEOnToggleButton( self, event ):
		event.Skip()

	def toggleBtnMODLISTBACKUPOnToggleButton( self, event ):
		event.Skip()

	def checkListMODLISTOnRightDClick( self, event ):
		event.Skip()

	def toggleBtnSAVEFILESDELETEOnToggleButton( self, event ):
		event.Skip()

	def toggleBtnSAVEFILESBACKUPOnToggleButton( self, event ):
		event.Skip()

	def checkListSAVEFILESOnRightDClick( self, event ):
		event.Skip()

	def menuItemFileExitOnMenuSelection( self, event ):
		sys.exit()

	def menuItemToolsAssetEditorOnMenuSelection( self, event ):
		os.startfile('Tools\\Asset Editor.exe')

	def menuItemToolsBlenderOnMenuSelection( self, event ):
		subprocess.run("start steam://run/365670", shell=True)

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

