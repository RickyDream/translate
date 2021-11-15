# -*- coding: utf-8 -*-
# __author__ : Ricky
# __createTime__ : 2021/1/7 10:47
# __fileName__ : GoldenCoordinateV2 CssLoader.py
# __devIDE__ : PyCharm
from PySide2 import QtWidgets as qtw
from PySide2 import QtGui as qtg
import os

class CssLoader():
    CssBaseDir = 'Resources/Css/'

    @classmethod
    def loadStyleSheet(cls, widget:qtw.QWidget, sheetPath):
        with open(cls.CssBaseDir+sheetPath, 'r', encoding='utf-8') as fr:
            style = fr.read()
            # print(style)
            widget.setStyleSheet(style)


class FontLoader():
    FontBaseDir = 'Resources/Fonts/'
    @classmethod
    def loadFont(cls, filename=None):
        path = cls.FontBaseDir + filename if filename else 'default.ttf'
        if os.path.isfile(path):
            qtg.QFontDatabase.addApplicationFont(path)




