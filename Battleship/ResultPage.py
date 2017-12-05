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
## Class ResultLayer
###########################################################################

class ResultLayer(wx.Frame):
    # 넘겨주고 받을 초기값 설정
    user_id = None
    Count = 0
    Score = 0

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Acorn_BattleShip_결과", pos=wx.DefaultPosition,
                          size=wx.Size(400, 250), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        # self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel3 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        # 제목
        self.ResultText = wx.StaticText(self.m_panel3, wx.ID_ANY, u"결과", wx.DefaultPosition, wx.DefaultSize, 0)
        self.ResultText.Wrap(-1)
        self.ResultText.SetFont(wx.Font(12, 75, 90, 90, False, "돋움"))

        bSizer9.Add(self.ResultText, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_panel3.SetSizer(bSizer9)
        self.m_panel3.Layout()
        bSizer9.Fit(self.m_panel3)
        bSizer4.Add(self.m_panel3, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel4 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer6 = wx.BoxSizer(wx.HORIZONTAL)

        # 이름
        self.ResultIDTxt = wx.StaticText(self.m_panel4, wx.ID_ANY, u"이름", wx.DefaultPosition, wx.DefaultSize,
                                           wx.ALIGN_CENTRE)
        self.ResultIDTxt.Wrap(-1)
        bSizer6.Add(self.ResultIDTxt, 1, wx.ALL, 5)

        self.ResultID = wx.TextCtrl(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                      wx.TE_LEFT | wx.TE_READONLY)
        bSizer6.Add(self.ResultID, 1, wx.ALL, 5)

        self.m_panel4.SetSizer(bSizer6)
        self.m_panel4.Layout()

        bSizer6.Fit(self.m_panel4)
        bSizer4.Add(self.m_panel4, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel5 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer7 = wx.BoxSizer(wx.HORIZONTAL)

        # 횟수
        self.ResultCountTxt = wx.StaticText(self.m_panel5, wx.ID_ANY, u"횟수", wx.DefaultPosition, wx.DefaultSize,
                                            wx.ALIGN_CENTRE)
        self.ResultCountTxt.Wrap(-1)
        bSizer7.Add(self.ResultCountTxt, 1, wx.ALL, 5)

        self.ResultCount = wx.TextCtrl(self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                       wx.TE_LEFT | wx.TE_READONLY)
        bSizer7.Add(self.ResultCount, 1, wx.ALL, 5)

        self.m_panel5.SetSizer(bSizer7)
        self.m_panel5.Layout()
        bSizer7.Fit(self.m_panel5)
        bSizer4.Add(self.m_panel5, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel6 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)

        # 점수
        self.ResultScoreTxt = wx.StaticText(self.m_panel6, wx.ID_ANY, u"점수", wx.DefaultPosition, wx.DefaultSize,
                                            wx.ALIGN_CENTRE)
        self.ResultScoreTxt.Wrap(-1)
        bSizer8.Add(self.ResultScoreTxt, 1, wx.ALL, 5)

        self.ResultScore = wx.TextCtrl(self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                       wx.TE_LEFT | wx.TE_READONLY)
        bSizer8.Add(self.ResultScore, 1, wx.ALL, 5)

        self.m_panel6.SetSizer(bSizer8)
        self.m_panel6.Layout()
        bSizer8.Fit(self.m_panel6)
        bSizer4.Add(self.m_panel6, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel51 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer61 = wx.BoxSizer(wx.VERTICAL)

        # 버튼
        self.ButtonOK = wx.Button(self.m_panel51, wx.ID_ANY, u"확인", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer61.Add(self.ButtonOK, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_panel51.SetSizer(bSizer61)
        self.m_panel51.Layout()
        bSizer61.Fit(self.m_panel51)
        bSizer4.Add(self.m_panel51, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer4)
        self.Layout()

        self.Centre(wx.BOTH)

        # 확인 버튼 함수 연동
        self.ButtonOK.Bind(wx.EVT_BUTTON, self.ReturnSelectPage)

    # 출력값 받아오기
    def GetResult(self, user_id, user_count, user_score):
        self.user_id = user_id
        self.ResultID.SetValue(str(self.user_id))

        self.Count = user_count
        self.ResultCount.SetValue(str(self.Count))

        self.Score = user_score
        self.ResultScore.SetValue(str(self.Score))

    # 돌아가기
    def ReturnSelectPage(self, event) :
        self.Close()

        from Battleship.SelectPage import SelectLayer

        app = wx.App()
        frame = SelectLayer(None)

        # Layer 이동
        frame.Show()
        app.MainLoop()

    def __del__(self):
        pass


