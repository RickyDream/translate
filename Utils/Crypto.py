# -*- coding: utf-8 -*-
# __author__ : Ricky
# __createTime__ : 2021/4/16 11:02
# __fileName__ : GoldenCoordinateV2 Crypto.py
# __devIDE__ : PyCharm

from PySide2 import QtCore as qtc


class Crypto(qtc.QObject):

    @classmethod
    def getMd5(self, data):
        self.md5 = qtc.QCryptographicHash(
            qtc.QCryptographicHash.Md5)
        self.md5.addData(data)
        hash_string = bytes(self.md5.result().toHex()).decode('UTF-8')
        return hash_string




