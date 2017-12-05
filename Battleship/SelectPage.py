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
## Class SelectLayer
###########################################################################

class SelectLayer(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title = u"Acorn_BattleShip_선택", pos=wx.DefaultPosition,
                          size=wx.Size(400, 600), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        # self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        # 텍스트
        self.SelectPage1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(400, 50), wx.TAB_TRAVERSAL)
        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.SelectText = wx.StaticText(self.SelectPage1, wx.ID_ANY, u"원하는 메뉴를 고르시오", wx.Point(-1, -1), wx.DefaultSize,
                                        wx.ALIGN_CENTRE)
        self.SelectText.Wrap(-1)
        self.SelectText.SetFont(wx.Font(16, 75, 90, 90, False, "돋움체"))

        bSizer2.Add(self.SelectText, 1, wx.ALL | wx.EXPAND, 10)

        self.SelectPage1.SetSizer(bSizer2)
        self.SelectPage1.Layout()
        bSizer1.Add(self.SelectPage1, 0, wx.ALL | wx.EXPAND, 10)

        # 게임 시작 버튼
        self.SelectPage2 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(400, 50), wx.TAB_TRAVERSAL)
        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.SelectStart = wx.Button(self.SelectPage2, wx.ID_ANY, u"게임 시작", wx.DefaultPosition, wx.Size(400, 20), 0)
        self.SelectStart.SetFont(wx.Font(14, 75, 90, 90, False, "돋움"))
        bSizer3.Add(self.SelectStart, 1, wx.ALL, 22)

        self.SelectPage2.SetSizer(bSizer3)
        self.SelectPage2.Layout()
        bSizer1.Add(self.SelectPage2, 1, wx.EXPAND | wx.ALL, 10)

        # 스코어 버튼
        self.SelectPage3 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(400, 100), wx.TAB_TRAVERSAL)
        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.SelectScore = wx.Button(self.SelectPage3, wx.ID_ANY, u"점수", wx.DefaultPosition, wx.Size(400, 50), 0)
        self.SelectScore.SetFont(wx.Font(14, 75, 90, 90, False, "돋움"))
        bSizer4.Add(self.SelectScore, 1, wx.ALL, 22)

        self.SelectPage3.SetSizer(bSizer4)
        self.SelectPage3.Layout()
        bSizer1.Add(self.SelectPage3, 1, wx.EXPAND | wx.ALL, 10)

        # 게임 설명 버튼
        self.SelectPage4 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(400, 100), wx.TAB_TRAVERSAL)
        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.SelectDescription = wx.Button(self.SelectPage4, wx.ID_ANY, u"게임 설명", wx.DefaultPosition, wx.Size(400, 50), 0)
        self.SelectDescription.SetFont(wx.Font(14, 75, 90, 90, False, "돋움"))
        bSizer5.Add(self.SelectDescription, 1, wx.ALL, 22)

        self.SelectPage4.SetSizer(bSizer5)
        self.SelectPage4.Layout()
        bSizer1.Add(self.SelectPage4, 1, wx.EXPAND | wx.ALL, 10)

        # 뒤로가기 버튼
        self.SelectPage5 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(400, 100), wx.TAB_TRAVERSAL)
        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        self.SelectBack = wx.Button(self.SelectPage5, wx.ID_ANY, u"뒤로 가기", wx.DefaultPosition, wx.Size(400, 50), 0)
        self.SelectBack.SetFont(wx.Font(14, 75, 90, 90, False, "돋움"))
        bSizer6.Add(self.SelectBack, 1, wx.ALL, 22)

        self.SelectPage5.SetSizer(bSizer6)
        self.SelectPage5.Layout()
        bSizer1.Add(self.SelectPage5, 1, wx.EXPAND | wx.ALL, 10)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # 버튼 이벤트 정의
        self.SelectStart.Bind(wx.EVT_BUTTON, self.OnSelectStartClicked)
        self.SelectScore.Bind(wx.EVT_BUTTON, self.OnSelectScoreClicked)
        self.SelectDescription.Bind(wx.EVT_BUTTON, self.OnSelectDescriptionClicked)
        self.SelectBack.Bind(wx.EVT_BUTTON, self.OnSelectBackClicked)

    # OnSelectStartClicked 함수 정의
    def OnSelectStartClicked(self, event):
        # 새 창으로
        self.Close()

        from Battleship.InputIDPage import InputIDLayer
        # 게임 시작을 위한 InputIDLayer Loading
        app = wx.App()
        frame = InputIDLayer(None)

        # Layer 이동
        frame.Show()
        app.MainLoop()

    # OnSelectScoreClicked 함수 정의
    def OnSelectScoreClicked(self, event):
        from Battleship.ScorePage import ScoreLayer

        # 점수화면 Layer Loading
        app = wx.App()
        frame = ScoreLayer(None)

        # Layer 이동
        frame.Show()
        app.MainLoop()

    # OnSelectDescriptionClicked 함수 정의
    def OnSelectDescriptionClicked(self, event):
        from Battleship.DescriptionPage import DescriptionLayer

        # 설명화면 Layer Loading
        app = wx.App()
        frame = DescriptionLayer(None)

        # Layer 이동
        frame.Show()
        app.MainLoop()

    # OnExitButtonClicked 함수 정의
    def OnSelectBackClicked(self, event):
        # 새 창으로
        self.Close()

        from Battleship.MainPage import MainLayer

        # 시작화면 Layer Loading
        app = wx.App()
        frame = MainLayer(None)

        # Layer 이동
        frame.Show()
        app.MainLoop()

    def __del__(self):
        pass



