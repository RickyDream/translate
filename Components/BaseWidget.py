# -*- coding: utf-8 -*-
# __author__ : Ricky
# __createTime__ : 2021/1/14 15:10
# __fileName__ : GoldenCoordinateV2 BaseWidget.py
# __devIDE__ : PyCharm


from PySide2 import QtWidgets as qtw
from PySide2 import QtGui as qtg
from PySide2 import QtCore as qtc
from Validators.RegExp import PhoneRegExp,PhoneCodeRegExp
from Components.BaseKeyEvent import BaseKeyEvent

class BaseWidget(BaseKeyEvent):
    def __init__(self,*args, **kwargs):
        """MainWindow constructor"""
        super().__init__(*args, **kwargs)
        # Main UI code goes here
        # 隐藏边框
        # self.setWindowFlags(self.windowFlags() | qtc.Qt.FramelessWindowHint)
        # 背景透明
        # self.setAttribute(qtc.Qt.WA_TranslucentBackground, True)
    # 通用槽函数绑定
    def initCommonSingleSlot(self):
        if hasattr(self, 'btnBack'):
            self.btnBack.clicked.connect(self.btnBackClicked)
        if hasattr(self, 'lineEditAccount'):
            self.lineEditAccount.setValidator(qtg.QRegExpValidator(qtc.QRegExp(PhoneRegExp)))
        if hasattr(self, 'lineEditPhoneCode'):
            self.lineEditPhoneCode.setValidator(qtg.QRegExpValidator(qtc.QRegExp(PhoneCodeRegExp)))
        if hasattr(self, 'btnCloseWin'):
            self.btnCloseWin.clicked.connect(self.btnCloseClicked)
        if hasattr(self, 'btnMiniWin'):
            self.btnMiniWin.clicked.connect(self.btnMiniWinClicked)
        if hasattr(self, 'btnMaxiWin'):
            self.btnMaxiWin.clicked.connect(self.btnMaxiWinClicked)
    def btnCloseClicked(self):
        if getattr(self, 'globalClose', False):
            self.window().appExit()
        else:
            self.close()
            if hasattr(self, 'back'):
                self.back.close()


    def btnBackClicked(self):
        self.hide()
        if hasattr(self, 'back'):
            self.back.show()

    def btnMiniWinClicked(self):
        self.window().showMinimized()
    def btnMaxiWinClicked(self):
        self.window().showMaximized()