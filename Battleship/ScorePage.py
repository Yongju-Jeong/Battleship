# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import MySQLdb

config = {
    'host' : '127.0.0.1',
    'user' : 'scott',
    'password' : 'tiger',
    'database' : 'work',
    'port' : 3306,
    'charset':'utf8',
    'use_unicode' : True}
###########################################################################
## Class ScoreLayer
###########################################################################

class ScoreLayer(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Acorn_BattleShip_점수", pos=wx.DefaultPosition,
                          size=wx.Size(400, 280), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        # self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel2 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        # 점수 List
        self.ScoreList = wx.ListCtrl(self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT | wx.LC_SORT_ASCENDING)
        bSizer4.Add(self.ScoreList, 1, wx.ALL | wx.EXPAND, 5)

        self.m_panel2.SetSizer(bSizer4)
        self.m_panel2.Layout()
        bSizer4.Fit(self.m_panel2)
        bSizer3.Add(self.m_panel2, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel3 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        # 초기화 버튼
        self.ScoreClear = wx.Button(self.m_panel3, wx.ID_ANY, u"초기화", wx.DefaultPosition, wx.DefaultSize, 0)
        self.ScoreClear.SetFont(wx.Font(14, 75, 90, 90, False, "돋움"))
        bSizer5.Add(self.ScoreClear, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_panel3.SetSizer(bSizer5)
        self.m_panel3.Layout()
        bSizer5.Fit(self.m_panel3)
        bSizer3.Add(self.m_panel3, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer3)
        self.Layout()

        self.Centre(wx.BOTH)

        # 컬럼 초기화
        self.ScoreList.InsertColumn(0, '이름', wx.LIST_FORMAT_LEFT, width = 200)
        self.ScoreList.InsertColumn(1, '점수', wx.LIST_FORMAT_LEFT, width = 161)

        # DB 초기화
        self.InitDB()

        # 초기화 버튼 함수 정의
        self.ScoreClear.Bind(wx.EVT_BUTTON, self.OnScoreClearClicked)

    # InitDB 정의
    def InitDB(self):
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            sql = "show tables"
            cursor.execute(sql)  # table 검색

            # 테이블 유무 검사
            tables = cursor.fetchall()
            tables_num = 0
            for i in tables:
                tables_num += 1
                if i[0] == 'battleshipscore':  # product 테이블 있는 경우
                    print('battleshipscore table exist')
                    break;  # 테이블 있으면 반복 탈출

                elif tables_num == len(tables):  # 테이블 없는 경우
                    sql = "create table battleshipscore(id VARCHAR (20), score VARCHAR (20))"
                    cursor.execute(sql)
                    print('create BattleShipScore table')

            # DB 전체 조회
            sql = "select * from battleshipscore"
            cursor.execute(sql)
            datas = cursor.fetchall()

            if len(datas) > 0:
                for row in datas:
                    i = self.ScoreList.InsertItem(5, 0)
                    self.ScoreList.SetItem(i, 0, str(row[0]))
                    self.ScoreList.SetItem(i, 1, row[1])

        except Exception as e:
            print('db 연동 오류 : ', e)
            conn.rollback()

        finally:
            cursor.close()
            conn.close()


     # OnScoreClearClicked 정의
    def OnScoreClearClicked(self, event):
        try:
            # 전체 삭제
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            sql = "delete from battleshipscore"
            cursor.execute(sql)
            conn.commit()

            # DB 전체 조회
            sql = "select * from battleshipscore"
            cursor.execute(sql)
            datas = cursor.fetchall()

            self.ScoreList.DeleteAllItems()

            if len(datas) > 0:
                for row in datas:
                    i = self.ScoreList.InsertItem(5, 0)
                    self.ScoreList.SetItem(i, 0, str(row[0]))
                    self.ScoreList.SetItem(i, 1, row[1])

        except Exception as e:
            print('db 연동 오류 : ', e)
            conn.rollback()

        finally:
            cursor.close()
            conn.close()

    def __del__(self):
        pass

