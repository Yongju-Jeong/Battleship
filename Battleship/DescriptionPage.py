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
## Class DescriptionLayer
###########################################################################

class DescriptionLayer(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title = u"Acorn_BattleShip_설명", pos=wx.DefaultPosition,
                          size=wx.Size(400, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        # self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))
        
        # 설명 헤드라인 추가
        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"설명", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE)
        self.m_staticText3.Wrap(-1)
        self.m_staticText3.SetFont(wx.Font(14, 75, 90, 90, False, "돋움"))

        bSizer1.Add(self.m_staticText3, 0, wx.ALL | wx.EXPAND, 5)

        self.m_panel3 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer4 = wx.BoxSizer(wx.VERTICAL)
        
        # 설명문 추가
        self.m_textCtrl2 = wx.TextCtrl(self.m_panel3, wx.ID_ANY,  wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                       wx.TE_MULTILINE | wx.TE_READONLY)
        # 설명문 라인별 추가
        self.m_textCtrl2.AppendText("* 이 게임의 진행방식은 다음과 같습니다." + "\n")
        self.m_textCtrl2.AppendText("1. 게임 시작과 동시에 5 x 5의 격자판 중 랜덤한 위치에 목표가 숨겨져 있습니다." + "\n")
        self.m_textCtrl2.AppendText("2. 격자판에서 원하는 곳을 클릭하여 목표의 유무를 확인합니다." + "\n")
        self.m_textCtrl2.AppendText("3. 목표를 찾을때까지 게임은 계속 진행됩니다." + "\n")
        self.m_textCtrl2.AppendText("\n")
        self.m_textCtrl2.AppendText("* 게임의 최종 점수는 다음과 같이 결정됩니다." + "\n")
        self.m_textCtrl2.AppendText("1. 최초 100점이 주어지며 목표가 없는 곳을 클릭할 경우 일정량의 점수가 감소됩니다." + "\n")
        self.m_textCtrl2.AppendText("2. 감소되는 점수는 게임의 경과가 오래 지속될 수록 증가합니다." + "\n")
        self.m_textCtrl2.AppendText("\t\t회차\t감소하는 점수" + "\n")
        self.m_textCtrl2.AppendText("\t\t 1 ~  5\t\t1점" + "\n")
        self.m_textCtrl2.AppendText("\t\t 6 ~ 10\t\t3점" + "\n")
        self.m_textCtrl2.AppendText("\t\t11 ~   \t\t5점" + "\n")
        self.m_textCtrl2.AppendText("3. 최대 점수는 100점이며 최소 점수는 10점 입니다.")

        
        bSizer4.Add(self.m_textCtrl2, 1, wx.ALL | wx.EXPAND, 5)

        self.m_panel3.SetSizer(bSizer4)
        self.m_panel3.Layout()
        bSizer4.Fit(self.m_panel3)
        bSizer1.Add(self.m_panel3, 1, wx.EXPAND | wx.ALL, 0)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass
