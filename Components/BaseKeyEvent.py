# -*- coding: utf-8 -*-
# __author__ : Ricky
# __createTime__ : 2021/1/15 14:44
# __fileName__ : GoldenCoordinateV2 BaseKeyEvent.py
# __devIDE__ : PyCharm



from PySide2 import QtWidgets as qtw
from PySide2 import QtGui as qtg
from PySide2 import QtCore as qtc


class BaseKeyEvent(qtw.QWidget):
    def keyPressEvent(self, keySet:qtg.QKeyEvent):
        print(keySet)
        if keySet.key() == qtc.Qt.Key_Escape:
            self.window().showNormal()




