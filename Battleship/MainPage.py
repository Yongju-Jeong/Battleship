# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc



###########################################################################
## Class MainLayer
###########################################################################

class MainLayer(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title = u"Acorn_BattleShip_시작", pos=wx.DefaultPosition,
                          size=wx.Size(400, 500), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        # self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        # 이미지
        self.MainPage1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(400, 250), wx.TAB_TRAVERSAL)
        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        bSizer2.SetMinSize(wx.Size(400, 250))
        self.MainImage = wx.StaticBitmap(self.MainPage1, wx.ID_ANY, wx.Bitmap(u"plane.bmp", wx.BITMAP_TYPE_ANY),
                                         wx.Point(-1, -1), wx.DefaultSize, 0)
        bSizer2.Add(self.MainImage, 1, wx.ALL | wx.EXPAND, 5)


        self.MainPage1.SetSizer(bSizer2)
        self.MainPage1.Layout()
        bSizer1.Add(self.MainPage1, 1, wx.EXPAND | wx.ALL, 5)

        # 버튼 1
        self.MainPage2 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(200, 70), wx.TAB_TRAVERSAL)
        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.StartButton = wx.Button(self.MainPage2, wx.ID_ANY, u"시작", wx.DefaultPosition, wx.Size(150, 100), 0)
        self.StartButton.SetFont(wx.Font(14, 75, 90, 90, False, "돋움"))
        bSizer3.Add(self.StartButton, 1, wx.ALIGN_CENTER | wx.ALL, 30)

        self.MainPage2.SetSizer(bSizer3)
        self.MainPage2.Layout()
        bSizer1.Add(self.MainPage2, 1, wx.ALL | wx.EXPAND, 5)

        # 버튼 2
        self.MainPage3 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(200, 70), wx.TAB_TRAVERSAL)
        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.ExitButton = wx.Button(self.MainPage3, wx.ID_ANY, u"종료", wx.DefaultPosition, wx.Size(150, 100), 0)
        self.ExitButton.SetFont(wx.Font(14, 75, 90, 90, False, "돋움"))
        bSizer4.Add(self.ExitButton, 1, wx.ALIGN_CENTER | wx.ALL, 30)

        self.MainPage3.SetSizer(bSizer4)
        self.MainPage3.Layout()
        bSizer1.Add(self.MainPage3, 1, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # 버튼 이벤트 정의
        self.StartButton.Bind(wx.EVT_BUTTON, self.OnStartButtonClicked)
        self.ExitButton.Bind(wx.EVT_BUTTON, self.OnExitButtonClicked)

    # OnStartButtonClicked 함수 정의
    def OnStartButtonClicked(self, event):
        self.Close()

        from Battleship.SelectPage import SelectLayer

        app = wx.App()
        frame = SelectLayer(None)

        # Layer 이동
        frame.Show()
        app.MainLoop()

        # OnExitButtonClicked 함수 정의
    def OnExitButtonClicked(self, event):
        self.Close()

    def __del__(self):
        pass
