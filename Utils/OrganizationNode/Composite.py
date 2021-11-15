# -*- coding: utf-8 -*-
# __author__ : Ricky
# __createTime__ : 2021/1/21 14:11
# __fileName__ : GoldenCoordinateV2 Composite.py
# __devIDE__ : PyCharm

from Utils.Helper import toJson

class Composite():
    def __init__(self, data):
        self._keys = []
        self.initAttrs(data)

    def initAttrs(self, data):
        for attr in (data or {}):
            self._keys.append(attr)
            setattr(self, attr, data[attr])
    def keys(self):
        return self._keys
    def __str__(self):
        return toJson(dict(self))

    def __getitem__(self, item):
        return getattr(self, item)



