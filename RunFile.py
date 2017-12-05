'''
BattleShip 게임
'''

import wx.xrc


if __name__ == "__main__" :    # 프로그램의 시작점
    from Battleship.MainPage import MainLayer

    app = wx.App()             # App 생성
    frame = MainLayer(parent= None)          # Frame 객체 생성
    frame.Show()

    app.MainLoop()  # App 실행

