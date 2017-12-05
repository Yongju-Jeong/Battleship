# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import random
import MySQLdb

###########################################################################
## Class GameLayer
###########################################################################
config = {
    'host' : '127.0.0.1',
    'user' : 'scott',
    'password' : 'tiger',
    'database' : 'work',
    'port' : 3306,
    'charset':'utf8',
    'use_unicode' : True}

class GameLayer(wx.Frame):
    # 넘겨주고 받을 초기값 설정
    user_id = None
    Count = 0
    Score = 100

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Acorn_BattleShip_게임", pos=wx.DefaultPosition,
                          size=wx.Size(700, 780), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        # self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(700, 80), wx.TAB_TRAVERSAL)
        bSizer3 = wx.BoxSizer(wx.HORIZONTAL)

        # 이름 텍스트
        self.GameIDTxt = wx.StaticText(self.m_panel1, wx.ID_ANY, u"이름", wx.DefaultPosition, wx.DefaultSize, 0)
        self.GameIDTxt.Wrap(-1)
        self.GameIDTxt.SetFont(wx.Font(12, 75, 90, 90, False, "돋움"))

        bSizer3.Add(self.GameIDTxt, 0, wx.ALL, 5)

        # 이름 값
        self.GameID = wx.TextCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                  wx.TE_READONLY)
        self.GameID.SetFont(wx.Font(11, 75, 90, 90, False, "굴림"))

        bSizer3.Add(self.GameID, 0, wx.ALL, 5)
        # 남은 횟수 텍스트
        self.GameLeftTxt = wx.StaticText(self.m_panel1, wx.ID_ANY, u"시도 횟수", wx.DefaultPosition, wx.DefaultSize, 0)
        self.GameLeftTxt.Wrap(-1)
        self.GameLeftTxt.SetFont(wx.Font(12, 75, 90, 90, False, "돋움체"))

        bSizer3.Add(self.GameLeftTxt, 0, wx.ALL, 5)

        # 남은 횟수 값
        self.GameLeft = wx.TextCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                    wx.TE_READONLY)
        self.GameLeft.SetFont(wx.Font(11, 75, 90, 90, False, "굴림"))

        bSizer3.Add(self.GameLeft, 0, wx.ALL, 5)

        # 점수 텍스트
        self.GameScoreTxt = wx.StaticText(self.m_panel1, wx.ID_ANY, u"점수", wx.DefaultPosition, wx.DefaultSize, 0)
        self.GameScoreTxt.Wrap(-1)
        self.GameScoreTxt.SetFont(wx.Font(12, 75, 90, 90, False, "돋움체"))

        bSizer3.Add(self.GameScoreTxt, 0, wx.ALL, 5)

        # 점수 값
        self.GameScore = wx.TextCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                     wx.TE_READONLY)
        self.GameScore.SetFont(wx.Font(11, 75, 90, 90, False, "굴림"))

        bSizer3.Add(self.GameScore, 0, wx.ALL, 5)

        self.m_panel1.SetSizer(bSizer3)
        self.m_panel1.Layout()
        bSizer1.Add(self.m_panel1, 0, wx.ALL | wx.EXPAND, 1)

        # 떴다 떴다 비행기 25대
        self.m_panel3 = wx.Panel(self, 0, wx.DefaultPosition, wx.Size(700, 700), wx.TAB_TRAVERSAL)
        gSizer1 = wx.GridSizer(5, 5, 0, 0)

        # 비행기 출발
        self.Plane1 = wx.BitmapButton(self.m_panel3, 1, wx.Bitmap(u"target.bmp", wx.BITMAP_TYPE_ANY),
                                      wx.DefaultPosition, wx.Size(130, 130), wx.BU_AUTODRAW)
        gSizer1.Add(self.Plane1, 0, wx.ALL, 1)

        self.Plane2 = wx.BitmapButton(self.m_panel3, 2, wx.Bitmap(u"target.bmp", wx.BITMAP_TYPE_ANY),
                                      wx.DefaultPosition, wx.Size(130, 130), wx.BU_AUTODRAW)
        gSizer1.Add(self.Plane2, 0, wx.ALL, 1)

        self.Plane3 = wx.BitmapButton(self.m_panel3, 3, wx.Bitmap(u"target.bmp", wx.BITMAP_TYPE_ANY),
                                      wx.DefaultPosition, wx.Size(130, 130), wx.BU_AUTODRAW)
        gSizer1.Add(self.Plane3, 0, wx.ALL, 1)

        self.Plane4 = wx.BitmapButton(self.m_panel3, 4, wx.Bitmap(u"target.bmp", wx.BITMAP_TYPE_ANY),
                                      wx.DefaultPosition, wx.Size(130, 130), wx.BU_AUTODRAW)
        gSizer1.Add(self.Plane4, 0, wx.ALL, 1)

        self.Plane5 = wx.BitmapButton(self.m_panel3, 5, wx.Bitmap(u"target.bmp", wx.BITMAP_TYPE_ANY),
                                      wx.DefaultPosition, wx.Size(130, 130), wx.BU_AUTODRAW)
        gSizer1.Add(self.Plane5, 0, wx.ALL, 1)

        self.Plane6 = wx.BitmapButton(self.m_panel3, 6, wx.Bitmap(u"target.bmp", wx.BITMAP_TYPE_ANY),
                                      wx.DefaultPosition, wx.Size(130, 130), wx.BU_AUTODRAW)
        gSizer1.Add(self.Plane6, 0, wx.ALL, 1)

        self.Plane7 = wx.BitmapButton(self.m_panel3, 7, wx.Bitmap(u"target.bmp", wx.BITMAP_TYPE_ANY),
                                      wx.DefaultPosition, wx.Size(130, 130), wx.BU_AUTODRAW)
        gSizer1.Add(self.Plane7, 0, wx.ALL, 1)

        self.Plane8 = wx.BitmapButton(self.m_panel3, 8, wx.Bitmap(u"target.bmp", wx.BITMAP_TYPE_ANY),
                                      wx.DefaultPosition, wx.Size(130, 130), wx.BU_AUTODRAW)
        gSizer1.Add(self.Plane8, 0, wx.ALL, 1)

        self.Plane9 = wx.BitmapButton(self.m_panel3, 9, wx.Bitmap(u"target.bmp", wx.BITMAP_TYPE_ANY),
                                      wx.DefaultPosition, wx.Size(130, 130), wx.BU_AUTODRAW)
        gSizer1.Add(self.Plane9, 0, wx.ALL, 1)

        self.Plane10 = wx.BitmapButton(self.m_panel3, 10, wx.Bitmap(u"target.bmp", wx.BITMAP_TYPE_ANY),
                                       wx.DefaultPosition, wx.Size(130, 130), wx.BU_AUTODRAW)
        gSizer1.Add(self.Plane10, 0, wx.ALL, 1)

        self.Plane11 = wx.BitmapButton(self.m_panel3, 11, wx.Bitmap(u"target.bmp", wx.BITMAP_TYPE_ANY),
                                       wx.DefaultPosition, wx.Size(130, 130), wx.BU_AUTODRAW)
        gSizer1.Add(self.Plane11, 0, wx.ALL, 1)

        self.Plane12 = wx.BitmapButton(self.m_panel3, 12, wx.Bitmap(u"target.bmp", wx.BITMAP_TYPE_ANY),
                                       wx.DefaultPosition, wx.Size(130, 130), wx.BU_AUTODRAW)
        gSizer1.Add(self.Plane12, 0, wx.ALL, 1)

        self.Plane13 = wx.BitmapButton(self.m_panel3, 13, wx.Bitmap(u"target.bmp", wx.BITMAP_TYPE_ANY),
                                       wx.DefaultPosition, wx.Size(130, 130), wx.BU_AUTODRAW)
        gSizer1.Add(self.Plane13, 0, wx.ALL, 1)

        self.Plane14 = wx.BitmapButton(self.m_panel3, 14, wx.Bitmap(u"target.bmp", wx.BITMAP_TYPE_ANY),
                                       wx.DefaultPosition, wx.Size(130, 130), wx.BU_AUTODRAW)
        gSizer1.Add(self.Plane14, 0, wx.ALL, 1)

        self.Plane15 = wx.BitmapButton(self.m_panel3, 15, wx.Bitmap(u"target.bmp", wx.BITMAP_TYPE_ANY),
                                       wx.DefaultPosition, wx.Size(130, 130), wx.BU_AUTODRAW)
        gSizer1.Add(self.Plane15, 0, wx.ALL, 1)

        self.Plane16 = wx.BitmapButton(self.m_panel3, 16, wx.Bitmap(u"target.bmp", wx.BITMAP_TYPE_ANY),
                                       wx.DefaultPosition, wx.Size(130, 130), wx.BU_AUTODRAW)
        gSizer1.Add(self.Plane16, 0, wx.ALL, 1)

        self.Plane17 = wx.BitmapButton(self.m_panel3, 17, wx.Bitmap(u"target.bmp", wx.BITMAP_TYPE_ANY),
                                       wx.DefaultPosition, wx.Size(130, 130), wx.BU_AUTODRAW)
        gSizer1.Add(self.Plane17, 0, wx.ALL, 1)

        self.Plane18 = wx.BitmapButton(self.m_panel3, 18, wx.Bitmap(u"target.bmp", wx.BITMAP_TYPE_ANY),
                                       wx.DefaultPosition, wx.Size(130, 130), wx.BU_AUTODRAW)
        gSizer1.Add(self.Plane18, 0, wx.ALL, 1)

        self.Plane19 = wx.BitmapButton(self.m_panel3, 19, wx.Bitmap(u"target.bmp", wx.BITMAP_TYPE_ANY),
                                       wx.DefaultPosition, wx.Size(130, 130), wx.BU_AUTODRAW)
        gSizer1.Add(self.Plane19, 0, wx.ALL, 1)

        self.Plane20 = wx.BitmapButton(self.m_panel3, 20, wx.Bitmap(u"target.bmp", wx.BITMAP_TYPE_ANY),
                                       wx.DefaultPosition, wx.Size(130, 130), wx.BU_AUTODRAW)
        gSizer1.Add(self.Plane20, 0, wx.ALL, 1)

        self.Plane21 = wx.BitmapButton(self.m_panel3, 21, wx.Bitmap(u"target.bmp", wx.BITMAP_TYPE_ANY),
                                       wx.DefaultPosition, wx.Size(130, 130), wx.BU_AUTODRAW)
        gSizer1.Add(self.Plane21, 0, wx.ALL, 1)

        self.Plane22 = wx.BitmapButton(self.m_panel3, 22, wx.Bitmap(u"target.bmp", wx.BITMAP_TYPE_ANY),
                                       wx.DefaultPosition, wx.Size(130, 130), wx.BU_AUTODRAW)
        gSizer1.Add(self.Plane22, 0, wx.ALL, 1)

        self.Plane23 = wx.BitmapButton(self.m_panel3, 23, wx.Bitmap(u"target.bmp", wx.BITMAP_TYPE_ANY),
                                       wx.DefaultPosition, wx.Size(130, 130), wx.BU_AUTODRAW)
        gSizer1.Add(self.Plane23, 0, wx.ALL, 1)

        self.Plane24 = wx.BitmapButton(self.m_panel3, 24, wx.Bitmap(u"target.bmp", wx.BITMAP_TYPE_ANY),
                                       wx.DefaultPosition, wx.Size(130, 130), wx.BU_AUTODRAW)
        gSizer1.Add(self.Plane24, 0, wx.ALL, 1)

        self.Plane25 = wx.BitmapButton(self.m_panel3, 25, wx.Bitmap(u"target.bmp", wx.BITMAP_TYPE_ANY),
                                       wx.DefaultPosition, wx.Size(130, 130), wx.BU_AUTODRAW)
        gSizer1.Add(self.Plane25, 0, wx.ALL, 1)

        self.m_panel3.SetSizer(gSizer1)
        self.m_panel3.Layout()
        bSizer1.Add(self.m_panel3, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # 초기값 입력(ID 제외)
        self.GameLeft.SetValue(str(self.Count))
        self.GameScore.SetValue(str(self.Score))

        # 정답이 될 Ans 변수 생성
        self.TargetNumber = random.randint(1, 25)
        print(self.TargetNumber)

        # 중복 클릭을 막기위한 카운터 리스트 생성
        self.IsClicked = [0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0]

        # 비행기 버튼별 클릭 입력 함수 정의
        self.Plane1.Bind(wx.EVT_BUTTON, self.ComparePlaneID)
        self.Plane2.Bind(wx.EVT_BUTTON, self.ComparePlaneID)
        self.Plane3.Bind(wx.EVT_BUTTON, self.ComparePlaneID)
        self.Plane4.Bind(wx.EVT_BUTTON, self.ComparePlaneID)
        self.Plane5.Bind(wx.EVT_BUTTON, self.ComparePlaneID)
        self.Plane6.Bind(wx.EVT_BUTTON, self.ComparePlaneID)
        self.Plane7.Bind(wx.EVT_BUTTON, self.ComparePlaneID)
        self.Plane8.Bind(wx.EVT_BUTTON, self.ComparePlaneID)
        self.Plane9.Bind(wx.EVT_BUTTON, self.ComparePlaneID)
        self.Plane10.Bind(wx.EVT_BUTTON, self.ComparePlaneID)
        self.Plane11.Bind(wx.EVT_BUTTON, self.ComparePlaneID)
        self.Plane12.Bind(wx.EVT_BUTTON, self.ComparePlaneID)
        self.Plane13.Bind(wx.EVT_BUTTON, self.ComparePlaneID)
        self.Plane14.Bind(wx.EVT_BUTTON, self.ComparePlaneID)
        self.Plane15.Bind(wx.EVT_BUTTON, self.ComparePlaneID)
        self.Plane16.Bind(wx.EVT_BUTTON, self.ComparePlaneID)
        self.Plane17.Bind(wx.EVT_BUTTON, self.ComparePlaneID)
        self.Plane18.Bind(wx.EVT_BUTTON, self.ComparePlaneID)
        self.Plane19.Bind(wx.EVT_BUTTON, self.ComparePlaneID)
        self.Plane20.Bind(wx.EVT_BUTTON, self.ComparePlaneID)
        self.Plane21.Bind(wx.EVT_BUTTON, self.ComparePlaneID)
        self.Plane22.Bind(wx.EVT_BUTTON, self.ComparePlaneID)
        self.Plane23.Bind(wx.EVT_BUTTON, self.ComparePlaneID)
        self.Plane24.Bind(wx.EVT_BUTTON, self.ComparePlaneID)
        self.Plane25.Bind(wx.EVT_BUTTON, self.ComparePlaneID)


    # ID 넘겨 받기 - 화면 설정
    def GetUserID(self, user_id):
        self.user_id = user_id
        self.GameID.SetValue(self.user_id)

    # 점수 감소 함수
    def ScoreLose(self):
        if self.Count >= 0 and self.Count < 6 :
            return (self.Score - 1)
        elif self.Count >= 6 and self.Count < 11 :
            return (self.Score - 3)
        else :
            return (self.Score - 5)

    # 클릭 이벤트에 대한 함수 정의
    def ComparePlaneID(self, event):
        eid = event.Id

        print(self.IsClicked[eid - 1])
        if eid == self.TargetNumber and self.IsClicked[eid - 1] == 0:
            self.Count += 1

            # DB 연동
            id = str(self.user_id)
            score = str(self.Score)
            # print(id, score)

            try:
                conn = MySQLdb.connect(**config)
                cursor = conn.cursor()

                # 테이블 유무 검사
                sql = "show tables"
                cursor.execute(sql)  # table 검색
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

                sdata = (id, score)
                # print(sdata)

                # 레코드 추가
                sql = "insert into battleshipscore values( %s, %s)"
                cursor.execute(sql, sdata)
                conn.commit()
                # print('Success')

            except Exception as e:
                print('db 연동 오류 : ', e)
                conn.rollback()

            finally:
                cursor.close()
                conn.close()

            # 게임창 닫고
            self.Close()

            from Battleship.ResultPage import ResultLayer

            # 결과창 키고
            app = wx.App()  # App 생성
            frame = ResultLayer(parent=None)  # Frame 객체 생성

            # ID 보내고
            frame.GetResult(self.user_id, self.Count, self.Score)
            # print(self.user_id, self.Count, self.Score)

            # 게임 하자
            frame.Show()
            app.MainLoop()  # App 실행
        elif eid != self.TargetNumber and self.IsClicked[eid - 1] == 0:
            # 표시값 변경
            self.Count += 1
            self.Score = self.ScoreLose()

            # 표시값 개입력
            self.GameLeft.SetValue(str(self.Count))
            self.GameScore.SetValue(str(self.Score))

            # 이미지 변경
            event.GetEventObject().SetBitmapLabel(wx.Bitmap(u"wrong.bmp", wx.BITMAP_TYPE_ANY))

            # IsClicked 카운터 리스트 값 올리기
            self.IsClicked[eid - 1] = 1
            print(self.IsClicked)
        elif eid == self.TargetNumber and self.IsClicked[eid - 1] != 0:
            # 이런 경우가 있을수가 없음
            pass
        elif eid != self.TargetNumber and self.IsClicked[eid - 1] != 0:
            print('Wrong Input')


    def __del__(self):
        pass
