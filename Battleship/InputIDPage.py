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
## Class InputIDLayer
###########################################################################

class InputIDLayer(wx.Frame):
    user_id = None

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"이름을 입력하시오.", pos=wx.DefaultPosition,
                          size=wx.Size(400, 200), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        # self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        # ID 텍스트
        self.IDText = wx.StaticText(self.m_panel1, wx.ID_ANY, u"이름", wx.DefaultPosition, wx.DefaultSize,
                                    wx.ALIGN_CENTRE)
        self.IDText.Wrap(-1)
        bSizer2.Add(self.IDText, 1, wx.ALIGN_CENTER | wx.ALL, 5)

        # ID 값
        self.ID = wx.TextCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER)
        bSizer2.Add(self.ID, 1, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_panel1.SetSizer(bSizer2)
        self.m_panel1.Layout()
        bSizer2.Fit(self.m_panel1)
        bSizer1.Add(self.m_panel1, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel2 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # 이벤트 함수 정의
        self.ID.Bind(wx.EVT_TEXT_ENTER, self.InputIdEvent)

    # InputIDEvent 정의
    def InputIdEvent(self, event):
        # 창 닫고
        self.Close()

        # ID 받고
        self.user_id = self.ID.GetValue()
        # print(self.user_id)

        from Battleship.GamePage import GameLayer
        # 게임기 키고
        app = wx.App()  # App 생성
        frame = GameLayer(parent=None)  # Frame 객체 생성

        # ID 보내고
        frame.GetUserID(self.user_id)

        # 게임 하자
        frame.Show()
        app.MainLoop()  # App 실행




    def __del__(self):
        pass


