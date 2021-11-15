# -*- coding: utf-8 -*-
# __author__ : Ricky
# __createTime__ : 2021/1/21 11:45
# __fileName__ : GoldenCoordinateV2 DepartMap.py
# __devIDE__ : PyCharm


class DepartMap():

    _childDeparts = None
    _members = None

    def __init__(self):
        self._childDeparts = []
        self._members = []

    def getMembers(self):
        return self._members

    def addMember(self, member):
        self._members.append(member)

    def addChildDepart(self, depart):
        self._childDeparts.append(depart)
    def getChildDeparts(self):
        return self._childDeparts








